"""clone.py - レイアウトサブパイプライン 7 サブステップの実行スクリプト

/codi ステップ 2 (implementation) がレイアウトタスクの場合に呼び出される
サブステップエントリポイント。本元リポジトリでは /codi 自体が使えないため、
clone.py 単体での起動にも対応する (IS_SOURCE ガードなし)。

使い方:
    python core/clone.py <subcommand> <task_id>

サブコマンド (= constants.LAYOUT_SUBSTEPS):
    recon     取材 (Node + Playwright で参考サイトから取得)
    dump      本棚化 (.libs/storybook/ に下書き)
    apply     要望適用 (元サイト < 要望)
    rules     ルール適用 (ハードコ禁止 / iOS / Tailwind v4)
    build     部品実装 (.tsx + .stories.tsx 生成)
    assemble  ページ統合 (page.tsx + SEO)
    baseline  VRT 基準作成 (pixel-perfect 基準スクショ)

詳細: .libs/research/webclone/rsrc-webclone-codi-integration.md
"""

import io
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import LIBS_DIR, NXT_ROOT, PROJECT_ROOT
from constants import (
    LAYOUT_SUBSTEPS,
    STORYBOOK_SHELF_NAME,
    STORYBOOK_INPUT_FILENAME,
    RECON_REFERENCE_SECTION_SUFFIX,
    RECON_REQUEST_SECTION_SUFFIX,
    RECON_NOTE_SECTION_SUFFIX,
    RECON_OUTPUT_DIR_NAME,
    RECON_SITE_DIR_PREFIX,
    RECON_VIEWPORTS,
    RECON_NODE_DIR_NAME,
    RECON_NODE_SCRIPT_FILENAME,
    RECON_NODE_TIMEOUT_SEC,
    RECON_TEXT_ONLY_MARKER_FILENAME,
    BASELINE_NODE_SCRIPT_FILENAME,
    BASELINE_NODE_TIMEOUT_SEC,
    BASELINE_OUTPUT_DIR_NAME,
    BASELINE_STORYBOOK_PORT,
    ANIM_LIB_PATTERNS_FILENAME,
    SCROLL_SAMPLING_STEPS,
    SCROLL_TRACKED_SELECTORS,
    SCROLL_SAMPLES_FILENAME,
    RECON_ASSETS_DIR_NAME,
    DIFF_NODE_SCRIPT_FILENAME,
    DIFF_NODE_TIMEOUT_SEC,
    DIFF_OUTPUT_DIR_NAME,
    DIFF_IMAGE_PREFIX,
    DIFF_RESULT_FILENAME,
    DIFF_PIXELMATCH_THRESHOLD,
    DIFF_MAX_MISMATCH_RATIO,
)
from page_parser import parse_header, parse_sections
from feedback import init_error_handling

init_error_handling()


# --- サブステップハンドラ (全てスタブ) ---
#
# 各ハンドラは「未実装」メッセージを出して exit 0 で終わる。
# スタブ段階では手動テスト用途で /codi からは呼ばれない。
# サブステップを実装するときに、この関数の中身を書き換えていく。


def _stub(substep: str, task_id: str) -> None:
    """未実装ハンドラ共通処理。"""
    print(f"clone: {substep} は未実装 (task={task_id})")


def _input_path(task_id: str):
    """レイアウトタスクの取材入力ファイルのパスを返す。"""
    if LIBS_DIR is None:
        return None
    return LIBS_DIR / STORYBOOK_SHELF_NAME / task_id.lower() / STORYBOOK_INPUT_FILENAME


def _build_input_template(task_id: str) -> str:
    """recon 取材入力ファイル (input.md) のテンプレを生成する。"""
    return (
        f"# {task_id} — <部品名> 取材入力\n"
        "\n"
        "関連: \n"
        "タグ: storybook, 取材入力\n"
        "\n"
        f"## {task_id}{RECON_REFERENCE_SECTION_SUFFIX} — 参考サイト\n"
        "- https://example.com/\n"
        "\n"
        f"## {task_id}.採用ライブラリ — 採用ライブラリ指定 (任意)\n"
        "- (空欄なら recon 検出結果から自動選択)\n"
        "<!-- 指定する場合は gsap / motion / lenis / r3f / lottie / pure-css のいずれかを書く -->\n"
        "\n"
        f"## {task_id}.要望 — 要望\n"
        "- \n"
        "\n"
        f"## {task_id}.メモ — メモ\n"
        "- \n"
    )


def _extract_reference_urls(content: str) -> list[str]:
    """input.md の `## <TASK-ID>.参考サイト` セクション配下から URL を抽出する。

    箇条書き (`- https://...` / `* https://...`) 形式の URL だけを拾う。
    """
    urls: list[str] = []
    for sec in parse_sections(content):
        if not sec["id"].endswith(RECON_REFERENCE_SECTION_SUFFIX):
            continue
        for line in sec["content"].split("\n"):
            m = re.match(r"^\s*[-*]\s+(https?://\S+)", line)
            if m:
                urls.append(m.group(1))
    return urls


def _extract_section_body(content: str, suffix: str) -> str:
    """input.md の特定サフィックスを持つセクションの本文を返す。

    複数該当がある場合は先頭のセクションだけ返す。見つからなければ空文字。
    """
    for sec in parse_sections(content):
        if sec["id"].endswith(suffix):
            return sec["content"].strip()
    return ""


def _has_non_placeholder_body(body: str) -> bool:
    """セクション本文が実質的に記入されているかを判定する。

    箇条書きの `- ` だけの行 / 空行 / テンプレート状態は「未記入」扱い。
    """
    for line in body.split("\n"):
        stripped = line.strip()
        if not stripped:
            continue
        # 箇条書きで中身が空なら未記入扱い
        if stripped in {"-", "*", "- ", "* "}:
            continue
        # 記号だけの行でもなく 2 文字以上あれば記入と見なす
        if len(stripped.lstrip("-* ")) >= 2:
            return True
    return False


def _find_playwright_cli() -> tuple[str | None, int, str]:
    """プロジェクトローカルの playwright パッケージを node_modules/.bin/ で検査する。

    recon は Node スクリプト経由で chromium を起動するが、playwright パッケージ
    自体の存在確認には node_modules/.bin/playwright が最も確実な指標になる。

    Returns: (playwright_path, exit_code, error_message)
      - 見つかった   : (path, 0, "")
      - node_modules なし : (None, 3, メッセージ)
      - playwright なし    : (None, 4, メッセージ)
    """
    if PROJECT_ROOT is None:
        return None, 3, "PROJECT_ROOT を特定できません。"

    bin_dir = PROJECT_ROOT / "node_modules" / ".bin"
    if not bin_dir.exists():
        return None, 3, (
            f"node_modules/ が見つかりません: {bin_dir.parent}\n"
            "  プロジェクトで `npm install` を実行してください。"
        )

    # shutil.which は path 引数の中を検索し、Windows では .cmd / .exe を自動解決する
    playwright_path = shutil.which("playwright", path=str(bin_dir))
    if playwright_path is None:
        return None, 4, (
            "Playwright がインストールされていません。\n"
            "プロジェクトルートで次を実行してください:\n"
            "  npm install -D playwright\n"
            "  npx playwright install chromium"
        )

    return playwright_path, 0, ""


def _find_node_executable() -> tuple[str | None, str]:
    """システム PATH から `node` 実行ファイルを探す。

    Windows では .exe / .cmd を shutil.which が自動解決する。

    Returns: (node_path, error_message)
    """
    node_path = shutil.which("node")
    if node_path is None:
        return None, (
            "Node.js が見つかりません。\n"
            "Node 18 以上をインストールしてから再実行してください。"
        )
    return node_path, ""


def _find_recon_script() -> tuple[Path | None, str]:
    """core/clone_node/recon.mjs の実パスを返す。

    本元・プロジェクト両方で paths.NXT_ROOT から算出できる
    (本元: <repo>/core/clone_node/recon.mjs,
     プロジェクト: .nxt-core/core/clone_node/recon.mjs)。
    """
    script = NXT_ROOT / "core" / RECON_NODE_DIR_NAME / RECON_NODE_SCRIPT_FILENAME
    if not script.exists():
        return None, f"recon スクリプトが見つかりません: {script}"
    return script, ""


def _anim_lib_patterns_path() -> Path:
    """clone_node/anim_lib_patterns.json のパスを返す。"""
    return NXT_ROOT / "core" / RECON_NODE_DIR_NAME / ANIM_LIB_PATTERNS_FILENAME


def _load_anim_lib_patterns() -> dict:
    """SSOT の anim_lib_patterns.json を読み込む (Python 側から参照する用)。

    recon.mjs も同じファイルを読むので、変更時の追従は本 JSON 1 箇所で済む。
    """
    path = _anim_lib_patterns_path()
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {"patterns": [], "selectPriority": []}


def _run_node_recon(
    node_path: str,
    script: Path,
    url: str,
    output_dir: Path,
    viewports: list[tuple[str, tuple[int, int]]],
    assets_dir: Path | None = None,
) -> tuple[bool, str]:
    """recon.mjs を 1 回起動して全ビューポートを一括取材する。

    ライブラリ検出 / スクロールサンプリング / Lottie・Rive 自動 DL を有効にするため、
    `--scroll-steps` / `--scroll-selectors` / `--assets-dir` を渡す。

    Returns: (success, message)
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [node_path, str(script), url, str(output_dir)]
    for name, (w, h) in viewports:
        cmd.extend(["--viewport", f"{name}:{w}x{h}"])
    cmd.extend(["--scroll-steps", str(SCROLL_SAMPLING_STEPS)])
    cmd.extend(["--scroll-selectors", ",".join(SCROLL_TRACKED_SELECTORS)])
    if assets_dir is not None:
        assets_dir.mkdir(parents=True, exist_ok=True)
        cmd.extend(["--assets-dir", str(assets_dir)])

    # cwd はプロジェクトルート。Node の node_modules 解決が PROJECT_ROOT/node_modules/
    # に到達できるようにするため (recon.mjs が `import { chromium } from 'playwright'` で
    # ベアインポートするので、cwd から上方向にモジュール解決される)。
    cwd = PROJECT_ROOT if PROJECT_ROOT is not None else None

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=RECON_NODE_TIMEOUT_SEC,
            cwd=str(cwd) if cwd else None,
            encoding="utf-8",
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return False, f"タイムアウト ({RECON_NODE_TIMEOUT_SEC} 秒)"
    except OSError as exc:
        return False, f"実行エラー: {exc}"

    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        return False, (
            f"recon.mjs が失敗しました (exit={result.returncode})\n"
            f"  stderr: {stderr}\n"
            f"  stdout: {stdout}"
        )

    return True, (result.stdout or "").strip()


def _slug_from_url(url: str) -> str:
    """URL を人間向けの短いラベルに変換する (ログ表示用)。"""
    s = re.sub(r"^https?://", "", url)
    s = re.sub(r"[^\w.-]", "-", s)
    return s[:60]


def cmd_recon(task_id: str) -> None:
    """サブステップ 2-1 取材 — 参考サイトから情報を取得する。

    動作モード:
      - URL あり (1 件以上): 各 URL ごとに site-<i>/ を作って Node recon.mjs で
        スクショ + 6 項目取材 (DOM/CSS/色/フォント/アセット/アニメ) を JSON 化する。
      - URL なし + 要望あり: text-only.json マーカーを書き出して成功扱いで抜ける。
        dump 以降がテキスト要望だけを入力にして本棚ページを作る。
      - URL なし + 要望なし: エラー終了。
    """
    input_path = _input_path(task_id)
    if input_path is None:
        print("エラー: .libs/ が見つかりません。", file=sys.stderr)
        sys.exit(1)

    # 入力ファイル不在 → テンプレ提示
    if not input_path.exists():
        print(f"clone recon: 取材入力ファイルがありません: {input_path}")
        print()
        print("以下のテンプレで input.md を作成してから再実行してください:")
        print()
        print("---- template ----")
        print(_build_input_template(task_id), end="")
        print("------------------")
        sys.exit(2)

    # 入力ファイル読み込み → URL + 要望抽出
    try:
        content = input_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: input.md の読み込みに失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    urls = _extract_reference_urls(content)
    request_body = _extract_section_body(content, RECON_REQUEST_SECTION_SUFFIX)
    note_body = _extract_section_body(content, RECON_NOTE_SECTION_SUFFIX)
    has_request = _has_non_placeholder_body(request_body)

    output_dir = input_path.parent / RECON_OUTPUT_DIR_NAME
    output_dir.mkdir(parents=True, exist_ok=True)

    # --- URL なしモードの分岐 ---
    if not urls:
        if not has_request:
            print(
                f"エラー: {input_path} に参考 URL も要望も記入されていません。",
                file=sys.stderr,
            )
            print(
                f"  `## {task_id}{RECON_REFERENCE_SECTION_SUFFIX}` に URL を書くか、"
                f"`## {task_id}{RECON_REQUEST_SECTION_SUFFIX}` に要望を書いてください。",
                file=sys.stderr,
            )
            sys.exit(1)

        marker = {
            "mode": "text-only",
            "task_id": task_id,
            "request": request_body,
            "note": note_body,
        }
        marker_path = output_dir / RECON_TEXT_ONLY_MARKER_FILENAME
        marker_path.write_text(
            json.dumps(marker, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(
            "clone recon: URL なし + 要望ありモードで完了しました "
            "(テキスト要望だけから dump が本棚ページを作ります)"
        )
        print(f"  入力: {input_path}")
        print(f"  マーカー: {marker_path}")
        return

    # --- URL あり: Node 取材 ---
    print(f"clone recon: {len(urls)} 件の参考サイト URL を取得しました")
    print(f"  入力: {input_path}")
    for i, url in enumerate(urls, 1):
        print(f"  [{i}] {url}")

    # playwright パッケージの存在確認 (recon.mjs が chromium を使うため必須)
    _, pw_code, pw_err = _find_playwright_cli()
    if pw_code != 0:
        print(f"エラー: {pw_err}", file=sys.stderr)
        sys.exit(pw_code)

    node_path, node_err = _find_node_executable()
    if node_path is None:
        print(f"エラー: {node_err}", file=sys.stderr)
        sys.exit(5)

    script_path, script_err = _find_recon_script()
    if script_path is None:
        print(f"エラー: {script_err}", file=sys.stderr)
        sys.exit(6)

    # viewports は (name, (w, h)) の形だけ使う (ファイル名は recon.mjs 側で組み立てる)
    viewports = [(name, vp) for name, vp, _scr, _json in RECON_VIEWPORTS]

    print()
    print(f"clone recon: {len(urls)} URL x {len(viewports)} 解像度を取材します")
    print(f"  Node: {node_path}")
    print(f"  スクリプト: {script_path}")
    print(f"  出力ルート: {output_dir}")

    captured_sites: list[Path] = []
    for i, url in enumerate(urls, 1):
        site_dir = output_dir / f"{RECON_SITE_DIR_PREFIX}{i}"
        site_assets_dir = site_dir / RECON_ASSETS_DIR_NAME
        label = _slug_from_url(url)
        print()
        print(f"  [site-{i}] {label} -> {site_dir}")
        success, msg = _run_node_recon(
            node_path, script_path, url, site_dir, viewports,
            assets_dir=site_assets_dir,
        )
        if not success:
            print(f"エラー (site-{i}): {msg}", file=sys.stderr)
            sys.exit(1)
        # Node の進捗行をインデントして表示
        for line in msg.splitlines():
            print(f"    {line}")

        # サイトごとのメタ JSON を書き残しておく (dump が参照する)
        site_meta = {
            "index": i,
            "url": url,
            "label": label,
            "viewports": [
                {"name": name, "width": w, "height": h}
                for name, (w, h) in viewports
            ],
        }
        (site_dir / "site.json").write_text(
            json.dumps(site_meta, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        captured_sites.append(site_dir)

    print()
    print(f"clone recon: {len(captured_sites)} サイトの取材完了")
    for p in captured_sites:
        print(f"  -> {p}")


# --- dump サブステップのヘルパー群 ---


def _task_slug(task_id: str) -> str:
    return task_id.lower()


def _bookshelf_page_path(task_id: str) -> Path | None:
    """本棚正本ページ (.libs/storybook/<slug>/<slug>.md) のパスを返す。"""
    if LIBS_DIR is None:
        return None
    slug = _task_slug(task_id)
    return LIBS_DIR / STORYBOOK_SHELF_NAME / slug / f"{slug}.md"


_RGB_RE = re.compile(
    r"^rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)(?:\s*,\s*([\d.]+))?\s*\)$"
)
_HEX_RE = re.compile(r"^#[0-9a-fA-F]{3,8}$")


def _rgb_to_hex(color_str: str) -> str | None:
    """'rgb(r,g,b)' / 'rgba(r,g,b,a)' / '#hex' → '#rrggbb' に統一する。

    透明 (alpha < 0.05) や不明な表現は None。
    """
    if not color_str:
        return None
    s = color_str.strip()
    m = _RGB_RE.match(s)
    if m:
        r = min(int(m.group(1)), 255)
        g = min(int(m.group(2)), 255)
        b = min(int(m.group(3)), 255)
        alpha = m.group(4)
        if alpha is not None and float(alpha) < 0.05:
            return None
        return f"#{r:02x}{g:02x}{b:02x}"
    if _HEX_RE.match(s):
        return s.lower()[:7]
    return None


def _clean_font_family(font_family: str) -> str:
    """'Inter, "Helvetica Neue", sans-serif' → 'Inter'."""
    if not font_family:
        return ""
    first = font_family.split(",")[0].strip()
    return first.strip('"').strip("'")


def _load_recon_data(task_dir: Path) -> dict:
    """recon ディレクトリから取材 JSON と text-only マーカーを読み込む。

    Returns:
        {
          "mode": "urls" | "text-only" | None,
          "sites": [ {"path": Path, "meta": dict, "viewports": {name: json}} ],
          "text_only": dict | None,
        }
    """
    recon_dir = task_dir / RECON_OUTPUT_DIR_NAME
    result: dict = {"mode": None, "sites": [], "text_only": None}

    if not recon_dir.exists():
        return result

    marker_path = recon_dir / RECON_TEXT_ONLY_MARKER_FILENAME
    if marker_path.exists():
        try:
            result["text_only"] = json.loads(marker_path.read_text(encoding="utf-8"))
            result["mode"] = "text-only"
            return result
        except (json.JSONDecodeError, OSError):
            pass

    site_dirs = sorted(
        d for d in recon_dir.iterdir()
        if d.is_dir() and d.name.startswith(RECON_SITE_DIR_PREFIX)
    )
    for site_dir in site_dirs:
        site = {"path": site_dir, "viewports": {}, "meta": None}
        site_json = site_dir / "site.json"
        if site_json.exists():
            try:
                site["meta"] = json.loads(site_json.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                pass
        for json_file in sorted(site_dir.glob("recon-*.json")):
            vp_name = json_file.stem.replace("recon-", "")
            try:
                site["viewports"][vp_name] = json.loads(
                    json_file.read_text(encoding="utf-8")
                )
            except (json.JSONDecodeError, OSError):
                pass
        result["sites"].append(site)

    if result["sites"]:
        result["mode"] = "urls"
    return result


def _summarize_css(css_block: dict) -> dict:
    """recon JSON の css ブロックからトークン候補を整形する。"""
    if not isinstance(css_block, dict):
        return {"colors": [], "fonts": [], "sizes": [], "weights": []}

    hex_colors: list[tuple[str, int]] = []
    seen_hex: set[str] = set()
    for item in css_block.get("colors") or []:
        if not isinstance(item, dict):
            continue
        hex_val = _rgb_to_hex(item.get("value", ""))
        if hex_val is None or hex_val in seen_hex:
            continue
        seen_hex.add(hex_val)
        hex_colors.append((hex_val, int(item.get("count") or 0)))

    cleaned_fonts: list[tuple[str, int]] = []
    seen_fonts: set[str] = set()
    for item in css_block.get("fonts") or []:
        if not isinstance(item, dict):
            continue
        name = _clean_font_family(item.get("value", ""))
        if not name or name in seen_fonts:
            continue
        seen_fonts.add(name)
        cleaned_fonts.append((name, int(item.get("count") or 0)))

    sizes = [s for s in (css_block.get("fontSizes") or []) if isinstance(s, str)]
    weights = [str(w) for w in (css_block.get("fontWeights") or [])]

    return {
        "colors": hex_colors,
        "fonts": cleaned_fonts,
        "sizes": sizes,
        "weights": weights,
    }


def _merge_css_summaries(summaries: list[dict]) -> dict:
    """複数 viewport / 複数サイトのサマリを 1 本に統合する (出現数を合算)。"""
    merged_colors: dict[str, int] = {}
    merged_fonts: dict[str, int] = {}
    merged_sizes: dict[str, int] = {}
    merged_weights: set[str] = set()

    for s in summaries:
        for hex_val, count in s["colors"]:
            merged_colors[hex_val] = merged_colors.get(hex_val, 0) + count
        for name, count in s["fonts"]:
            merged_fonts[name] = merged_fonts.get(name, 0) + count
        for size in s["sizes"]:
            merged_sizes[size] = merged_sizes.get(size, 0) + 1
        merged_weights.update(s["weights"])

    return {
        "colors": sorted(merged_colors.items(), key=lambda x: x[1], reverse=True),
        "fonts": sorted(merged_fonts.items(), key=lambda x: x[1], reverse=True),
        "sizes": sorted(merged_sizes.items(), key=lambda x: x[1], reverse=True),
        "weights": sorted(merged_weights),
    }


def _format_site_section(task_id: str, site: dict) -> list[str]:
    """1 サイトぶんの Markdown 断片 (### site-<i>: <URL> ...) を返す。"""
    lines: list[str] = []
    meta = site.get("meta") or {}
    idx = meta.get("index", "?")
    url = meta.get("url", "(URL 不明)")
    lines.append(f"### site-{idx}: {url}")
    lines.append("")

    viewports = site.get("viewports") or {}
    summaries = [_summarize_css((vp.get("css") or {})) for vp in viewports.values()]
    merged = _merge_css_summaries(summaries)

    if merged["colors"]:
        lines.append("- 主要色 (トップ 10):")
        for hex_val, count in merged["colors"][:10]:
            lines.append(f"  - `{hex_val}` (出現 {count})")
    if merged["fonts"]:
        lines.append("- フォント:")
        for name, count in merged["fonts"][:5]:
            lines.append(f"  - `{name}` (出現 {count})")

    total_images = 0
    total_bgs = 0
    for vp in viewports.values():
        assets = vp.get("assets") or {}
        total_images += len(assets.get("images") or [])
        total_bgs += len(assets.get("backgroundImages") or [])
    lines.append(f"- アセット: 画像 {total_images} / 背景画像 {total_bgs}")

    total_anims = 0
    for vp in viewports.values():
        total_anims += len(vp.get("animations") or [])
    lines.append(f"- アニメーション: {total_anims} 個検出")

    # トポロジー (最初の viewport から拾う)
    topo_items: list[str] = []
    for vp in viewports.values():
        topo = vp.get("topology") or {}
        for k in ("header", "nav", "main", "aside", "footer"):
            if topo.get(k):
                topo_items.append(k)
        break
    if topo_items:
        lines.append(f"- トポロジー: {', '.join(topo_items)}")

    lines.append("")
    return lines


def _format_animations_section(task_id: str, sites: list) -> list[str]:
    lines = [f"## {task_id}.アニメーション仕様 — アニメーション仕様", ""]
    found = False
    for site in sites:
        meta = site.get("meta") or {}
        idx = meta.get("index", "?")
        for vp_name, vp in (site.get("viewports") or {}).items():
            anims = vp.get("animations") or []
            if not anims:
                continue
            found = True
            lines.append(f"### site-{idx} / {vp_name} ({len(anims)} 個)")
            for i, anim in enumerate(anims[:10], 1):
                target = anim.get("target") or {}
                tag = target.get("tag") or "?"
                duration = anim.get("duration")
                easing = anim.get("easing")
                lines.append(
                    f"- #{i} `{tag}`: duration={duration}, easing={easing}"
                )
            lines.append("")
    if not found:
        lines.append("(取材なし)")
        lines.append("")
    return lines


def _format_libraries_section(task_id: str, sites: list) -> list[str]:
    """採用ライブラリセクション — recon の detected / scriptsHit / globalsHit をまとめる。

    RSRC-WEBANIM-CAPTURE §技術詳細 1 / RSRC-WEBANIM-REPLAY §使い分けマトリックス。
    後工程 (/codi build) はこのセクションを読んで雛形を分岐する。
    """
    lines = [f"## {task_id}.採用ライブラリ — 採用ライブラリ", ""]
    lines.append(
        "> recon が検出したアニメーション / スクロール / スライダーライブラリ。"
        "build が本セクションを読んで雛形を分岐する (gsap / motion / lenis / r3f / lottie / pure-css)。"
    )
    lines.append(
        "> ユーザー指定がある場合は input.md の `採用ライブラリ` セクションで上書きできる。"
    )
    lines.append("")

    patterns = _load_anim_lib_patterns()
    name_to_label = {p["name"]: p.get("label", p["name"]) for p in patterns.get("patterns", [])}

    aggregated: dict[str, set[int]] = {}
    per_site: list[tuple[int, dict]] = []
    for site in sites:
        meta = site.get("meta") or {}
        idx = meta.get("index")
        if idx is None:
            continue
        merged = {}
        for vp in (site.get("viewports") or {}).values():
            libs = vp.get("libraries") or {}
            for name in (libs.get("detected") or {}):
                merged.setdefault(name, {"scripts": [], "globals": []})
                merged[name]["scripts"].extend((libs.get("scriptsHit") or {}).get(name, []))
                merged[name]["globals"].extend((libs.get("globalsHit") or {}).get(name, []))
                aggregated.setdefault(name, set()).add(idx)
        per_site.append((idx, merged))

    if not aggregated:
        lines.append("(ライブラリ検出なし — pure-CSS 想定で雛形を出す)")
        lines.append("")
        return lines

    lines.append("### 集計 (複数サイト横断)")
    lines.append("")
    priority = list(patterns.get("selectPriority", []))
    sorted_names = sorted(
        aggregated.keys(),
        key=lambda n: priority.index(n) if n in priority else len(priority),
    )
    for name in sorted_names:
        sites_for = sorted(aggregated[name])
        sites_str = ", ".join(f"site-{i}" for i in sites_for)
        label = name_to_label.get(name, name)
        lines.append(f"- **{label}** (`{name}`): {sites_str}")
    lines.append("")

    for idx, merged in per_site:
        if not merged:
            continue
        lines.append(f"### site-{idx} の詳細")
        lines.append("")
        for name, hit in merged.items():
            label = name_to_label.get(name, name)
            scripts = list(dict.fromkeys(hit["scripts"]))[:3]
            globals_ = list(dict.fromkeys(hit["globals"]))[:5]
            lines.append(f"- **{label}** (`{name}`)")
            if globals_:
                lines.append(f"  - globals: `{', '.join(globals_)}`")
            if scripts:
                for s in scripts:
                    lines.append(f"  - script: `{s}`")
        lines.append("")

    return lines


def _format_scroll_mapping_section(task_id: str, sites: list) -> list[str]:
    """スクロール連動マッピングセクション — 代表サンプルの抜粋 + 全量 JSON への参照。

    RSRC-WEBANIM-CAPTURE §技術詳細 6 / RSRC-WEBANIM-REPLAY §2 "Motion" の useTransform LUT に使う。
    """
    lines = [f"## {task_id}.スクロール連動マッピング — スクロール連動マッピング", ""]
    lines.append(
        "> recon が desktop viewport で 120 分割サンプリングして記録した "
        "`transform / opacity / filter` の実測値。build が代表 LUT を "
        "`useTransform` / `ScrollTrigger.scrub` に差し込む根拠になる。"
    )
    lines.append("")

    found = False
    for site in sites:
        meta = site.get("meta") or {}
        idx = meta.get("index", "?")
        for vp_name, vp in (site.get("viewports") or {}).items():
            scroll_data = vp.get("scrollSamples")
            if not scroll_data:
                continue
            samples = scroll_data.get("samples") or []
            target_count = scroll_data.get("targetCount", 0)
            if not samples or target_count == 0:
                continue
            found = True
            lines.append(
                f"### site-{idx} / {vp_name} "
                f"({len(samples)} 段階 × {target_count} ターゲット)"
            )
            lines.append("")
            # 代表 8 段階 (0, 1/7, 2/7, ..., 1/1) だけ抜粋して表示
            n = len(samples)
            indices = [round(k * (n - 1) / 7) for k in range(8)] if n >= 8 else list(range(n))
            # 先頭ターゲット 3 個を横軸に
            max_targets = 3
            header_targets = [
                t["sel"] for t in (samples[0].get("frame") or [])[:max_targets]
            ]
            if header_targets:
                lines.append("| y(px) | " + " | ".join(header_targets) + " |")
                lines.append("|---|" + "---|" * len(header_targets))
                for i in indices:
                    sample = samples[i]
                    y = sample.get("y", "?")
                    cells = []
                    for t in (sample.get("frame") or [])[:max_targets]:
                        transform = (t.get("transform") or "none").replace("|", "/")
                        opacity = t.get("opacity", "?")
                        cells.append(f"t=`{transform[:40]}` op={opacity}")
                    lines.append(f"| {y} | " + " | ".join(cells) + " |")
                lines.append("")
            lines.append(
                f"(全量は `recon/site-{idx}/{SCROLL_SAMPLES_FILENAME}` 参照)"
            )
            lines.append("")

    if not found:
        lines.append("(取材なし — recon 未実行または対象セレクタにマッチする要素がない)")
        lines.append("")
    return lines


def _format_assets_section(task_id: str, sites: list) -> list[str]:
    """アセット取材セクション — Lottie / Rive の自動 DL 一覧。

    RSRC-WEBANIM-HARDCASE §5 "Lottie/Rive 検出"。build は本セクションを見て
    `@lottiefiles/react-lottie-player` or `@rive-app/react-canvas` の雛形を出す。
    """
    lines = [f"## {task_id}.アセット取材 — アセット取材 (Lottie / Rive)", ""]
    lines.append(
        "> recon がネットワーク監視で自動 DL した Lottie JSON / Rive ファイル。"
        "本棚ページからの相対パスで build 工程が埋め込む。"
    )
    lines.append("")

    found = False
    for site in sites:
        meta = site.get("meta") or {}
        idx = meta.get("index", "?")
        site_path: Path | None = site.get("path")
        if site_path is None:
            continue
        manifest_path = site_path / RECON_ASSETS_DIR_NAME / "manifest.json"
        if not manifest_path.exists():
            continue
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        assets = manifest.get("assets") or []
        if not assets:
            continue
        found = True
        lines.append(f"### site-{idx} ({len(assets)} ファイル)")
        lines.append("")
        for asset in assets[:10]:
            kind = asset.get("kind", "?")
            file_name = asset.get("fileName", "?")
            size = asset.get("size", "?")
            rel = f"recon/site-{idx}/{RECON_ASSETS_DIR_NAME}/{file_name}"
            lines.append(
                f"- **{kind}**: `{rel}` ({size} bytes) ← {asset.get('url', '?')}"
            )
        lines.append("")

    if not found:
        lines.append("(Lottie / Rive 検出なし)")
        lines.append("")
    return lines


def _build_bookshelf_page(
    task_id: str, input_meta: dict, recon_data: dict
) -> str:
    """本棚正本ページの Markdown を組み立てる (dump 段階: 元サイト実値のみ)。"""
    lines: list[str] = []
    mode = recon_data.get("mode") or "unknown"
    title = input_meta.get("title") or "<部品名未設定>"

    # ヘッダー
    lines.append(f"# {task_id} — {title}")
    lines.append("")
    lines.append("関連: ")
    lines.append(f"タグ: storybook, layout-dump, {mode}")
    lines.append("")

    # 概要
    lines.append(f"## {task_id}.概要 — 概要")
    lines.append("")
    if mode == "text-only":
        lines.append("モード: テキスト要望のみ (参考サイトなし)")
    elif mode == "urls":
        n = len(recon_data["sites"])
        lines.append(f"モード: URL クローン ({n} サイト取材)")
    else:
        lines.append("モード: 不明 (recon 未実行か取材失敗)")
    lines.append("")
    lines.append("> dump が出力した「元サイトの実値」だけのページ。")
    lines.append("> apply が要望で上書きし、rules がトークン化する。**直接編集禁止**。")
    lines.append("")

    # URL モード固有のセクション
    if mode == "urls":
        sites = recon_data["sites"]

        lines.append(f"## {task_id}.参考サイト一覧 — 参考サイト一覧")
        lines.append("")
        for site in sites:
            lines.extend(_format_site_section(task_id, site))

        # 全サイト統合のトークン候補
        all_summaries: list[dict] = []
        for site in sites:
            for vp in (site.get("viewports") or {}).values():
                all_summaries.append(_summarize_css((vp.get("css") or {})))
        overall = _merge_css_summaries(all_summaries)

        lines.append(f"## {task_id}.色トークン候補 — 色トークン候補")
        lines.append("")
        lines.append(
            "> dump が抽出した元サイトの色。rules で Tailwind v4 `@theme` トークンに変換する。"
        )
        lines.append("")
        if overall["colors"]:
            for i, (hex_val, count) in enumerate(overall["colors"][:20], 1):
                lines.append(
                    f"- `--color-extracted-{i:03d}`: `{hex_val}` (出現 {count})"
                )
        else:
            lines.append("(取材なし)")
        lines.append("")

        lines.append(f"## {task_id}.フォントトークン候補 — フォントトークン候補")
        lines.append("")
        if overall["fonts"]:
            for i, (name, count) in enumerate(overall["fonts"][:10], 1):
                lines.append(
                    f"- `--font-family-extracted-{i:03d}`: `'{name}'` (出現 {count})"
                )
        else:
            lines.append("(取材なし)")
        lines.append("")

        if overall["sizes"]:
            lines.append(f"## {task_id}.フォントサイズ候補 — フォントサイズ候補")
            lines.append("")
            for size, count in overall["sizes"][:30]:
                lines.append(f"- `{size}` (出現 {count})")
            lines.append("")

        lines.extend(_format_libraries_section(task_id, sites))
        lines.extend(_format_animations_section(task_id, sites))
        lines.extend(_format_scroll_mapping_section(task_id, sites))
        lines.extend(_format_assets_section(task_id, sites))

    # text-only モード
    elif mode == "text-only":
        lines.append(f"## {task_id}.参考サイト一覧 — 参考サイト一覧")
        lines.append("")
        lines.append("(参考サイトなし — テキスト要望だけで設計する)")
        lines.append("")
        # 空のトークン候補セクション (rules が要望から値を決めて埋める)
        lines.append(f"## {task_id}.色トークン候補 — 色トークン候補")
        lines.append("")
        lines.append("(要望から rules が決定する)")
        lines.append("")
        lines.append(f"## {task_id}.フォントトークン候補 — フォントトークン候補")
        lines.append("")
        lines.append("(要望から rules が決定する)")
        lines.append("")

    # 要望転載 (apply が同じ箇所を上書き)
    request = input_meta.get("request", "")
    lines.append(f"## {task_id}.要望取り込み — 要望取り込み")
    lines.append("")
    lines.append(
        "> input.md の要望セクションを転載。apply が元サイト実値にこの要望を反映する。"
    )
    lines.append("")
    if request and _has_non_placeholder_body(request):
        lines.append(request)
    else:
        lines.append("(要望なし)")
    lines.append("")

    # メモ
    note = input_meta.get("note", "")
    lines.append(f"## {task_id}.メモ — メモ")
    lines.append("")
    if note and _has_non_placeholder_body(note):
        lines.append(note)
    else:
        lines.append("(メモなし)")
    lines.append("")

    return "\n".join(lines)


def cmd_dump(task_id: str) -> None:
    """サブステップ 2-2 本棚化 — recon 結果を .libs/storybook/ に下書きする。

    入力: .libs/storybook/<slug>/input.md + 同階層の recon/
    出力: .libs/storybook/<slug>/<slug>.md (本棚正本ページ)
    """
    input_path = _input_path(task_id)
    if input_path is None or not input_path.exists():
        print(
            f"エラー: 取材入力 ({input_path}) がありません。先に recon を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        content = input_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: input.md 読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    # 入力メタ情報
    header = parse_header(content)
    title = header["title"] if header else "<部品名未設定>"
    input_meta = {
        "title": title,
        "request": _extract_section_body(content, RECON_REQUEST_SECTION_SUFFIX),
        "note": _extract_section_body(content, RECON_NOTE_SECTION_SUFFIX),
    }

    # recon 結果
    task_dir = input_path.parent
    recon_data = _load_recon_data(task_dir)

    if recon_data["mode"] is None:
        print(
            f"エラー: 取材結果 ({task_dir / RECON_OUTPUT_DIR_NAME}) が見つかりません。"
            "先に recon を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    page_md = _build_bookshelf_page(task_id, input_meta, recon_data)

    page_path = _bookshelf_page_path(task_id)
    if page_path is None:
        print("エラー: 本棚ページのパスを決定できません。", file=sys.stderr)
        sys.exit(1)

    page_path.parent.mkdir(parents=True, exist_ok=True)
    existed = page_path.exists()
    page_path.write_text(page_md + "\n", encoding="utf-8")

    action = "更新" if existed else "作成"
    print(f"clone dump: 本棚ページを{action}しました")
    print(f"  -> {page_path}")
    print(f"  モード: {recon_data['mode']}")
    if recon_data["mode"] == "urls":
        print(f"  サイト数: {len(recon_data['sites'])}")


# --- apply サブステップのヘルパー群 ---


def _replace_or_append_section(
    page_md: str, section_id: str, new_section_md: str
) -> str:
    """本棚ページ内の `## <section_id> — ...` セクションを置換する。

    該当セクションがなければ末尾に追加する。冪等。
    """
    lines = page_md.split("\n")
    start: int | None = None
    end: int | None = None
    header_re = re.compile(rf"^##\s+{re.escape(section_id)}\s+—")
    any_h2_re = re.compile(r"^##\s+\S+")

    for i, line in enumerate(lines):
        if start is None and header_re.match(line):
            start = i
            continue
        if start is not None and i > start and any_h2_re.match(line):
            end = i
            break

    new_lines = new_section_md.split("\n")

    if start is None:
        base = page_md.rstrip("\n")
        return base + "\n\n" + new_section_md + "\n"

    if end is None:
        end = len(lines)

    result = lines[:start] + new_lines + [""] + lines[end:]
    return "\n".join(result)


def _collect_token_candidates_from_page(page_md: str) -> dict:
    """本棚ページから色/フォント/サイズの候補値を抽出する (apply 用)。

    dump が書き込んだ `## ID.色トークン候補` / `## ID.フォントトークン候補` /
    `## ID.フォントサイズ候補` から実値を拾う。各セクションの末尾サフィックスで
    マッチさせるので、task_id に依存しない。
    """
    colors: list[str] = []
    fonts: list[str] = []
    sizes: list[str] = []
    for sec in parse_sections(page_md):
        sec_id = sec["id"]
        body = sec["content"]
        if sec_id.endswith(".色トークン候補"):
            for line in body.split("\n"):
                m = re.search(r"`(#[0-9a-fA-F]{6,8})`", line)
                if m:
                    colors.append(m.group(1).lower())
        elif sec_id.endswith(".フォントトークン候補"):
            for line in body.split("\n"):
                m = re.search(r"`'([^']+)'`", line)
                if m:
                    fonts.append(m.group(1))
        elif sec_id.endswith(".フォントサイズ候補"):
            for line in body.split("\n"):
                m = re.search(r"`([\d.]+(?:px|rem|em|%))`", line)
                if m:
                    sizes.append(m.group(1))
    return {"colors": colors, "fonts": fonts, "sizes": sizes}


def _build_request_import_section(task_id: str, request_body: str) -> str:
    """要望取り込みセクション (input.md 転載) を組み立てる。末尾改行なし。"""
    lines = [
        f"## {task_id}.要望取り込み — 要望取り込み",
        "",
        "> input.md の要望セクションを転載。apply が元サイト実値にこの要望を反映する。",
        "",
    ]
    if request_body and _has_non_placeholder_body(request_body):
        lines.append(request_body)
    else:
        lines.append("(要望なし)")
    return "\n".join(lines)


def _build_apply_section(
    task_id: str, request_body: str, tokens: dict
) -> str:
    """要望反映指示セクション (末尾改行なし) を組み立てる。"""
    lines = [
        f"## {task_id}.要望反映指示 — 要望反映指示",
        "",
        "> apply が生成。build はこの指示を読んで元サイト実値に要望を反映した `.tsx` を作る。",
        "> 「元サイト < 要望」原則 (specs/06-coding-rules.md) に従い、要望が元サイト値より優先される。",
        "",
        "### 要望 (input.md より)",
        "",
    ]
    if request_body and _has_non_placeholder_body(request_body):
        lines.append(request_body)
    else:
        lines.append("(要望なし — 元サイト実値のまま採用する)")
    lines.append("")
    lines.append("### 元サイトの主要値 (参考)")
    lines.append("")
    if tokens["colors"]:
        colors_str = ", ".join(f"`{c}`" for c in tokens["colors"][:10])
        lines.append(f"- 色: {colors_str}")
    else:
        lines.append("- 色: (取材なし — 要望から決定)")
    if tokens["fonts"]:
        fonts_str = ", ".join(f"`{f}`" for f in tokens["fonts"][:5])
        lines.append(f"- フォント: {fonts_str}")
    else:
        lines.append("- フォント: (取材なし — 要望から決定)")
    if tokens["sizes"]:
        sizes_str = ", ".join(f"`{s}`" for s in tokens["sizes"][:10])
        lines.append(f"- サイズ: {sizes_str}")
    else:
        lines.append("- サイズ: (取材なし — 要望から決定)")
    return "\n".join(lines)


def cmd_apply(task_id: str) -> None:
    """サブステップ 2-3 要望適用 — 要望反映指示を本棚ページに追記する。

    apply は「要望 + 元サイト主要値」を 1 セクションにまとめる機械的な工程。
    個別の値 (色「青系」→ 具体 hex) の決定は build 工程で AI が行う。
    冪等: 再実行すると最新の要望で指示セクションが更新される。
    """
    input_path = _input_path(task_id)
    if input_path is None or not input_path.exists():
        print(
            f"エラー: 取材入力 ({input_path}) がありません。", file=sys.stderr
        )
        sys.exit(1)

    try:
        content = input_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: input.md 読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    page_path = _bookshelf_page_path(task_id)
    if page_path is None or not page_path.exists():
        print(
            "エラー: 本棚ページがありません。先に dump を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    request_body = _extract_section_body(content, RECON_REQUEST_SECTION_SUFFIX)

    try:
        page_md = page_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: 本棚ページ読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    tokens = _collect_token_candidates_from_page(page_md)

    # 1. 要望取り込みセクションも最新化 (input.md → 本棚ページを同期)
    request_section = _build_request_import_section(task_id, request_body)
    new_page_md = _replace_or_append_section(
        page_md, f"{task_id}.要望取り込み", request_section
    )

    # 2. 要望反映指示セクションを追記/更新
    apply_section = _build_apply_section(task_id, request_body, tokens)
    new_page_md = _replace_or_append_section(
        new_page_md, f"{task_id}.要望反映指示", apply_section
    )

    if not new_page_md.endswith("\n"):
        new_page_md += "\n"
    page_path.write_text(new_page_md, encoding="utf-8")

    print("clone apply: 要望反映指示を本棚ページに追記しました")
    print(f"  -> {page_path}")
    if request_body and _has_non_placeholder_body(request_body):
        first_line = next(
            (l for l in request_body.split("\n") if l.strip()), ""
        )
        preview = first_line[:60]
        print(
            f"  要望: {preview}{'...' if len(first_line) > 60 else ''}"
        )
    else:
        print("  要望: (なし)")
    print(
        f"  参照した元サイト値: 色 {len(tokens['colors'])} / "
        f"フォント {len(tokens['fonts'])} / サイズ {len(tokens['sizes'])}"
    )


# --- rules サブステップのヘルパー群 ---


def _slug_for_font(name: str, fallback_idx: int) -> str:
    """フォント名 → CSS 変数スラッグ (例: 'Noto Sans JP' → 'noto-sans-jp')。"""
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.lower()).strip("-")
    return slug if slug else f"family-{fallback_idx:02d}"


def _build_rules_section(task_id: str, tokens: dict) -> str:
    """Tailwind v4 @theme トークン定義セクションを組み立てる。末尾改行なし。"""
    lines = [
        f"## {task_id}.トークン定義 — Tailwind v4 @theme トークン定義",
        "",
        "> rules が生成。build はこの `@theme` 定義を `src/app/globals.css` に追記してから `.tsx` を生成する。",
        "> 要望で別の値に差し替える場合もこのトークン名を使う (ハードコ禁止 / specs/06-coding-rules.md)。",
        "",
        "### 色",
        "",
    ]
    if tokens["colors"]:
        lines.append("```css")
        lines.append("@theme {")
        for i, color in enumerate(tokens["colors"][:20], 1):
            lines.append(f"  --color-extracted-{i:03d}: {color};")
        lines.append("}")
        lines.append("```")
        lines.append("")
        lines.append(
            "Tailwind クラス例: `bg-extracted-001`, `text-extracted-002`, "
            "`border-extracted-003`"
        )
    else:
        lines.append("(色の取材なし — 要望から build が決定してトークン化する)")
    lines.append("")

    lines.append("### フォントファミリー")
    lines.append("")
    if tokens["fonts"]:
        lines.append("```css")
        lines.append("@theme {")
        for i, font in enumerate(tokens["fonts"][:10], 1):
            slug = _slug_for_font(font, i)
            lines.append(f'  --font-extracted-{slug}: "{font}", sans-serif;')
        lines.append("}")
        lines.append("```")
        lines.append("")
        lines.append("Tailwind クラス例: `font-extracted-inter`, `font-extracted-noto-sans-jp`")
    else:
        lines.append("(フォントの取材なし — 要望から build が決定してトークン化する)")
    lines.append("")

    lines.append("### フォントサイズ")
    lines.append("")
    if tokens["sizes"]:
        seen: set[str] = set()
        css_lines: list[str] = []
        for size in tokens["sizes"][:20]:
            m = re.match(r"^([\d.]+)(px|rem|em)$", size)
            if not m:
                continue
            num = m.group(1).replace(".", "_")
            unit = m.group(2)
            slug = f"{num}{unit}" if unit != "px" else num
            if slug in seen:
                continue
            seen.add(slug)
            css_lines.append(f"  --text-extracted-{slug}: {size};")
        if css_lines:
            lines.append("```css")
            lines.append("@theme {")
            lines.extend(css_lines)
            lines.append("}")
            lines.append("```")
            lines.append("")
            lines.append("Tailwind クラス例: `text-extracted-16`, `text-extracted-24`")
        else:
            lines.append("(サイズ候補から有効なトークンを組み立てられず — 要望から決定)")
    else:
        lines.append("(サイズの取材なし — 要望から build が決定してトークン化する)")
    lines.append("")

    # iOS 対応 (全タスク共通の固定文言)
    lines.append("### iOS Safari 対応 (必須)")
    lines.append("")
    lines.append("- `viewport-fit=cover` を `layout.tsx` の Metadata viewport に設定")
    lines.append("- `env(safe-area-inset-top/right/bottom/left)` を header / footer / 固定要素に適用")
    lines.append("- タップ領域は最低 44×44 CSS px 確保")
    lines.append("- `-webkit-tap-highlight-color: transparent` + 明示的なフォーカスリングを添える")
    lines.append("")

    # 使用ルール
    lines.append("### 使用ルール (specs/06-coding-rules.md より)")
    lines.append("")
    lines.append("- `className=\"bg-[#xxxxxx]\"` のような任意値ユーティリティは禁止")
    lines.append("- `style={{ color: '#xxx' }}` などの直書き色値も禁止")
    lines.append("- トークン化した値だけを使う (`className=\"bg-extracted-001\"`)")
    lines.append("- 動的な値 (props / state から計算) は `style` 経由で許容")
    return "\n".join(lines)


def cmd_rules(task_id: str) -> None:
    """サブステップ 2-4 ルール適用 — Tailwind v4 トークン定義 + iOS 対応を本棚ページに追記する。

    冪等: 再実行で本棚ページ内の色/フォント/サイズ候補を再読込してトークンを再生成する。
    """
    page_path = _bookshelf_page_path(task_id)
    if page_path is None or not page_path.exists():
        print(
            "エラー: 本棚ページがありません。先に dump → apply を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        page_md = page_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: 本棚ページ読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    tokens = _collect_token_candidates_from_page(page_md)
    rules_section = _build_rules_section(task_id, tokens)

    new_page_md = _replace_or_append_section(
        page_md, f"{task_id}.トークン定義", rules_section
    )
    if not new_page_md.endswith("\n"):
        new_page_md += "\n"
    page_path.write_text(new_page_md, encoding="utf-8")

    print("clone rules: Tailwind v4 トークン定義を本棚ページに追記しました")
    print(f"  -> {page_path}")
    print(
        f"  トークン化: 色 {len(tokens['colors'])} / "
        f"フォント {len(tokens['fonts'])} / サイズ {len(tokens['sizes'])}"
    )


# --- build サブステップのヘルパー群 ---


def _task_id_to_pascal(task_id: str) -> str:
    """APPLY-TEST-01 → ApplyTest01 (コンポーネント名)。"""
    return "".join(p.capitalize() for p in task_id.split("-"))


def _build_tsx_skeleton(task_id: str) -> str:
    """.tsx 雛形 (コードフェンス付き) — pure-CSS / 既定フォールバック。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.tsx\n"
        "'use client';\n"
        "\n"
        "type PASCALProps = {\n"
        "  /** 追加 prop をここに */\n"
        "};\n"
        "\n"
        "export function PASCAL(_props: PASCALProps) {\n"
        "  return (\n"
        "    <section\n"
        "      className=\"bg-extracted-001 text-extracted-002 font-extracted-inter\"\n"
        "      style={{\n"
        "        paddingTop: 'env(safe-area-inset-top)',\n"
        "        paddingBottom: 'env(safe-area-inset-bottom)',\n"
        "      }}\n"
        "    >\n"
        "      {/* 「要望反映指示」と元サイトのトポロジー/主要色を反映 */}\n"
        "    </section>\n"
        "  );\n"
        "}\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


def _build_tsx_skeleton_motion(task_id: str) -> str:
    """Motion for React (旧 Framer Motion) 雛形 — RSRC-WEBANIM-REPLAY §2。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.tsx\n"
        "'use client';\n"
        "\n"
        "import { motion, useScroll, useTransform } from 'motion/react';\n"
        "import { useRef } from 'react';\n"
        "\n"
        "export function PASCAL() {\n"
        "  const ref = useRef<HTMLDivElement>(null);\n"
        "  const { scrollYProgress } = useScroll({\n"
        "    target: ref,\n"
        "    offset: ['start end', 'end start'],\n"
        "  });\n"
        "  // スクロール連動マッピングセクションの LUT を [0..1] → 値へ差し込む\n"
        "  const y = useTransform(scrollYProgress, [0, 0.5, 1], [0, -80, -160]);\n"
        "  const opacity = useTransform(scrollYProgress, [0, 0.1, 0.9, 1], [0, 1, 1, 0]);\n"
        "\n"
        "  return (\n"
        "    <motion.section\n"
        "      ref={ref}\n"
        "      style={{ y, opacity }}\n"
        "      className=\"bg-extracted-001 text-extracted-002\"\n"
        "    >\n"
        "      {/* 要望反映 */}\n"
        "    </motion.section>\n"
        "  );\n"
        "}\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


def _build_tsx_skeleton_gsap(task_id: str) -> str:
    """GSAP + ScrollTrigger + useGSAP 雛形 — RSRC-WEBANIM-REPLAY §2。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.tsx\n"
        "'use client';\n"
        "\n"
        "import { useRef } from 'react';\n"
        "import { gsap } from 'gsap';\n"
        "import { ScrollTrigger } from 'gsap/ScrollTrigger';\n"
        "import { useGSAP } from '@gsap/react';\n"
        "\n"
        "gsap.registerPlugin(useGSAP, ScrollTrigger);\n"
        "\n"
        "export function PASCAL() {\n"
        "  const root = useRef<HTMLDivElement>(null);\n"
        "  useGSAP(\n"
        "    () => {\n"
        "      gsap.to('.PASCAL-layer', {\n"
        "        yPercent: -50,\n"
        "        ease: 'none',\n"
        "        scrollTrigger: {\n"
        "          trigger: root.current,\n"
        "          start: 'top top',\n"
        "          end: '+=1200',\n"
        "          scrub: 0.5,\n"
        "          pin: true,\n"
        "          anticipatePin: 1,\n"
        "        },\n"
        "      });\n"
        "    },\n"
        "    { scope: root, revertOnUpdate: true },\n"
        "  );\n"
        "\n"
        "  return (\n"
        "    <section ref={root} className=\"bg-extracted-001 text-extracted-002\">\n"
        "      <div className=\"PASCAL-layer\">{/* 要望反映 */}</div>\n"
        "    </section>\n"
        "  );\n"
        "}\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


def _build_tsx_skeleton_lenis(task_id: str) -> str:
    """Lenis ReactLenis + useLenis 雛形 — RSRC-WEBANIM-REPLAY §2。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.tsx\n"
        "'use client';\n"
        "\n"
        "// Lenis は root provider 化が前提。`src/app/providers.tsx` に以下を追加する:\n"
        "//   'use client';\n"
        "//   import { ReactLenis } from 'lenis/react';\n"
        "//   export function Providers({ children }: { children: React.ReactNode }) {\n"
        "//     return <ReactLenis root>{children}</ReactLenis>;\n"
        "//   }\n"
        "// 既存の GSAP と併用する場合は `lenis.on('scroll', ScrollTrigger.update)` + `gsap.ticker.add(t => lenis.raf(t*1000))` で同期する。\n"
        "\n"
        "import { useLenis } from 'lenis/react';\n"
        "\n"
        "export function PASCAL() {\n"
        "  useLenis(() => {\n"
        "    // スクロール進捗を監視したいときに使う (任意)\n"
        "  });\n"
        "\n"
        "  return (\n"
        "    <section className=\"bg-extracted-001 text-extracted-002\">\n"
        "      {/* 要望反映 */}\n"
        "    </section>\n"
        "  );\n"
        "}\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


def _build_tsx_skeleton_r3f(task_id: str) -> str:
    """React Three Fiber 雛形 — RSRC-WEBANIM-REPLAY §6。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.tsx\n"
        "'use client';\n"
        "\n"
        "import { Canvas, useFrame } from '@react-three/fiber';\n"
        "import { useRef } from 'react';\n"
        "import type { Mesh } from 'three';\n"
        "\n"
        "function PASCALScene() {\n"
        "  const mesh = useRef<Mesh>(null);\n"
        "  useFrame(({ clock }) => {\n"
        "    if (mesh.current) mesh.current.rotation.y = clock.elapsedTime * 0.3;\n"
        "  });\n"
        "  return (\n"
        "    <mesh ref={mesh}>\n"
        "      <planeGeometry args={[2, 2]} />\n"
        "      <meshBasicMaterial color=\"#ffffff\" />\n"
        "    </mesh>\n"
        "  );\n"
        "}\n"
        "\n"
        "export function PASCAL() {\n"
        "  return (\n"
        "    <section className=\"relative h-[100vh] bg-extracted-001\">\n"
        "      <Canvas className=\"absolute inset-0\" dpr={[1, 2]}>\n"
        "        <ambientLight intensity={0.8} />\n"
        "        <PASCALScene />\n"
        "      </Canvas>\n"
        "      {/* 要望反映 (DOM 側) */}\n"
        "    </section>\n"
        "  );\n"
        "}\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


def _build_tsx_skeleton_lottie(task_id: str) -> str:
    """Lottie (@lottiefiles/react-lottie-player) 雛形 — RSRC-WEBANIM-HARDCASE §5。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.tsx\n"
        "'use client';\n"
        "\n"
        "// recon が DL した JSON を `public/lottie/<slug>/` に置き、下の src パスを合わせる。\n"
        "// 本棚ページの「アセット取材」セクションで recon 出力パスを確認すること。\n"
        "\n"
        "import { Player } from '@lottiefiles/react-lottie-player';\n"
        "\n"
        "export function PASCAL() {\n"
        "  return (\n"
        "    <section className=\"bg-extracted-001\">\n"
        "      <Player\n"
        "        autoplay\n"
        "        loop\n"
        "        src=\"/lottie/SLUG/animation.json\"\n"
        "        style={{ height: 400 }}\n"
        "      />\n"
        "    </section>\n"
        "  );\n"
        "}\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


# ライブラリ名 → 雛形関数 のマップ (selectPriority と同じキー体系)
_TSX_SKELETON_BY_LIB = {
    "gsap": _build_tsx_skeleton_gsap,
    "scroll-trigger": _build_tsx_skeleton_gsap,  # ScrollTrigger 単体なら GSAP 雛形
    "motion": _build_tsx_skeleton_motion,
    "lenis": _build_tsx_skeleton_lenis,
    "locomotive": _build_tsx_skeleton_lenis,     # Locomotive 代替として Lenis
    "three": _build_tsx_skeleton_r3f,
    "lottie": _build_tsx_skeleton_lottie,
    "rive": _build_tsx_skeleton_lottie,          # Rive は lottie と同じ位置付け (別ライブラリ推奨)
    "pure-css": _build_tsx_skeleton,
}


def _detect_adopted_library(task_id: str, page_md: str) -> tuple[str, str]:
    """採用ライブラリを決定する (ユーザー指定 > recon 検出 > pure-css)。

    Returns: (library_name, reason)
    """
    # 1. input.md のユーザー指定を確認
    input_path = _input_path(task_id)
    if input_path is not None and input_path.exists():
        try:
            input_content = input_path.read_text(encoding="utf-8")
            for sec in parse_sections(input_content):
                if not sec["id"].endswith(".採用ライブラリ"):
                    continue
                # 案内文 (HTML コメント / 箇条書きの括弧プレースホルダ) を除外し、
                # ユーザーが明示的に書いた指定だけを判定対象にする
                filtered: list[str] = []
                for line in sec["content"].split("\n"):
                    stripped = line.strip()
                    if not stripped or stripped.startswith("<!--"):
                        continue
                    if stripped.startswith(("-", "*")):
                        content = stripped[1:].strip()
                    else:
                        content = stripped
                    if content.startswith(("(", "<!--")):
                        continue
                    filtered.append(content)
                body = " ".join(filtered).lower()
                for key in _TSX_SKELETON_BY_LIB:
                    if re.search(rf"\b{re.escape(key)}\b", body):
                        return key, f"input.md のユーザー指定 (`{key}`)"
                if "r3f" in body or "three" in body:
                    return "three", "input.md のユーザー指定 (three/r3f)"
        except (OSError, UnicodeDecodeError):
            pass

    # 2. 本棚ページの「採用ライブラリ」セクションから detect 結果を読む
    detected_names: list[str] = []
    for sec in parse_sections(page_md):
        if not sec["id"].endswith(".採用ライブラリ"):
            continue
        for line in sec["content"].split("\n"):
            m = re.search(r"\(`([\w-]+)`\)", line)
            if m:
                detected_names.append(m.group(1))

    if detected_names:
        priority = _load_anim_lib_patterns().get("selectPriority", [])
        for name in priority:
            if name in detected_names:
                return name, f"recon 検出から優先度選択 (`{name}`)"
        # 優先度リストにない場合は最初の検出を使う
        return detected_names[0], f"recon 検出 (`{detected_names[0]}`)"

    return "pure-css", "検出なし — pure-CSS フォールバック"


def _build_stories_skeleton(task_id: str) -> str:
    """.stories.tsx 雛形 (コードフェンス付き)。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// src/components/SLUG/PASCAL.stories.tsx\n"
        "import type { Meta, StoryObj } from '@storybook/react';\n"
        "import { PASCAL } from './PASCAL';\n"
        "\n"
        "const meta: Meta<typeof PASCAL> = {\n"
        "  title: 'Layout/PASCAL',\n"
        "  component: PASCAL,\n"
        "  parameters: { layout: 'fullscreen' },\n"
        "};\n"
        "export default meta;\n"
        "\n"
        "type Story = StoryObj<typeof PASCAL>;\n"
        "\n"
        "export const Default: Story = {};\n"
        "\n"
        "export const Mobile: Story = {\n"
        "  parameters: {\n"
        "    viewport: { defaultViewport: 'iphone14' },\n"
        "  },\n"
        "};\n"
    )
    return "```tsx\n" + code.replace("SLUG", slug).replace("PASCAL", pascal) + "```"


def _build_vrt_spec_skeleton(task_id: str) -> str:
    """VRT テストファイル雛形 (コードフェンス付き)。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    code = (
        "// tests/vrt/SLUG.spec.ts\n"
        "import { test, expect } from '@playwright/test';\n"
        "\n"
        "const STORYBOOK_URL = 'http://localhost:6006';\n"
        "\n"
        "test('PASCAL — default', async ({ page }) => {\n"
        "  await page.goto(\n"
        "    `${STORYBOOK_URL}/iframe.html?id=layout-SLUG_LOWER--default&viewMode=story`,\n"
        "  );\n"
        "  await page.waitForLoadState('networkidle');\n"
        "  await expect(page).toHaveScreenshot('SLUG-default.png', {\n"
        "    fullPage: true,\n"
        "    threshold: 0,\n"
        "    maxDiffPixels: 0,\n"
        "    animations: 'disabled',\n"
        "  });\n"
        "});\n"
        "\n"
        "test('PASCAL — mobile', async ({ page }) => {\n"
        "  await page.goto(\n"
        "    `${STORYBOOK_URL}/iframe.html?id=layout-SLUG_LOWER--mobile&viewMode=story`,\n"
        "  );\n"
        "  await page.waitForLoadState('networkidle');\n"
        "  await expect(page).toHaveScreenshot('SLUG-mobile.png', {\n"
        "    fullPage: true,\n"
        "    threshold: 0,\n"
        "    maxDiffPixels: 0,\n"
        "    animations: 'disabled',\n"
        "  });\n"
        "});\n"
    )
    return (
        "```ts\n"
        + code.replace("SLUG_LOWER", pascal.lower())
        .replace("SLUG", slug)
        .replace("PASCAL", pascal)
        + "```"
    )


def _build_build_section(task_id: str, page_md: str) -> str:
    """ビルド指示セクション (末尾改行なし)。

    本棚ページの `採用ライブラリ` セクションと input.md のユーザー指定から
    採用ライブラリを決定し、対応する .tsx 雛形を出し分ける。
    pure-css が選ばれた場合のみ、従来の framer-motion variants 前提の実装手順を維持する。
    """
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    target_dir = f"src/components/{slug}"
    adopted, reason = _detect_adopted_library(task_id, page_md)
    skeleton_fn = _TSX_SKELETON_BY_LIB.get(adopted, _build_tsx_skeleton)

    # ライブラリ別の実装手順ヒント
    lib_hints = {
        "motion": (
            "7. アニメは Motion for React (`motion/react`) の `useScroll` + `useTransform` を使う",
            "8. LUT は本棚ページの「スクロール連動マッピング」セクションから代表値を移植する",
        ),
        "gsap": (
            "7. アニメは `@gsap/react` の `useGSAP` + ScrollTrigger を使う (scope 指定必須)",
            "8. scrub / pin / anticipatePin を本棚ページの「スクロール連動マッピング」に合わせる",
        ),
        "lenis": (
            "7. Lenis は `app/providers.tsx` で `<ReactLenis root>` として配置する",
            "8. GSAP 併用時は `lenis.on('scroll', ScrollTrigger.update)` で同期する",
        ),
        "three": (
            "7. R3F Canvas は必ず Client Component。`ssr: false` の `dynamic` で包むのが安全",
            "8. uniforms / shaderMaterial を使う場合は本棚ページの「WebGL 取材」(段階 2) を参照",
        ),
        "lottie": (
            "7. DL 済 JSON/riv は `public/lottie/{slug}/` に置く (本棚ページ「アセット取材」参照)",
            "8. サイズ / 速度の調整は Player props で行う (autoplay / loop / speed)",
        ),
        "pure-css": (
            "7. アニメは `prefers-reduced-motion` で停止できるよう CSS `@keyframes` + `@media` で実装",
        ),
    }
    tail_steps = lib_hints.get(adopted, lib_hints["pure-css"])

    lines = [
        f"## {task_id}.ビルド指示 — build 工程指示",
        "",
        "> build が生成。AI はこのセクション + 「要望反映指示」+ 「トークン定義」の 3 つを読んで",
        "> 下記の `.tsx` / `.stories.tsx` / VRT テストを生成する。",
        "",
        "### 採用ライブラリ",
        "",
        f"- 選択: **`{adopted}`**",
        f"- 判定根拠: {reason}",
        "- RSRC-WEBANIM-REPLAY §使い分けマトリックス に準拠",
        "",
        "### 生成先",
        "",
        f"- コンポーネント: `{target_dir}/{pascal}.tsx`",
        f"- Storybook ストーリー: `{target_dir}/{pascal}.stories.tsx`",
        f"- VRT テスト: `tests/vrt/{slug}.spec.ts`",
        f"- コンポーネント名: `{pascal}`",
        f"- Storybook タイトル: `Layout/{pascal}`",
        "",
        "### 実装手順",
        "",
        "1. `src/app/globals.css` の `@theme` ブロックに「トークン定義」セクションの CSS を追記",
        "2. 下の `.tsx` 雛形をベースに、要望反映指示と元サイトのトポロジー/主要色を反映",
        "3. 任意値 `bg-[#...]` は禁止。すべて `extracted-*` トークンクラスを使う",
        "4. iOS 対応ルール (safe-area-inset / 44px タップ領域) を遵守",
        "5. `.stories.tsx` で Default + Mobile の 2 story を作成 (VRT 基準に必要)",
        "6. `tests/vrt/` に VRT テストファイルを作成 (baseline 工程で基準スクショを自動撮影)",
    ]
    lines.extend(tail_steps)
    lines.extend([
        "",
        "### .tsx 雛形",
        "",
        skeleton_fn(task_id),
        "",
        "### .stories.tsx 雛形",
        "",
        _build_stories_skeleton(task_id),
        "",
        "### VRT テスト雛形",
        "",
        _build_vrt_spec_skeleton(task_id),
    ])
    return "\n".join(lines)


def cmd_build(task_id: str) -> None:
    """サブステップ 2-5 部品実装 — 本棚ページにビルド指示書 (生成先 + 雛形) を追記する。

    AI (エル子) は本棚ページのこのセクションを読んで `.tsx` / `.stories.tsx` を書き出す。
    スクリプトは工程制御と雛形生成に徹する (specs/08-responsibility.md 責務分離)。
    """
    page_path = _bookshelf_page_path(task_id)
    if page_path is None or not page_path.exists():
        print(
            "エラー: 本棚ページがありません。先に dump → apply → rules を実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        page_md = page_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: 本棚ページ読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    build_section = _build_build_section(task_id, page_md)
    new_page_md = _replace_or_append_section(
        page_md, f"{task_id}.ビルド指示", build_section
    )
    if not new_page_md.endswith("\n"):
        new_page_md += "\n"
    page_path.write_text(new_page_md, encoding="utf-8")

    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    adopted, _reason = _detect_adopted_library(task_id, page_md)
    print("clone build: ビルド指示を本棚ページに追記しました")
    print(f"  -> {page_path}")
    print(f"  コンポーネント名: {pascal}")
    print(f"  採用ライブラリ: {adopted}")
    print(f"  生成先 (推奨): src/components/{slug}/{pascal}.tsx")


# --- assemble サブステップ ---


def _build_assemble_section(task_id: str) -> str:
    """ページ統合指示セクション (末尾改行なし)。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    lines = [
        f"## {task_id}.ページ統合指示 — assemble 工程指示",
        "",
        "> assemble が生成。AI は build で作った部品を `page.tsx` に組み込み、SEO 設定を行う。",
        "",
        "### 組み込み先",
        "",
        f"- 推奨配置: `src/app/(marketing)/{slug}/page.tsx` または `src/app/page.tsx`",
        f"- import: `import {{ {pascal} }} from '@/components/{slug}/{pascal}';`",
        f"- 使用: `<{pascal} />` を JSX に配置",
        "",
        "### Metadata API (Next.js 16)",
        "",
        "```tsx",
        "import type { Metadata } from 'next';",
        "",
        "export const metadata: Metadata = {",
        "  title: '<ページタイトル>',",
        "  description: '<説明 120-160 文字>',",
        "  openGraph: {",
        "    title: '<OG タイトル>',",
        "    description: '<OG 説明>',",
        "    images: ['/og.png'],",
        "  },",
        "  twitter: {",
        "    card: 'summary_large_image',",
        "  },",
        "};",
        "",
        "export const viewport = {",
        "  viewportFit: 'cover',",
        "  themeColor: '#ffffff',",
        "};",
        "```",
        "",
        "### 構造化データ (JSON-LD)",
        "",
        "ページ種別 (Article / Product / Organization 等) に応じた JSON-LD を",
        "`<script type=\"application/ld+json\">` で埋め込む。schema.org を参照。",
        "",
        "### チェック項目",
        "",
        "- `<html lang>` が設定されているか (`src/app/layout.tsx`)",
        "- `<Metadata>` の title / description が埋まっているか",
        "- OG 画像パスが公開ディレクトリに存在するか",
        "- ページ内の H1 がちょうど 1 つか",
    ]
    return "\n".join(lines)


def cmd_assemble(task_id: str) -> None:
    """サブステップ 2-6 ページ統合 — page.tsx 組み込み + SEO 指示を追記する。"""
    page_path = _bookshelf_page_path(task_id)
    if page_path is None or not page_path.exists():
        print(
            "エラー: 本棚ページがありません。先に build まで実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        page_md = page_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: 本棚ページ読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    section = _build_assemble_section(task_id)
    new_page_md = _replace_or_append_section(
        page_md, f"{task_id}.ページ統合指示", section
    )
    if not new_page_md.endswith("\n"):
        new_page_md += "\n"
    page_path.write_text(new_page_md, encoding="utf-8")

    print("clone assemble: ページ統合指示を本棚ページに追記しました")
    print(f"  -> {page_path}")


# --- baseline サブステップ ---


def _build_baseline_section(task_id: str) -> str:
    """VRT 基準スクショ指示セクション (末尾改行なし)。"""
    pascal = _task_id_to_pascal(task_id)
    slug = _task_slug(task_id)
    lines = [
        f"## {task_id}.基準スクショ指示 — baseline 工程指示",
        "",
        "> baseline が自動実行。Storybook を起動 → 各ビューポートでスクショ撮影 → 停止する。",
        "",
        "### 自動撮影の出力先",
        "",
        f"- `.libs/storybook/{slug}/{BASELINE_OUTPUT_DIR_NAME}/baseline-desktop.png`",
        f"- `.libs/storybook/{slug}/{BASELINE_OUTPUT_DIR_NAME}/baseline-mobile.png`",
        "",
        "### VRT 回帰テスト (変更検出)",
        "",
        "基準スクショ撮影後、VRT テストで変更検出ができる:",
        "",
        "```bash",
        "# Storybook を起動してからテスト実行",
        "npx playwright test --project=vrt",
        "npx playwright test --project=vrt-mobile",
        "```",
        "",
        f"テストファイル: `tests/vrt/{slug}.spec.ts` (build 工程で生成済み)",
        "",
        "### 撮影ビューポート",
        "",
    ]
    for name, (w, h), _scr, _json in RECON_VIEWPORTS:
        lines.append(f"- `{name}` {w}×{h}")
    lines.extend([
        "",
        "### 撮影条件",
        "",
        "- `reducedMotion: 'reduce'` (アニメ停止)",
        "- `fullPage: true` (ページ全体)",
        "- `networkidle` 待機後 1.5 秒の安定化待ち",
    ])
    return "\n".join(lines)


def _find_baseline_script() -> tuple[Path | None, str]:
    """core/clone_node/baseline.mjs の実パスを返す。"""
    script = NXT_ROOT / "core" / RECON_NODE_DIR_NAME / BASELINE_NODE_SCRIPT_FILENAME
    if not script.exists():
        return None, f"baseline スクリプトが見つかりません: {script}"
    return script, ""


def _find_diff_script() -> tuple[Path | None, str]:
    """core/clone_node/diff.mjs の実パスを返す。"""
    script = NXT_ROOT / "core" / RECON_NODE_DIR_NAME / DIFF_NODE_SCRIPT_FILENAME
    if not script.exists():
        return None, f"diff スクリプトが見つかりません: {script}"
    return script, ""


def _run_node_diff(
    node_path: str,
    script: Path,
    baseline_png: Path,
    reference_png: Path,
    output_png: Path,
    threshold: float,
) -> tuple[bool, dict | str]:
    """diff.mjs を呼んで元サイトと再現の差分を計測する。

    Returns:
        (True, {"mismatchRatio": float, "diffImage": str, ...}) on success
        (False, error_message) on failure
    """
    output_png.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        node_path, str(script),
        "--baseline", str(baseline_png),
        "--reference", str(reference_png),
        "--output", str(output_png),
        "--threshold", str(threshold),
    ]
    cwd = PROJECT_ROOT if PROJECT_ROOT is not None else None
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=DIFF_NODE_TIMEOUT_SEC,
            cwd=str(cwd) if cwd else None,
            encoding="utf-8",
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return False, f"タイムアウト ({DIFF_NODE_TIMEOUT_SEC} 秒)"
    except OSError as exc:
        return False, f"実行エラー: {exc}"

    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        return False, f"diff.mjs 失敗 (exit={result.returncode}): {stderr}"

    # diff.mjs は最終行で JSON を吐く契約
    stdout = (result.stdout or "").strip()
    json_line = ""
    for line in reversed(stdout.splitlines()):
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            json_line = line
            break
    if not json_line:
        return False, f"diff.mjs の JSON 出力が見つかりません: {stdout}"
    try:
        return True, json.loads(json_line)
    except json.JSONDecodeError as exc:
        return False, f"diff.mjs の JSON パース失敗: {exc}"


def _compare_recon_vs_baseline(task_id: str, page_path: Path) -> None:
    """元サイトの recon スクショと再現の baseline スクショを pixelmatch で比較する。

    結果を `.libs/storybook/<slug>/diff/diff-result.json` と `diff-<viewport>.png` に保存する。
    段階 1 では「レポートのみ」。閾値超過時の自動修正ループは段階 5。
    """
    task_dir = page_path.parent
    recon_dir = task_dir / RECON_OUTPUT_DIR_NAME
    baseline_dir = task_dir / BASELINE_OUTPUT_DIR_NAME
    diff_dir = task_dir / DIFF_OUTPUT_DIR_NAME
    if not recon_dir.exists():
        print("clone baseline: recon/ がないため差分検証をスキップします")
        return
    if not baseline_dir.exists():
        print("clone baseline: baseline/ がないため差分検証をスキップします")
        return

    node_path, node_err = _find_node_executable()
    if node_path is None:
        print(f"警告 (差分検証スキップ): {node_err}", file=sys.stderr)
        return
    diff_script, script_err = _find_diff_script()
    if diff_script is None:
        print(f"警告 (差分検証スキップ): {script_err}", file=sys.stderr)
        return

    # site-1 を代表取材として比較する (複数サイト統合は段階 5 で扱う)
    first_site = recon_dir / f"{RECON_SITE_DIR_PREFIX}1"
    if not first_site.exists():
        print("clone baseline: recon/site-1 が見つかりません。差分検証をスキップ")
        return

    results = []
    for name, _vp, screenshot_filename, _json in RECON_VIEWPORTS:
        reference_png = first_site / screenshot_filename
        baseline_png = baseline_dir / f"baseline-{name}.png"
        if not reference_png.exists() or not baseline_png.exists():
            continue
        output_png = diff_dir / f"{DIFF_IMAGE_PREFIX}{name}.png"
        ok, payload = _run_node_diff(
            node_path, diff_script,
            baseline_png, reference_png, output_png,
            DIFF_PIXELMATCH_THRESHOLD,
        )
        if not ok:
            print(f"警告 (差分検証 {name}): {payload}", file=sys.stderr)
            continue
        ratio = float(payload.get("mismatchRatio", 0.0))
        verdict = "OK" if ratio <= DIFF_MAX_MISMATCH_RATIO else "要改善"
        print(
            f"  [diff {name}] 差分率 {ratio * 100:.2f}% ({verdict}) -> {output_png}"
        )
        results.append({
            "viewport": name,
            "baseline": str(baseline_png.relative_to(task_dir)).replace("\\", "/"),
            "reference": str(reference_png.relative_to(task_dir)).replace("\\", "/"),
            "diff": str(output_png.relative_to(task_dir)).replace("\\", "/"),
            "mismatchRatio": ratio,
            "verdict": verdict,
            **{k: v for k, v in payload.items() if k != "mismatchRatio"},
        })

    if not results:
        return

    diff_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "task_id": task_id,
        "threshold": DIFF_PIXELMATCH_THRESHOLD,
        "maxMismatchRatio": DIFF_MAX_MISMATCH_RATIO,
        "results": results,
    }
    (diff_dir / DIFF_RESULT_FILENAME).write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _run_node_baseline(
    node_path: str,
    script: Path,
    story_id: str,
    output_dir: Path,
    viewports: list[tuple[str, tuple[int, int]]],
    port: int,
) -> tuple[bool, str]:
    """baseline.mjs を起動して Storybook ストーリーの基準スクショを取得する。

    Returns: (success, message)
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    cmd = [node_path, str(script), story_id, str(output_dir)]
    for name, (w, h) in viewports:
        cmd.extend(["--viewport", f"{name}:{w}x{h}"])
    cmd.extend(["--port", str(port)])

    cwd = PROJECT_ROOT if PROJECT_ROOT is not None else None

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=BASELINE_NODE_TIMEOUT_SEC,
            cwd=str(cwd) if cwd else None,
            encoding="utf-8",
            errors="replace",
        )
    except subprocess.TimeoutExpired:
        return False, f"タイムアウト ({BASELINE_NODE_TIMEOUT_SEC} 秒)"
    except OSError as exc:
        return False, f"実行エラー: {exc}"

    if result.returncode != 0:
        stderr = (result.stderr or "").strip()
        stdout = (result.stdout or "").strip()
        return False, (
            f"baseline.mjs が失敗しました (exit={result.returncode})\n"
            f"  stderr: {stderr}\n"
            f"  stdout: {stdout}"
        )

    return True, (result.stdout or "").strip()


def cmd_baseline(task_id: str) -> None:
    """サブステップ 2-7 VRT 基準作成 — Storybook の基準スクショを自動撮影する。"""
    page_path = _bookshelf_page_path(task_id)
    if page_path is None or not page_path.exists():
        print(
            "エラー: 本棚ページがありません。先に assemble まで実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        page_md = page_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: 本棚ページ読み込み失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    # 本棚ページに指示セクションを追記 (参照用)
    section = _build_baseline_section(task_id)
    new_page_md = _replace_or_append_section(
        page_md, f"{task_id}.基準スクショ指示", section
    )
    if not new_page_md.endswith("\n"):
        new_page_md += "\n"
    page_path.write_text(new_page_md, encoding="utf-8")

    # --- 実際にスクショを撮影 ---

    # Playwright チェック
    _, pw_code, pw_err = _find_playwright_cli()
    if pw_code != 0:
        print(f"エラー: {pw_err}", file=sys.stderr)
        sys.exit(pw_code)

    # Node チェック
    node_path, node_err = _find_node_executable()
    if node_path is None:
        print(f"エラー: {node_err}", file=sys.stderr)
        sys.exit(1)

    # baseline.mjs チェック
    baseline_script, script_err = _find_baseline_script()
    if baseline_script is None:
        print(f"エラー: {script_err}", file=sys.stderr)
        sys.exit(1)

    # Story ID を計算 (Storybook の title: 'Layout/PascalCase' → ID: 'layout-pascalcase--default')
    pascal = _task_id_to_pascal(task_id)
    story_id = f"layout-{pascal.lower()}--default"

    output_dir = page_path.parent / BASELINE_OUTPUT_DIR_NAME

    # ビューポートリスト (recon と同じ形式に変換)
    viewports = [(name, vp) for name, vp, _scr, _json in RECON_VIEWPORTS]

    print(f"clone baseline: VRT 基準スクショを撮影します")
    print(f"  ストーリー: Layout/{pascal} (id={story_id})")
    print(f"  出力先: {output_dir}")

    ok, msg = _run_node_baseline(
        node_path, baseline_script, story_id, output_dir,
        viewports, BASELINE_STORYBOOK_PORT,
    )

    if not ok:
        print(f"エラー: 基準スクショの撮影に失敗しました\n{msg}", file=sys.stderr)
        sys.exit(1)

    # 結果を表示
    print()
    print(msg)
    print()
    print("clone baseline: 基準スクショの撮影完了")
    print(f"  本棚ページ: {page_path}")
    print(f"  スクショ: {output_dir}")

    # --- 段階 1: 元サイト vs 再現の差分検証 (pixelmatch) ---
    # RSRC-WEBANIM-HARDCASE §7 "VRT 差分自動修正ループ" のレポート部分のみ実装。
    # 自動修正は段階 5 (別セッション)。ここでは数値と画像を保存するだけ。
    print()
    print("clone baseline: 元サイト vs 再現の差分を計測します (レポートのみ)")
    _compare_recon_vs_baseline(task_id, page_path)


# --- ディスパッチ ---
# LAYOUT_SUBSTEPS を単一の出どころにして辞書を生成する。
# cmd_<name> 関数が欠けていれば import 時に KeyError で落ちる (欠落検知)。

SUBCOMMANDS = {name: globals()[f"cmd_{name}"] for name in LAYOUT_SUBSTEPS}


# --- main ---


def _usage() -> None:
    subs = ", ".join(LAYOUT_SUBSTEPS)
    print("usage: python core/clone.py <subcommand> <task_id>", file=sys.stderr)
    print(f"  subcommand: {subs}", file=sys.stderr)


def main() -> None:
    if len(sys.argv) < 3:
        _usage()
        sys.exit(1)

    subcommand = sys.argv[1].lower()
    task_id = sys.argv[2].upper()

    handler = SUBCOMMANDS.get(subcommand)
    if handler is None:
        print(f"エラー: 不明なサブコマンド '{subcommand}'", file=sys.stderr)
        _usage()
        sys.exit(1)

    handler(task_id)


if __name__ == "__main__":
    main()
