"""feedback_sync.py — フィードバック共有リポジトリ (erqo-feedback) 同期

プロジェクト → 本元への一方向通知経路。`/fb` で送信された JSON を
`.libs/fb-shared/inbox/` 配下に `<project_name>-<filename>.json` として
保存し、erqo-feedback リポジトリに push する。本元はセッション開始時に
pull + 新着表示する。

設計の対比 (erqo-research との違い):
- erqo-research: 本元 / 全プロジェクトが双方向に share (各々が読み書き)
- erqo-feedback: プロジェクトが push のみ、本元が pull のみ (一方向通知)

リポジトリ未作成時の挙動:
- 初回失敗で `.claude/state/_feedback_sync_disabled.flag` を立てる
- 以降同セッション/起動では sync を試みない (毎セッションのノイズ抑制)
- ユーザーがリポジトリを作成 + flag を削除すれば再開
- いずれの失敗も degraded mode (致命的エラーにしない、他機能は動作)

5 つのエントリポイント:
- ensure_cloned:        .libs/fb-shared/ が無ければ clone (初回セットアップ用)
- auto_pull:            本元のセッション開始時 (新着 inbox を取り込む)
- push_report:          プロジェクト側 fb 送信時 (1 JSON を push)
- missing_clone_warning: clone 未済時に復旧手順を返す
- list_inbox:           inbox の JSON 一覧を新しい順に返す (本元のセッション表示用)

使い方 (CLI):
    python core/feedback_sync.py ensure                # 無ければ clone
    python core/feedback_sync.py pull                  # 最新を取り込み (本元用)
    python core/feedback_sync.py push <report_path>    # JSON を 1 件送信
"""

import io
import shutil
import subprocess
import sys
from pathlib import Path

# Windows UTF-8 出力 (L2 Python §2)
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from constants import FEEDBACK_REPO_URL, FEEDBACK_INBOX_DIR_NAME
from paths import (
    FEEDBACK_INBOX_DIR,
    FEEDBACK_SHARED_DIR,
    FEEDBACK_SYNC_DISABLED_FILE,
    IS_SOURCE,
    PROJECT_ROOT,
)
from feedback import init_error_handling

init_error_handling()


# --- 内部ヘルパ ---


def _require_shared_dir() -> Path:
    """FEEDBACK_SHARED_DIR が決定できなければエラー終了。"""
    if FEEDBACK_SHARED_DIR is None:
        print(
            "[feedback_sync] PROJECT_ROOT が見つかりません (CLAUDE.md 未発見)",
            file=sys.stderr,
        )
        sys.exit(1)
    return FEEDBACK_SHARED_DIR


def _is_clone(dir_path: Path) -> bool:
    """.git が存在すれば clone 済みとみなす。"""
    return (dir_path / ".git").exists()


def _is_disabled() -> bool:
    """sticky-failure flag が立っているか。"""
    return FEEDBACK_SYNC_DISABLED_FILE is not None and FEEDBACK_SYNC_DISABLED_FILE.exists()


def _mark_disabled(reason: str) -> None:
    """sticky-failure flag を立てる。理由を中に書く (ユーザー判断材料)。"""
    if FEEDBACK_SYNC_DISABLED_FILE is None:
        return
    try:
        FEEDBACK_SYNC_DISABLED_FILE.parent.mkdir(parents=True, exist_ok=True)
        FEEDBACK_SYNC_DISABLED_FILE.write_text(
            f"feedback sync disabled.\nreason: {reason}\n"
            f"再開するには このファイルを削除してください: {FEEDBACK_SYNC_DISABLED_FILE}\n",
            encoding="utf-8",
        )
    except OSError:
        pass


_GIT_TIMEOUT_SEC = 10
_GIT_CLONE_TIMEOUT_SEC = 60


def _run_git(
    cwd: Path, args: list[str], timeout: int = _GIT_TIMEOUT_SEC,
) -> subprocess.CompletedProcess[str]:
    """git サブコマンドを実行する。check=False。タイムアウトは疑似レスポンスで返す。"""
    try:
        return subprocess.run(
            ["git", "-C", str(cwd), *args],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired:
        return subprocess.CompletedProcess(
            ["git", "-C", str(cwd), *args], 124, "", f"タイムアウト ({timeout}s)",
        )


def _warn(message: str) -> None:
    """stderr に警告を出す (致命的エラー扱いにしない)。"""
    print(f"[feedback_sync] {message}", file=sys.stderr)


def _project_name() -> str:
    """fb の push 時、ファイル名 prefix に使うプロジェクト名。"""
    if PROJECT_ROOT is None:
        return "unknown"
    return PROJECT_ROOT.name


# --- 公開 API ---


def ensure_cloned(shared_dir: Path | None = None) -> bool:
    """.libs/fb-shared/ が無ければ clone する。既存なら何もしない。

    戻り値: True = clone 済み or 新規 clone 成功、False = 失敗 (警告のみ)
    sticky-failure flag が立っているときは試行しない。
    """
    if _is_disabled():
        return False
    target = shared_dir if shared_dir is not None else _require_shared_dir()
    if _is_clone(target):
        return True

    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = subprocess.run(
            ["git", "clone", FEEDBACK_REPO_URL, str(target)],
            check=False,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=_GIT_CLONE_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        _warn(f"clone タイムアウト ({_GIT_CLONE_TIMEOUT_SEC}s、degraded mode で続行)")
        _mark_disabled(f"clone timeout ({FEEDBACK_REPO_URL})")
        return False
    if result.returncode != 0:
        _warn(f"clone 失敗 (degraded mode で続行): {result.stderr.strip()}")
        _mark_disabled(f"clone failed: {result.stderr.strip()[:200]}")
        return False
    return True


def missing_clone_warning(shared_dir: Path | None = None) -> str | None:
    """clone されていなければ復旧手順付きの警告文字列を返す。clone 済みなら None。

    sticky-failure flag が立っているときも警告を返す (リポジトリ未作成等のユーザー認知用)。
    """
    target = shared_dir if shared_dir is not None else FEEDBACK_SHARED_DIR
    if target is None:
        return None
    if _is_clone(target):
        return None

    setup_cmd = (
        "python core/dev.py setup" if IS_SOURCE
        else "python .nxt-core/core/install.py --update"
    )
    flag_note = ""
    if _is_disabled():
        flag_note = (
            f"\n   現在 sticky-failure flag のため sync は停止中: "
            f"{FEEDBACK_SYNC_DISABLED_FILE}\n"
            f"   リポジトリ作成後、flag を削除して再開してください。"
        )
    return (
        f"⚠ `.libs/fb-shared/` が未セットアップです (erqo-feedback リポジトリ)。\n"
        f"   `{setup_cmd}` を実行して clone を試みてください。"
        f"   未作成の場合は GitHub で `erqo-feedback` リポジトリを作成してください。"
        f"{flag_note}"
    )


def auto_pull(shared_dir: Path | None = None) -> None:
    """本元のセッション開始時に呼ぶ。git pull --ff-only。失敗は警告のみ。"""
    if _is_disabled():
        return
    target = shared_dir if shared_dir is not None else _require_shared_dir()
    if not _is_clone(target):
        return

    result = _run_git(target, ["pull", "--ff-only"])
    if result.returncode != 0:
        _warn(f"pull 失敗: {result.stderr.strip()}")


def push_report(report_path: Path, shared_dir: Path | None = None) -> bool:
    """1 件の fb JSON を inbox に追加して push する。

    プロジェクト側 send_feedback の末尾で呼ばれる想定。失敗は警告のみ (戻り値 False)。
    本元 (IS_SOURCE) では何もしない (本元は /fb を持たない設計だが念のためガード)。
    sticky-failure flag が立っているときも何もしない。
    """
    if IS_SOURCE or _is_disabled():
        return False

    target = shared_dir if shared_dir is not None else _require_shared_dir()
    if not _is_clone(target):
        return False
    inbox = target / FEEDBACK_INBOX_DIR_NAME
    inbox.mkdir(parents=True, exist_ok=True)

    project = _project_name()
    dst = inbox / f"{project}-{report_path.name}"
    try:
        shutil.copy2(report_path, dst)
    except OSError as exc:
        _warn(f"inbox へのコピー失敗: {exc}")
        return False

    add_result = _run_git(target, ["add", str(dst.relative_to(target))])
    if add_result.returncode != 0:
        _warn(f"add 失敗: {add_result.stderr.strip()}")
        return False

    commit_msg = f"fb: {project} - {report_path.stem}"
    commit_result = _run_git(target, ["commit", "-m", commit_msg])
    if commit_result.returncode != 0:
        _warn(f"commit 失敗: {commit_result.stderr.strip()}")
        return False

    push_result = _run_git(target, ["push"])
    if push_result.returncode != 0:
        _warn(
            f"push 失敗 (ローカルには commit 済み、次回再試行可能): "
            f"{push_result.stderr.strip()}"
        )
        return False
    return True


def list_inbox(shared_dir: Path | None = None, limit: int = 10) -> list[Path]:
    """inbox の JSON 一覧を新しい順に返す (本元のセッション表示用)。

    clone されていない / inbox が空なら空リストを返す。
    """
    target = shared_dir if shared_dir is not None else FEEDBACK_SHARED_DIR
    if target is None or not _is_clone(target):
        return []
    inbox = target / FEEDBACK_INBOX_DIR_NAME
    if not inbox.exists():
        return []
    files = sorted(
        (p for p in inbox.glob("*.json") if p.is_file()),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    return files[:limit]


# --- CLI ---


def main() -> None:
    if PROJECT_ROOT is None:
        print("[feedback_sync] PROJECT_ROOT が見つかりません", file=sys.stderr)
        sys.exit(1)

    if len(sys.argv) < 2:
        print(
            "usage: python core/feedback_sync.py <ensure|pull|push> [args...]",
            file=sys.stderr,
        )
        sys.exit(1)

    command = sys.argv[1]

    if command == "ensure":
        ok = ensure_cloned()
        sys.exit(0 if ok else 1)
    elif command == "pull":
        auto_pull()
    elif command == "push":
        if len(sys.argv) < 3:
            print("エラー: push には JSON ファイルパスが必要です。", file=sys.stderr)
            sys.exit(1)
        report_path = Path(sys.argv[2]).resolve()
        if not report_path.exists():
            print(f"エラー: {report_path} が存在しません", file=sys.stderr)
            sys.exit(1)
        ok = push_report(report_path)
        sys.exit(0 if ok else 1)
    elif command == "list":
        for p in list_inbox():
            print(p)
    else:
        print(f"エラー: 不明なコマンド '{command}' (ensure/pull/push/list)", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
