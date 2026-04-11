"""clone.py - レイアウトサブパイプライン 7 サブステップの実行スクリプト

/codi ステップ 2 (implementation) がレイアウトタスクの場合に呼び出される
サブステップエントリポイント。本元リポジトリでは /codi 自体が使えないため、
clone.py 単体での起動にも対応する (IS_SOURCE ガードなし)。

使い方:
    python core/clone.py <subcommand> <task_id>

サブコマンド (= constants.LAYOUT_SUBSTEPS):
    recon     取材 (Playwright CLI で参考サイトから取得)
    dump      本棚化 (.libs/storybook/ に下書き)
    apply     要望適用 (元サイト < 要望)
    rules     ルール適用 (ハードコ禁止 / iOS / Tailwind v4)
    build     部品実装 (.tsx + .stories.tsx 生成)
    assemble  ページ統合 (page.tsx + SEO)
    baseline  VRT 基準作成 (pixel-perfect 基準スクショ)

詳細: .libs/research/webclone/rsrc-webclone-codi-integration.md
"""

import io
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

from paths import LIBS_DIR, PROJECT_ROOT
from constants import (
    LAYOUT_SUBSTEPS,
    STORYBOOK_SHELF_NAME,
    STORYBOOK_INPUT_FILENAME,
    RECON_REFERENCE_SECTION_SUFFIX,
    RECON_OUTPUT_DIR_NAME,
    RECON_VIEWPORTS,
    RECON_PLAYWRIGHT_TIMEOUT_SEC,
)
from page_parser import parse_sections
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


def _find_playwright_cli() -> tuple[str | None, int, str]:
    """プロジェクトローカルの playwright CLI (node_modules/.bin/playwright) を探す。

    npx 経由の検査は npx が on-demand でパッケージを取得してしまうため当てにできない。
    PROJECT_ROOT/node_modules/.bin/ を直接見るのが最も確実。

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
            "  npm install -D @playwright/test\n"
            "  npx playwright install chromium"
        )

    return playwright_path, 0, ""


def _run_playwright_screenshot(
    playwright_path: str,
    url: str,
    output: Path,
    viewport: tuple[int, int],
) -> tuple[bool, str]:
    """Playwright CLI でフルページスクショを取得する。

    Returns: (success, message)
    """
    output.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        playwright_path, "screenshot",
        f"--viewport-size={viewport[0]},{viewport[1]}",
        "--full-page",
        url,
        str(output),
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=RECON_PLAYWRIGHT_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        return False, f"タイムアウト ({RECON_PLAYWRIGHT_TIMEOUT_SEC} 秒)"
    except OSError as exc:
        return False, f"実行エラー: {exc}"

    if result.returncode != 0:
        stderr = result.stderr.strip()
        return False, (
            f"playwright screenshot が失敗しました (exit={result.returncode})\n"
            f"  stderr: {stderr}"
        )

    return True, str(output)


def cmd_recon(task_id: str) -> None:
    """サブステップ 2-1 取材 — 参考サイトから情報を取得する。

    現状 (recon A): 入力ファイル (.libs/storybook/<task>/input.md) を検出し、
    参考サイト URL を抽出するところまで。実際の Playwright 起動は recon B 以降。
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

    # 入力ファイル読み込み → URL 抽出
    try:
        content = input_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exc:
        print(f"エラー: input.md の読み込みに失敗: {exc}", file=sys.stderr)
        sys.exit(1)

    urls = _extract_reference_urls(content)
    if not urls:
        print(
            f"エラー: {input_path} に参考サイト URL が見つかりません。",
            file=sys.stderr,
        )
        print(
            f"  `## {task_id}{RECON_REFERENCE_SECTION_SUFFIX} — 参考サイト` セクションに "
            "`- https://...` 形式で URL を書いてください。",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"clone recon: {len(urls)} 件の参考サイト URL を取得しました")
    print(f"  入力: {input_path}")
    for i, url in enumerate(urls, 1):
        print(f"  [{i}] {url}")

    # --- recon B/C: 最初の URL から RECON_VIEWPORTS の各解像度でスクショ取得 ---
    playwright_path, err_code, err_msg = _find_playwright_cli()
    if playwright_path is None:
        print(f"エラー: {err_msg}", file=sys.stderr)
        sys.exit(err_code)

    target_url = urls[0]
    output_dir = input_path.parent / RECON_OUTPUT_DIR_NAME

    print()
    print(f"clone recon: {len(RECON_VIEWPORTS)} 解像度のスクショを取得します")
    print(f"  URL: {target_url}")
    print(f"  出力ディレクトリ: {output_dir}")

    captured: list[str] = []
    for name, viewport, filename in RECON_VIEWPORTS:
        output = output_dir / filename
        print()
        print(f"  [{name}] viewport={viewport[0]}x{viewport[1]} -> {output.name}")
        success, msg = _run_playwright_screenshot(
            playwright_path, target_url, output, viewport
        )
        if not success:
            print(f"エラー ({name}): {msg}", file=sys.stderr)
            sys.exit(1)
        captured.append(msg)

    print()
    print(f"clone recon: {len(captured)} 枚のスクショ取得完了")
    for path in captured:
        print(f"  -> {path}")
    print()
    print("次フェーズ (recon D: DOM/CSS/色/フォント/アセット の page.evaluate 取材) は未実装。")
    print("  方針 (Node / playwright-python / 取材の妥協) は recon D 着手時に再検討する。")


def cmd_dump(task_id: str) -> None:
    """サブステップ 2-2 本棚化 — .libs/storybook/ に下書き。"""
    _stub("dump", task_id)


def cmd_apply(task_id: str) -> None:
    """サブステップ 2-3 要望適用 — 元サイト < 要望。"""
    _stub("apply", task_id)


def cmd_rules(task_id: str) -> None:
    """サブステップ 2-4 ルール適用 — ハードコ禁止 / iOS / Tailwind v4。"""
    _stub("rules", task_id)


def cmd_build(task_id: str) -> None:
    """サブステップ 2-5 部品実装 — .tsx + .stories.tsx 生成。"""
    _stub("build", task_id)


def cmd_assemble(task_id: str) -> None:
    """サブステップ 2-6 ページ統合 — page.tsx + SEO。"""
    _stub("assemble", task_id)


def cmd_baseline(task_id: str) -> None:
    """サブステップ 2-7 VRT 基準作成 — pixel-perfect 基準スクショ。"""
    _stub("baseline", task_id)


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
