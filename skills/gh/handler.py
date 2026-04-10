"""handler.py - /gh Git 操作スクリプト

プロジェクトの git 操作を安全に実行する。

使い方:
    python .nxt-core/skills/gh/handler.py check           # 差分確認
    python .nxt-core/skills/gh/handler.py commit "msg"     # git add -A → commit
    python .nxt-core/skills/gh/handler.py push             # push
    python .nxt-core/skills/gh/handler.py full "msg"       # commit + push
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

# core/ をパスに追加
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "core"))

from paths import PROJECT_ROOT, IS_SOURCE
from feedback import init_error_handling

init_error_handling()


def _require_project() -> Path:
    """プロジェクト環境チェック。"""
    if IS_SOURCE or PROJECT_ROOT is None:
        print("エラー: プロジェクト内でのみ実行できます。", file=sys.stderr)
        sys.exit(1)
    return PROJECT_ROOT


def _run(cmd: list[str], cwd: str | None = None, check: bool = True) -> subprocess.CompletedProcess:
    """git コマンドを実行する。"""
    project = _require_project()
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        cwd=cwd or str(project), encoding="utf-8",
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


# --- コマンド ---


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
    """変更をステージング + コミットする。"""
    if not _has_changes():
        print("変更なし")
        return

    _run(["git", "add", "-A"])
    _run(["git", "commit", "-m", message])
    print(f"コミット完了: {message}")


def cmd_push() -> None:
    """現在ブランチをリモートにプッシュする。"""
    branch = _get_branch()

    remote = _run(["git", "remote"], check=False)
    if not remote.stdout.strip():
        print("エラー: リモートが設定されていません。", file=sys.stderr)
        sys.exit(1)

    _run(["git", "push", "origin", branch])
    print(f"プッシュ完了: {branch} -> origin/{branch}")


def cmd_full(message: str) -> None:
    """commit + push を一括実行する。"""
    print("=== 1/2 コミット ===")
    cmd_commit(message)
    print("\n=== 2/2 プッシュ ===")
    cmd_push()
    print("\n=== 完了 ===")


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: handler.py <check|commit|push|full> [message]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "check":
        cmd_check()
    elif command == "commit":
        if len(sys.argv) < 3:
            print("エラー: コミットメッセージを指定してください。", file=sys.stderr)
            sys.exit(1)
        cmd_commit(sys.argv[2])
    elif command == "push":
        cmd_push()
    elif command == "full":
        if len(sys.argv) < 3:
            print("エラー: コミットメッセージを指定してください。", file=sys.stderr)
            sys.exit(1)
        cmd_full(sys.argv[2])
    else:
        print(f"エラー: 不明なコマンド '{command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
