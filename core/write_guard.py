"""write_guard.py — PreToolUse 書き込みパス保護ガード

Claude Code は `.git/` と `.claude/` 配下を「保護パス」として扱い、
bypassPermissions モードでも書き込み時に確認プロンプトを出す。
設定による無効化は存在しない (specs/09-memory.md 参照)。

このスクリプトは PreToolUse Hook から呼ばれ、stdin で渡される JSON の
tool_input.file_path を抽出して保護パス判定し、該当時は exit 2 で
ツール実行をブロックする。Claude Code の確認プロンプト発生を防止する。

呼び出し元:
- PreToolUse Hook (matcher: Write|Edit|NotebookEdit)

動作仕様:
- 例外サブディレクトリ (commands/agents/skills/worktrees) は素通し
- file_path が取得不能・プロジェクト外・解釈不能な入力は素通し (fail-open)
- 例外発生時も exit 0 で抜ける (Hook が AI 作業を妨害しないため)

Hook 設定例:
    "PreToolUse": [{
      "matcher": "Write|Edit|NotebookEdit",
      "hooks": [{
        "type": "command",
        "command": "python \\"$CLAUDE_PROJECT_DIR/{nxt}/core/write_guard.py\\"",
        "timeout": 5
      }]
    }]
"""

import io
import json
import os
import sys
from pathlib import Path

# Windows UTF-8 出力 (エラーメッセージが日本語のため必須)
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from constants import PROTECTED_PATH_PREFIXES, PROTECTED_PATH_EXCEPTIONS


def _to_relative(file_path: str, project_dir: str) -> str | None:
    """file_path をプロジェクトルート相対の posix パスに変換する。

    プロジェクト外や解釈不能なパスの場合は None。
    """
    try:
        fp = Path(file_path)
        if not fp.is_absolute():
            fp = Path(project_dir) / fp
        abs_path = fp.resolve()
        abs_project = Path(project_dir).resolve()
        rel = abs_path.relative_to(abs_project)
        return rel.as_posix()
    except (ValueError, OSError):
        return None


def _is_protected(rel_path: str) -> bool:
    """rel_path が保護パスに該当するか判定する。

    PROTECTED_PATH_PREFIXES に前方一致し、かつ
    PROTECTED_PATH_EXCEPTIONS のどれにも該当しなければ保護対象。
    """
    for exception in PROTECTED_PATH_EXCEPTIONS:
        if rel_path.startswith(exception):
            return False
    for prefix in PROTECTED_PATH_PREFIXES:
        if rel_path.startswith(prefix):
            return True
    return False


def _error_message(path: str) -> str:
    return (
        f"書き込み先 \"{path}\" は Claude Code の保護パスです。\n"
        f".git/ と .claude/ の配下 (commands/, agents/, skills/, worktrees/ を除く) には\n"
        f"書き込めません。プロジェクトルート直下のドット始まりファイル、または\n"
        f"保護パス外のディレクトリに置いてください。\n"
        f"詳細: specs/09-memory.md"
    )


def main() -> None:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    if not project_dir:
        return  # fail-open: Hook 環境変数が無いなら判定不能

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return  # fail-open: 解釈不能な入力は素通し

    tool_input = data.get("tool_input", {}) or {}
    file_path = (
        tool_input.get("file_path")
        or tool_input.get("notebook_path")
        or ""
    )
    if not file_path:
        return

    rel_path = _to_relative(file_path, project_dir)
    if rel_path is None:
        return  # プロジェクト外への書き込みは対象外

    if _is_protected(rel_path):
        print(_error_message(rel_path), file=sys.stderr)
        sys.exit(2)  # exit 2 = Claude Code がツール実行をブロックする


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # 失敗時は AI 作業を妨げないため fail-open
        sys.exit(0)
