"""install.py - プロジェクトセットアップスクリプト

新規インストールとアップデートを兼用する。
プロジェクトルートから実行する。

使い方:
    python .nxt-core/core/install.py            # 新規
    python .nxt-core/core/install.py --update   # 更新
"""

import io
import json
import shutil
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import NXT_ROOT, IS_SOURCE, STACK_NEXTJS_SKILLS_DIR, TEMPLATES_DIR
from constants import (
    LIBS_SHELVES,
    DEFAULT_GITIGNORE_LINES,
    QA_CONFIG_TEMPLATES,
    CLAUDE_DIR_NAME,
    CLAUDE_MD_FILENAME,
    GITIGNORE_FILENAME,
    LIBS_DIR_NAME,
    OS_SKILLS_FILENAME,
    OS_SPECS_FILES,
    OS_SECTION_HEADING,
    PERMISSION_DEFAULTS_ALLOW,
    PERMISSION_DEFAULTS_MODE,
    SCRIPTS_DIR_NAME,
    SETTINGS_FILENAME,
    SKILL_FRONTMATTER_TARGET_KEY,
    SKILL_FRONTMATTER_VARIANT_KEY,
    SKILL_MD_FILENAME,
    SKILLS_DIR_NAME,
    STATE_DIR_NAME,
    UI_SPECS_DIR_NAME,
    VARIANT_BOTH,
    VARIANT_DEFAULT,
    VARIANT_FILE_NAME,
    VARIANT_GENERIC,
    VARIANT_JSON_KEY,
    VARIANT_NEXTJS,
)
from feedback import init_error_handling
from variant import read_variant, write_variant

init_error_handling()

# --- モジュール内派生定数 ---

STANDARD_DIRS = [
    *[f"{LIBS_DIR_NAME}/{s}" for s in LIBS_SHELVES],
    f"{CLAUDE_DIR_NAME}/{STATE_DIR_NAME}",
    SCRIPTS_DIR_NAME,
    UI_SPECS_DIR_NAME,
    "e2e",
    "tests/vrt",
]


# --- ユーティリティ ---


def _nxt_relpath(project_root: Path) -> str:
    """NXT_ROOT のプロジェクトルート相対パス (posix 形式)。"""
    return NXT_ROOT.relative_to(project_root).as_posix()


def _claude_md_content(project_name: str, nxt_path: str) -> str:
    imports = "\n".join(f"@{nxt_path}/specs/{name}" for name in OS_SPECS_FILES)
    return (
        f"# {project_name}\n"
        f"\n"
        f"## erqo-next OS\n"
        f"{imports}\n"
        f"\n"
        f"## プロジェクトルール\n"
    )


def _hook_config(nxt_path: str) -> dict:
    return {
        "SessionStart": [
            {
                "matcher": "startup|resume",
                "hooks": [{
                    "type": "command",
                    "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/session.py"',
                    "timeout": 10,
                    "statusMessage": "プロジェクト情報を読み込み中...",
                }],
            },
            {
                "matcher": "compact",
                "hooks": [{
                    "type": "command",
                    "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/session.py" --compact',
                    "timeout": 10,
                    "statusMessage": "コンテキストを復元中...",
                }],
            },
        ],
        "PreToolUse": [
            {
                "matcher": "Write|Edit|NotebookEdit",
                "hooks": [
                    {
                        "type": "command",
                        "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/write_guard.py"',
                        "timeout": 5,
                    },
                    {
                        "type": "command",
                        "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/coding_rules_hook.py"',
                        "timeout": 5,
                    },
                ],
            },
            {
                "matcher": "mcp__.*",
                "hooks": [
                    {
                        "type": "command",
                        "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/project_servers_hook.py"',
                        "timeout": 5,
                    },
                ],
            },
        ],
    }


def _claude_dir(project_root: Path) -> Path:
    return project_root / CLAUDE_DIR_NAME


def _state_dir(project_root: Path) -> Path:
    return _claude_dir(project_root) / STATE_DIR_NAME


def _project_skills_dir(project_root: Path) -> Path:
    return _claude_dir(project_root) / SKILLS_DIR_NAME


def _settings_path(project_root: Path) -> Path:
    return _claude_dir(project_root) / SETTINGS_FILENAME


def _os_skills_manifest_path(project_root: Path) -> Path:
    return _state_dir(project_root) / OS_SKILLS_FILENAME


# --- セットアップ関数 ---


def sync_os_imports_in_claude_md(existing: str, nxt_path: str) -> str | None:
    """既存 CLAUDE.md の `## erqo-next OS` ブロックを OS_SPECS_FILES から再生成する。

    見出し `OS_SECTION_HEADING` から次の `## ` 見出し (または EOF) までを、
    最新の @import 一覧で置き換える。見出しが見つからなければ None を返す。
    `## プロジェクトルール` など以降のユーザー編集は保持される。

    `nxt_path` はプロジェクトルート相対の `.nxt-core` (プル子側) または
    空文字 (本元側で `@specs/XX.md` 直指定) のどちらも受け付ける。
    本元側同期には `dev.py:sync_source_claude_md` から再利用される。
    """
    lines = existing.splitlines()
    heading_idx: int | None = None
    for i, line in enumerate(lines):
        if line.strip() == OS_SECTION_HEADING:
            heading_idx = i
            break
    if heading_idx is None:
        return None

    end_idx = len(lines)
    for j in range(heading_idx + 1, len(lines)):
        if lines[j].startswith("## "):
            end_idx = j
            break

    prefix = f"{nxt_path}/" if nxt_path else ""
    new_imports = [f"@{prefix}specs/{name}" for name in OS_SPECS_FILES]
    new_block = [lines[heading_idx], *new_imports, ""]
    new_lines = lines[:heading_idx] + new_block + lines[end_idx:]
    result = "\n".join(new_lines)
    if existing.endswith("\n") and not result.endswith("\n"):
        result += "\n"
    return result


def setup_claude_md(project_root: Path) -> bool:
    """CLAUDE.md を作成または同期する。

    - 新規ファイル: `_claude_md_content()` から全生成
    - 既存ファイル: `## erqo-next OS` ブロックだけを `OS_SPECS_FILES` と同期し、
      `## プロジェクトルール` 以降のユーザー手動編集は保持する
    - `## erqo-next OS` 見出しが無い既存ファイルはスキップ (ユーザー自由記述を尊重)
    """
    claude_md = project_root / CLAUDE_MD_FILENAME
    nxt_path = _nxt_relpath(project_root)

    if not claude_md.exists():
        content = _claude_md_content(project_root.name, nxt_path)
        claude_md.write_text(content, encoding="utf-8")
        print(f"  {CLAUDE_MD_FILENAME}: 作成")
        return True

    try:
        existing = claude_md.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        print(f"  {CLAUDE_MD_FILENAME}: 既存 (読み込み失敗でスキップ)")
        return False

    updated = sync_os_imports_in_claude_md(existing, nxt_path)
    if updated is None:
        print(f"  {CLAUDE_MD_FILENAME}: 既存 ({OS_SECTION_HEADING} 見出しなしでスキップ)")
        return False
    if updated == existing:
        print(f"  {CLAUDE_MD_FILENAME}: 既存 (同期済み)")
        return False
    claude_md.write_text(updated, encoding="utf-8")
    print(f"  {CLAUDE_MD_FILENAME}: {OS_SECTION_HEADING} ブロックを最新化")
    return True


def setup_hooks(project_root: Path) -> bool:
    """settings.json に Hook を設定する。既存の Hook はマージ。

    _hook_config() が返す全 hook_type (SessionStart / PreToolUse 等) を
    走査し、matcher が未登録のエントリだけを追加する。プロジェクト固有や
    手動で書かれた Hook は触らずに保持する。
    """
    nxt_path = _nxt_relpath(project_root)
    hook_config = _hook_config(nxt_path)

    settings_path = _settings_path(project_root)
    settings_path.parent.mkdir(parents=True, exist_ok=True)

    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            settings = {}
    else:
        settings = {}

    hooks = settings.setdefault("hooks", {})

    added_total = 0
    for hook_type, hook_entries in hook_config.items():
        existing_entries = hooks.setdefault(hook_type, [])
        existing_by_matcher = {entry.get("matcher", ""): entry for entry in existing_entries}
        for hook_entry in hook_entries:
            matcher = hook_entry["matcher"]
            new_hooks = hook_entry.get("hooks", [])
            if matcher not in existing_by_matcher:
                # 新規 matcher: エントリごと追加
                existing_entries.append(hook_entry)
                added_total += len(new_hooks)
            else:
                # 既存 matcher: hooks 配列内のコマンドをコマンド単位でマージ
                existing_entry = existing_by_matcher[matcher]
                existing_hook_list = existing_entry.setdefault("hooks", [])
                existing_commands = {h.get("command", "") for h in existing_hook_list}
                for new_hook in new_hooks:
                    if new_hook.get("command", "") not in existing_commands:
                        existing_hook_list.append(new_hook)
                        added_total += 1

    settings_path.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    label = f"{added_total} 個追加" if added_total else "設定済み (変更なし)"
    print(f"  {SETTINGS_FILENAME}: Hook {label}")
    return added_total > 0


def _prompt_variant() -> str:
    """対話で variant を選ばせる。1/2 の入力を VARIANT_NEXTJS/VARIANT_GENERIC に変換。

    非対話環境 (EOFError) では VARIANT_DEFAULT (プル子) に倒す。
    """
    print("このプロジェクトの種類を選んでください:")
    print("  1) Next.js プロジェクト (プル子 — 標準、/layo 付き)")
    print("  2) その他のスタック (プタ子 — 最小構成、/layo なし)")
    while True:
        try:
            answer = input("番号を入力 (1/2): ").strip()
        except EOFError:
            print(f"  (非対話モード: {VARIANT_DEFAULT} として登録)")
            return VARIANT_DEFAULT
        if answer == "1":
            return VARIANT_NEXTJS
        if answer == "2":
            return VARIANT_GENERIC
        print("  エラー: 1 か 2 を入力してください。")


def setup_variant(project_root: Path, update_mode: bool) -> bool:
    """variant.json を作成または migrate する。

    - 既に印がある: 触らない (冪等)
    - 新規インストール (update_mode=False) + 印なし: 対話で選ばせる
    - アップデート (update_mode=True) + 印なし: VARIANT_DEFAULT を書く
      (既存プル子の後方互換マイグレーション)
    """
    variant_file = _state_dir(project_root) / VARIANT_FILE_NAME
    if variant_file.exists():
        try:
            current = json.loads(variant_file.read_text(encoding="utf-8")).get(
                VARIANT_JSON_KEY, "?"
            )
            print(f"  {VARIANT_FILE_NAME}: 既存 ({current})")
        except (json.JSONDecodeError, OSError, UnicodeDecodeError):
            print(f"  {VARIANT_FILE_NAME}: 既存 (読み込み失敗でスキップ)")
        return False

    if update_mode:
        value = VARIANT_DEFAULT
        print(
            f"  {VARIANT_FILE_NAME}: 印なし → {VARIANT_DEFAULT} として登録"
            " (既存プル子の後方互換マイグレーション)"
        )
    else:
        value = _prompt_variant()

    write_variant(value)
    print(f"  {VARIANT_FILE_NAME}: {value} として保存")
    return True


def setup_permission_defaults(project_root: Path) -> bool:
    """settings.json に共通 permission 設定をマージする。

    本元・プロジェクト両方で同じ設定を使うため、constants.PERMISSION_DEFAULTS_*
    を読み込んで .claude/settings.json に書き込む。既存の allow リストには
    重複なくマージし、defaultMode と skipDangerousModePermissionPrompt は
    上書きする。
    """
    settings_path = _settings_path(project_root)
    settings_path.parent.mkdir(parents=True, exist_ok=True)

    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            settings = {}
    else:
        settings = {}

    permissions = settings.setdefault("permissions", {})
    existing_allow = list(permissions.get("allow", []))
    merged_allow = list(existing_allow)
    for entry in PERMISSION_DEFAULTS_ALLOW:
        if entry not in merged_allow:
            merged_allow.append(entry)

    changed = (
        merged_allow != existing_allow
        or permissions.get("defaultMode") != PERMISSION_DEFAULTS_MODE
        or settings.get("skipDangerousModePermissionPrompt") is not True
    )

    permissions["allow"] = merged_allow
    permissions["defaultMode"] = PERMISSION_DEFAULTS_MODE
    settings["skipDangerousModePermissionPrompt"] = True

    settings_path.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  {SETTINGS_FILENAME}: 共通 permission 設定 {'更新' if changed else '設定済み (変更なし)'}")
    return changed


def _read_skill_frontmatter_field(skill_md_path: Path, field: str, default: str) -> str:
    """SKILL.md の YAML frontmatter から指定フィールドを読む。

    frontmatter が欠落・不正の場合や、該当 field が無い場合は default を返す。
    """
    try:
        content = skill_md_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return default
    if not content.startswith("---"):
        return default
    end = content.find("\n---", 3)
    if end < 0:
        return default
    front = content[3:end]
    prefix = f"{field}:"
    for line in front.splitlines():
        stripped = line.strip()
        if stripped.startswith(prefix):
            return stripped.split(":", 1)[1].strip()
    return default


def _read_skill_target(skill_md_path: Path) -> str:
    """SKILL.md の `target:` を読む。欠落時は "both" (本元・プル子両対応)。"""
    return _read_skill_frontmatter_field(skill_md_path, SKILL_FRONTMATTER_TARGET_KEY, "both")


def _read_skill_variant(skill_md_path: Path) -> str:
    """SKILL.md の `variant:` を読む。欠落時は VARIANT_BOTH (プル子・プタ子両対応)。"""
    return _read_skill_frontmatter_field(skill_md_path, SKILL_FRONTMATTER_VARIANT_KEY, VARIANT_BOTH)


# variant → stacks/<variant>/skills/ のマッピング
# 段階 3 で VARIANT_GENERIC: STACK_GENERIC_SKILLS_DIR を追加する想定。
_STACK_SKILLS_DIRS: dict[str, Path] = {
    VARIANT_NEXTJS: STACK_NEXTJS_SKILLS_DIR,
}


def _scan_skills() -> list[tuple[str, Path]]:
    """共通 + variant 固有の skills/ 配下をスキャンし、(name, src_root) のリストを返す。

    走査対象:
    - 共通: NXT_ROOT / skills/ (本元・プロジェクト共通)
    - variant 固有: stacks/<variant>/skills/ (プロジェクトの印に該当するもののみ)

    target フィルタ: 本元 (IS_SOURCE) では `target: project` を除外。
    variant フィルタ: プロジェクト側では SKILL.md の `variant:` と照合 (本元では無効)。
    同名衝突: 共通側が先勝ち (scan_targets の並び順)。
    """
    variant_filter = None if IS_SOURCE else read_variant()

    scan_targets: list[Path] = [NXT_ROOT / SKILLS_DIR_NAME]
    if variant_filter in _STACK_SKILLS_DIRS:
        scan_targets.append(_STACK_SKILLS_DIRS[variant_filter])

    result: list[tuple[str, Path]] = []
    seen: set[str] = set()
    for src_root in scan_targets:
        if not src_root.exists():
            continue
        for d in sorted(src_root.iterdir()):
            if not d.is_dir():
                continue
            if d.name in seen:
                continue
            skill_md = d / SKILL_MD_FILENAME
            if not skill_md.exists():
                continue
            target = _read_skill_target(skill_md)
            if IS_SOURCE and target == "project":
                continue
            if variant_filter is not None:
                skill_variant = _read_skill_variant(skill_md)
                if skill_variant != VARIANT_BOTH and skill_variant != variant_filter:
                    continue
            result.append((d.name, src_root))
            seen.add(d.name)
    return result


def _rewrite_skill_paths(dst_dir: Path, nxt_path: str) -> None:
    """コピー先の SKILL.md 内の {nxt} プレースホルダを実パスに置換する。

    本体リポジトリ（nxt_path == "."）の場合は "{nxt}/" ごと除去する。
    プロジェクトの場合は "{nxt}" を相対パスに置換する。
    """
    skill_md = dst_dir / SKILL_MD_FILENAME
    if not skill_md.exists():
        return
    content = skill_md.read_text(encoding="utf-8")
    if nxt_path == ".":
        rewritten = content.replace("{nxt}/", "")
    else:
        rewritten = content.replace("{nxt}", nxt_path)
    if rewritten != content:
        skill_md.write_text(rewritten, encoding="utf-8")


def setup_skills(project_root: Path, update_mode: bool) -> int:
    """スキルを .claude/skills/ にコピーする。

    新規: 全スキルをコピー。
    更新: 前回 _os_skills.json に記録されていたスキルのみ管理する。
          - 現在も存在するスキル → 上書きコピー
          - 削除されたスキル → .claude/skills/ から削除（stale 除去）
          - 新規追加されたスキル → コピー（自動取り込み）
          固有スキル（マニフェスト外）は保持される。

    コピー元は variant に応じて共通 skills/ と stacks/<variant>/skills/ の両方から
    `_scan_skills()` が (name, src_root) 形式で返したリストに従う。
    """
    nxt_path = _nxt_relpath(project_root)
    dst_dir = _project_skills_dir(project_root)
    dst_dir.mkdir(parents=True, exist_ok=True)

    os_skills = _scan_skills()
    if not os_skills:
        print("  スキル: ソースなし (スキップ)")
        return 0

    current_names = {name for name, _ in os_skills}

    # 更新モード: 前回のマニフェストと突き合わせて stale 削除を行う
    removed = 0
    if update_mode:
        manifest_path = _os_skills_manifest_path(project_root)
        previous_managed: set[str] = set()
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                previous_managed = set(manifest.get("skills", []))
            except (json.JSONDecodeError, OSError):
                previous_managed = set()

        # stale: 前回管理していたが現在のスキル一覧に存在しないもの
        stale = previous_managed - current_names
        for skill_name in sorted(stale):
            stale_path = dst_dir / skill_name
            if stale_path.exists():
                shutil.rmtree(stale_path)
                removed += 1

    count = 0
    for skill_name, src_root in os_skills:
        src_skill = src_root / skill_name
        dst_skill = dst_dir / skill_name
        if dst_skill.exists():
            shutil.rmtree(dst_skill)
        shutil.copytree(src_skill, dst_skill)
        _rewrite_skill_paths(dst_skill, nxt_path)
        count += 1

    if removed:
        print(f"  スキル: {count} 個コピー / {removed} 個削除")
    else:
        print(f"  スキル: {count} 個コピー")
    return count


def setup_os_skills_manifest(project_root: Path) -> None:
    """_os_skills.json を生成する。OS 提供スキルの一覧を記録。"""
    os_skills = [name for name, _ in _scan_skills()]
    manifest = {"version": "1.0.0", "skills": os_skills}

    manifest_path = _os_skills_manifest_path(project_root)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  {OS_SKILLS_FILENAME}: {len(os_skills)} 個のスキルを記録")


def setup_directories(project_root: Path) -> list[str]:
    """必要なディレクトリを作成する。"""
    created = []
    for d in STANDARD_DIRS:
        path = project_root / d
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(d)

    if created:
        print(f"  ディレクトリ: {len(created)} 個作成")
    else:
        print("  ディレクトリ: すべて存在 (変更なし)")
    return created


def setup_gitignore(project_root: Path) -> bool:
    """.gitignore を生成する。既存の場合は不足分を追記。"""
    gitignore = project_root / GITIGNORE_FILENAME

    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        existing = {line.strip() for line in content.splitlines()}
        missing = [line for line in DEFAULT_GITIGNORE_LINES if line not in existing]
        if not missing:
            print(f"  {GITIGNORE_FILENAME}: 設定済み (変更なし)")
            return False
        if not content.endswith("\n"):
            content += "\n"
        content += "\n".join(missing) + "\n"
        gitignore.write_text(content, encoding="utf-8")
        print(f"  {GITIGNORE_FILENAME}: {len(missing)} 行追加")
    else:
        gitignore.write_text("\n".join(DEFAULT_GITIGNORE_LINES) + "\n", encoding="utf-8")
        print(f"  {GITIGNORE_FILENAME}: 作成")

    return True


def setup_qa_configs(project_root: Path) -> int:
    """品質チェック設定ファイルをテンプレートから生成する。既存は上書きしない。"""
    if not TEMPLATES_DIR.exists():
        print("  品質チェック設定: テンプレートなし (スキップ)")
        return 0

    created = 0
    skipped = []
    for filename in QA_CONFIG_TEMPLATES:
        src = TEMPLATES_DIR / filename
        dst = project_root / filename
        if not src.exists():
            continue
        if dst.exists():
            skipped.append(filename)
            continue
        shutil.copy2(src, dst)
        created += 1

    if created:
        print(f"  品質チェック設定: {created} ファイル生成")
    if skipped:
        print(f"  品質チェック設定: {len(skipped)} ファイル既存 (スキップ)")
    if not created and not skipped:
        print("  品質チェック設定: テンプレートなし (スキップ)")
    return created


def verify_installation(project_root: Path) -> bool:
    """インストール検証。必須ファイル・ディレクトリの存在チェック。"""
    print("\n検証:")
    all_ok = True

    # ファイルチェック
    for f in [CLAUDE_MD_FILENAME, GITIGNORE_FILENAME]:
        ok = (project_root / f).exists()
        print(f"  {'OK' if ok else 'NG'} {f}")
        all_ok = all_ok and ok

    # settings.json + Hook 群
    settings_path = _settings_path(project_root)
    settings_hooks: dict = {}
    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
            settings_hooks = settings.get("hooks", {}) or {}
        except (json.JSONDecodeError, OSError):
            settings_hooks = {}
    has_session_hook = "SessionStart" in settings_hooks
    has_pretool_hook = "PreToolUse" in settings_hooks
    print(f"  {'OK' if has_session_hook else 'NG'} {SETTINGS_FILENAME} (SessionStart Hook)")
    print(f"  {'OK' if has_pretool_hook else 'NG'} {SETTINGS_FILENAME} (PreToolUse Hook)")
    all_ok = all_ok and has_session_hook and has_pretool_hook

    # スキル
    skills_dir = _project_skills_dir(project_root)
    has_skills = skills_dir.exists() and any(skills_dir.iterdir()) if skills_dir.exists() else False
    label = "OK" if has_skills else "--"
    print(f"  {label} {CLAUDE_DIR_NAME}/{SKILLS_DIR_NAME}/ (スキル)")

    # .libs/ 標準棚
    for shelf in LIBS_SHELVES:
        ok = (project_root / LIBS_DIR_NAME / shelf).exists()
        print(f"  {'OK' if ok else 'NG'} {LIBS_DIR_NAME}/{shelf}/")
        all_ok = all_ok and ok

    return all_ok


# --- メイン ---


def main() -> None:
    if IS_SOURCE:
        print("エラー: このスクリプトはプロジェクト内でのみ実行できます。", file=sys.stderr)
        sys.exit(1)

    update_mode = "--update" in sys.argv
    project_root = NXT_ROOT.parent

    mode = "アップデート" if update_mode else "インストール"
    print(f"erqo-next {mode}: {project_root.name}")
    print()

    # 1. CLAUDE.md (新規のみ)
    if not update_mode:
        setup_claude_md(project_root)

    # 2. Hook 設定
    setup_hooks(project_root)

    # 2.5. 共通 permission 設定
    setup_permission_defaults(project_root)

    # 2.7. variant (プル子 / プタ子) 選択 / マイグレーション
    #      スキルコピー前に書き込む (setup_skills 内の variant フィルタが印を読むため)
    setup_variant(project_root, update_mode)

    # 3. スキルコピー
    setup_skills(project_root, update_mode)

    # 4. _os_skills.json
    setup_os_skills_manifest(project_root)

    # 5. ディレクトリ作成
    setup_directories(project_root)

    # 6. .gitignore
    if not update_mode:
        setup_gitignore(project_root)

    # 7. 品質チェック設定 (新規のみ)
    if not update_mode:
        setup_qa_configs(project_root)

    # 8. 検証
    all_ok = verify_installation(project_root)

    print(f"\n{mode}{'完了' if all_ok else '完了 (一部 NG あり)'}")
    if not update_mode and all_ok:
        print("新しいセッションを開始して /dsgn で設計フェーズを始めてください。")


if __name__ == "__main__":
    main()
