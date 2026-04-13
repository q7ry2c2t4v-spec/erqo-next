"""research_sync.py — .libs/research/ を erqo-research リポジトリと同期する薄いラッパ

設計: .libs/research/os/rsrc-research-shared.md (RSRC-RESEARCH-SHARED)

3 つのエントリポイント:
- ensure_cloned:  .libs/research/ が無ければ clone (初回セットアップ用)
- auto_pull:      セッション開始時に呼ぶ (git pull --ff-only)
- auto_push:      /rsrc の保存後に呼ぶ (add + commit + push)

いずれも失敗しても致命的エラーにせず、stderr に警告を出して続行する。
研究ノートが無くても他の OS 機能は動作する (degraded mode)。

使い方 (CLI):
    python core/research_sync.py ensure           # 無ければ clone
    python core/research_sync.py pull             # 最新を取り込み
    python core/research_sync.py push "msg"       # 変更を送信
"""

import io
import subprocess
import sys
from pathlib import Path

# Windows UTF-8 出力 (L2 Python §2)
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from constants import RESEARCH_REPO_URL
from paths import PROJECT_ROOT, RESEARCH_DIR
from feedback import init_error_handling

init_error_handling()


# --- 内部ヘルパ ---


def _require_research_dir() -> Path:
    """RESEARCH_DIR が決定できなければエラー終了。"""
    if RESEARCH_DIR is None:
        print(
            "[research_sync] PROJECT_ROOT が見つかりません (CLAUDE.md 未発見)",
            file=sys.stderr,
        )
        sys.exit(1)
    return RESEARCH_DIR


def _is_clone(dir_path: Path) -> bool:
    """.git が存在すれば clone 済みとみなす。"""
    return (dir_path / ".git").exists()


def _run_git(cwd: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    """git サブコマンドを実行する。check=False で失敗しても戻り値で判定する。"""
    return subprocess.run(
        ["git", "-C", str(cwd), *args],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


def _warn(message: str) -> None:
    """stderr に警告を出す (致命的エラー扱いにしない)。"""
    print(f"[research_sync] {message}", file=sys.stderr)


# --- 公開 API ---


def ensure_cloned(research_dir: Path | None = None) -> bool:
    """.libs/research/ が無ければ clone する。既存なら何もしない。

    戻り値: True = clone 済み or 新規 clone 成功、False = 失敗 (警告のみ)
    """
    target = research_dir if research_dir is not None else _require_research_dir()
    if _is_clone(target):
        return True

    target.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(
        ["git", "clone", RESEARCH_REPO_URL, str(target)],
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    if result.returncode != 0:
        _warn(f"clone 失敗 (degraded mode で続行): {result.stderr.strip()}")
        return False
    return True


def auto_pull(research_dir: Path | None = None) -> None:
    """セッション開始時に呼ぶ。git pull --ff-only。失敗は警告のみ。"""
    target = research_dir if research_dir is not None else _require_research_dir()
    if not _is_clone(target):
        return

    result = _run_git(target, ["pull", "--ff-only"])
    if result.returncode != 0:
        _warn(f"pull 失敗: {result.stderr.strip()}")


def auto_push(message: str, research_dir: Path | None = None) -> None:
    """/rsrc の保存後に呼ぶ。変更があれば add + commit + push。失敗は警告のみ。"""
    target = research_dir if research_dir is not None else _require_research_dir()
    if not _is_clone(target):
        _warn(".libs/research/ が clone されていません (push スキップ)")
        return

    status = _run_git(target, ["status", "--porcelain"])
    if not status.stdout.strip():
        return  # 変更なし

    add_result = _run_git(target, ["add", "-A"])
    if add_result.returncode != 0:
        _warn(f"add 失敗: {add_result.stderr.strip()}")
        return

    commit_result = _run_git(target, ["commit", "-m", message])
    if commit_result.returncode != 0:
        _warn(f"commit 失敗: {commit_result.stderr.strip()}")
        return

    push_result = _run_git(target, ["push"])
    if push_result.returncode != 0:
        _warn(f"push 失敗 (ローカルには commit 済み、次回再試行可能): {push_result.stderr.strip()}")


# --- CLI ---


def main() -> None:
    if PROJECT_ROOT is None:
        print("[research_sync] PROJECT_ROOT が見つかりません", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) < 2:
        print("usage: python core/research_sync.py <ensure|pull|push> [message]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]

    if command == "ensure":
        ok = ensure_cloned()
        sys.exit(0 if ok else 1)
    elif command == "pull":
        auto_pull()
    elif command == "push":
        if len(sys.argv) < 3:
            print("エラー: push にはコミットメッセージが必要です。", file=sys.stderr)
            sys.exit(1)
        auto_push(sys.argv[2])
    else:
        print(f"エラー: 不明なコマンド '{command}' (ensure/pull/push)", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
