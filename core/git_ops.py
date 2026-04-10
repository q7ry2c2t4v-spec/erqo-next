"""git_ops.py — git 操作ユーティリティ

プロジェクト・本体リポジトリ共通で使う git 操作ヘルパー。

呼び出し元:
- /codi ステップ5 (実装の commit)
- 手動の差分確認

使い方:
    python core/git_ops.py check          # 差分確認
    python core/git_ops.py commit "msg"   # add -A → commit
"""

import io
import subprocess
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import PROJECT_ROOT
from feedback import init_error_handling

init_error_handling()


def _require_root() -> Path:
    """プロジェクトルートを返す。見つからなければエラー終了。"""
    if PROJECT_ROOT is None:
        print("エラー: プロジェクトルートが見つかりません。", file=sys.stderr)
        sys.exit(1)
    return PROJECT_ROOT


def _run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    """git コマンドを実行する。"""
    root = _require_root()
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        cwd=str(root), encoding="utf-8",
    )
    if check and result.returncode != 0:
        print(f"エラー: {' '.join(cmd)}", file=sys.stderr)
        if result.stderr.strip():
            print(f"  {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return result


def _get_branch() -> str:
    return _run(["git", "branch", "--show-current"]).stdout.strip()


def _has_changes() -> bool:
    staged = _run(["git", "diff", "--cached", "--quiet"], check=False)
    unstaged = _run(["git", "diff", "--quiet"], check=False)
    untracked = _run(["git", "ls-files", "--others", "--exclude-standard"], check=False)
    return staged.returncode != 0 or unstaged.returncode != 0 or bool(untracked.stdout.strip())


# --- 公開 API ---


def cmd_check() -> None:
    """差分一覧を表示する。"""
    branch = _get_branch()
    print(f"ブランチ: {branch}")

    if not _has_changes():
        print("変更なし")
        return

    status = _run(["git", "status", "--short"])
    print(f"\n変更ファイル:\n{status.stdout.strip()}")

    diff_stat = _run(["git", "diff", "--stat", "HEAD"], check=False)
    if diff_stat.stdout.strip():
        print(f"\n差分統計:\n{diff_stat.stdout.strip()}")


def cmd_commit(message: str) -> None:
    """全変更をステージングしてコミットする。"""
    if not _has_changes():
        print("変更なし")
        return

    _run(["git", "add", "-A"])
    _run(["git", "commit", "-m", message])
    print(f"コミット完了: {message}")


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python core/git_ops.py <check|commit> [message]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "check":
        cmd_check()
    elif command == "commit":
        if len(sys.argv) < 3:
            print("エラー: コミットメッセージを指定してください。", file=sys.stderr)
            sys.exit(1)
        cmd_commit(sys.argv[2])
    else:
        print(f"エラー: 不明なコマンド '{command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
