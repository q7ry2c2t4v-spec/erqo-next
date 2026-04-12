"""dev.py - 本体リポジトリ向け開発セットアップ

本体リポジトリ（IS_SOURCE）で /wrap, /ret などのスキルを使えるようにする。
プロジェクト用の install.py とは責務を分け、本体専用の最小セットアップだけを行う。

行うこと:
- skills/ → .claude/skills/ コピー（{nxt}/ プレースホルダ除去込み）
- _os_skills.json マニフェスト記録
- settings.json に SessionStart Hook を設定

行わないこと（プロジェクト用 install.py の処理）:
- CLAUDE.md 作成（手書きのものを尊重）
- .libs/ ディレクトリ作成（specs/ が知識源）
- .gitignore 整備（手書きのものを尊重）
- QA 設定生成（Python のみのリポジトリ）

使い方:
    python core/dev.py setup    # 初回: スキル + Hook 設定
    python core/dev.py update   # スキル再コピー（Hook 設定済みの想定）
    python core/dev.py _sync    # PostToolUse Hook 用（stdin から JSON を受け取る）
"""

import io
import json
import os
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import IS_SOURCE, NXT_ROOT, PROJECT_ROOT
from constants import CLAUDE_MD_FILENAME, SKILLS_DIR_NAME
from install import (
    setup_hooks,
    setup_skills,
    setup_os_skills_manifest,
    setup_permission_defaults,
    sync_os_imports_in_claude_md,
)
from feedback import init_error_handling

init_error_handling()


def _require_source() -> None:
    """本体リポジトリ以外で実行されたらエラー終了する。"""
    if not IS_SOURCE or PROJECT_ROOT is None:
        print("エラー: dev.py は本体リポジトリでのみ実行できます。", file=sys.stderr)
        print("プロジェクトでは install.py を使ってください。", file=sys.stderr)
        sys.exit(1)


def sync_source_claude_md() -> bool:
    """本元 CLAUDE.md の `## erqo-next OS` ブロックを OS_SPECS_FILES と同期する。

    install.py の `sync_os_imports_in_claude_md` を再利用する。`nxt_path=""`
    を渡すことで本元リポジトリルート相対の `@specs/XX.md` 形式で書き出す。
    見出しが無ければスキップ。既に最新なら書き込みしない (冪等)。
    """
    claude_md = NXT_ROOT / CLAUDE_MD_FILENAME
    if not claude_md.exists():
        print(f"  {CLAUDE_MD_FILENAME}: 本元ルートに無いためスキップ")
        return False

    try:
        existing = claude_md.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        print(f"  {CLAUDE_MD_FILENAME}: 読み込み失敗 (スキップ)")
        return False

    updated = sync_os_imports_in_claude_md(existing, "")
    if updated is None:
        print(f"  {CLAUDE_MD_FILENAME}: `## erqo-next OS` 見出しなしでスキップ")
        return False
    if updated == existing:
        print(f"  {CLAUDE_MD_FILENAME}: 同期済み")
        return False

    claude_md.write_text(updated, encoding="utf-8")
    print(f"  {CLAUDE_MD_FILENAME}: 本元 `## erqo-next OS` ブロックを最新化")
    return True


def cmd_setup() -> None:
    """初回セットアップ: 本元 CLAUDE.md 同期 + Hook + 共通 permission + スキル + マニフェスト。"""
    _require_source()
    print(f"erqo-next 本体セットアップ: {PROJECT_ROOT.name}")
    print()

    # 0. 本元 CLAUDE.md の erqo-next OS ブロックを OS_SPECS_FILES と同期
    sync_source_claude_md()

    # 1. Hook 設定
    setup_hooks(PROJECT_ROOT)

    # 2. 共通 permission 設定
    setup_permission_defaults(PROJECT_ROOT)

    # 3. スキルコピー
    setup_skills(PROJECT_ROOT, update_mode=False)

    # 4. マニフェスト記録
    setup_os_skills_manifest(PROJECT_ROOT)

    print()
    print("セットアップ完了。新しいセッションを開始するとスキルが使えます。")


def cmd_update() -> None:
    """スキルのみ再コピー。Hook は触らない。"""
    _require_source()
    print(f"erqo-next 本体スキル更新: {PROJECT_ROOT.name}")
    print()

    setup_skills(PROJECT_ROOT, update_mode=True)
    setup_os_skills_manifest(PROJECT_ROOT)

    print()
    print("更新完了。")


def cmd_sync_hook() -> None:
    """PostToolUse Hook 用: skills/ 配下のファイルが編集されたら再コピーを走らせる。

    Claude Code から stdin に渡される JSON を読み、tool_input.file_path が
    skills/ 配下なら setup_skills + setup_os_skills_manifest を silent 実行する。
    skills/ 配下でなければ何もせず終了する。失敗しても 0 で抜ける（hook を妨げない）。
    """
    if not IS_SOURCE or PROJECT_ROOT is None:
        return

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return

    tool_input = data.get("tool_input", {}) or {}
    tool_response = data.get("tool_response", {}) or {}
    file_path = (
        tool_response.get("filePath")
        or tool_input.get("file_path")
        or ""
    )
    if not file_path:
        return

    parts = Path(file_path).parts
    if SKILLS_DIR_NAME not in parts:
        return

    # silent 実行: stdout/stderr を捨てる
    devnull = open(os.devnull, "w", encoding="utf-8")
    saved_out, saved_err = sys.stdout, sys.stderr
    sys.stdout = devnull
    sys.stderr = devnull
    try:
        setup_skills(PROJECT_ROOT, update_mode=True)
        setup_os_skills_manifest(PROJECT_ROOT)
    except Exception:
        pass
    finally:
        sys.stdout = saved_out
        sys.stderr = saved_err
        devnull.close()


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python core/dev.py <setup|update|_sync>", file=sys.stderr)
        sys.exit(1)

    action = sys.argv[1]

    if action == "setup":
        cmd_setup()
    elif action == "update":
        cmd_update()
    elif action == "_sync":
        cmd_sync_hook()
    else:
        print(f"エラー: 不明なアクション '{action}'", file=sys.stderr)
        print("有効なアクション: setup, update, _sync", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
