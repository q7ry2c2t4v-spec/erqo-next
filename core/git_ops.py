"""git_ops.py — git 操作ユーティリティ

プロジェクト・本体リポジトリ共通で使う git 操作ヘルパー。
旧 skills/gh/handler.py から移設し、IS_SOURCE ガードを撤去したもの。

呼び出し元:
- skills/wrap (セッション記録 + コミット統合スキル)
- /codi ステップ5 (実装の commit)

使い方:
    python core/git_ops.py check                        # 差分確認
    python core/git_ops.py commit "msg"                 # add -A → commit
    python core/git_ops.py commit "msg" --files A B C   # 指定ファイルのみ commit
    python core/git_ops.py push                         # push
    python core/git_ops.py full "msg"                   # commit + push
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


def cmd_commit(message: str, files: list[str] | None = None) -> None:
    """変更をステージング + コミットする。

    files が指定された場合はそれだけステージングする。
    None の場合は git add -A で全変更をステージングする。
    """
    if not _has_changes() and not files:
        print("変更なし")
        return

    if files:
        _run(["git", "add", "--", *files])
    else:
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
        print("usage: python core/git_ops.py <check|commit|push|full> [message] [--files ...]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "check":
        cmd_check()
    elif command == "commit":
        if len(sys.argv) < 3:
            print("エラー: コミットメッセージを指定してください。", file=sys.stderr)
            sys.exit(1)
        message = sys.argv[2]
        files = None
        if "--files" in sys.argv:
            idx = sys.argv.index("--files")
            files = sys.argv[idx + 1:]
        cmd_commit(message, files)
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
