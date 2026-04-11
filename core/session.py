"""session.py - セッション管理 (SessionStart Hook)

SessionStart Hook から呼ばれ、additionalContext を stdout に JSON 出力する。

使い方:
    python .nxt-core/core/session.py              # 通常モード (startup/resume)
    python .nxt-core/core/session.py --compact    # コンパクションモード
"""

import io
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import (
    PROJECT_ROOT,
    IS_SOURCE,
    STATE_DIR,
    DESIGN_DIR,
    LOGS_DIR,
    VERSION_FILE,
    VERSION_CHECK_STATE_FILE,
)
from constants import (
    STATUS_TODO,
    STATUS_WIP,
    STATE_FILE_PREFIX,
    SESSION_LOG_PATTERN,
    ERQO_REPO_URL,
    VERSION_CHECK_INTERVAL_SEC,
    MAX_CONTEXT_LENGTH,
    SESSION_LOG_PREVIEW_LINES,
)
from index import reindex
from page_parser import parse_sections, parse_tp_row
from feedback import init_error_handling

init_error_handling()


# --- ヘルパー ---


def _log_dir() -> Path | None:
    """セッションログディレクトリ。"""
    return LOGS_DIR


def _design_dir() -> Path | None:
    """設計ディレクトリ。"""
    return DESIGN_DIR


def _run_git(*args: str, timeout: int = 5) -> str | None:
    """git コマンドを実行して stdout を返す。失敗時は None。"""
    if not PROJECT_ROOT:
        return None
    try:
        result = subprocess.run(
            ["git", *args],
            capture_output=True, text=True,
            cwd=str(PROJECT_ROOT), timeout=timeout,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        pass
    return None


# --- 各機能 ---


def run_reindex() -> None:
    """_index.json を再生成する。"""
    reindex()


def check_version() -> str | None:
    """VERSION ファイルと GitHub API を比較し、新バージョンがあれば通知文を返す。"""
    version_file = VERSION_FILE
    if not version_file.exists():
        return None

    # 1日1回制限
    check_file = VERSION_CHECK_STATE_FILE
    if check_file:
        try:
            if check_file.exists():
                data = json.loads(check_file.read_text(encoding="utf-8"))
                last_check = datetime.fromisoformat(data["checked_at"])
                now = datetime.now(timezone.utc)
                if (now - last_check).total_seconds() < VERSION_CHECK_INTERVAL_SEC:
                    return None
        except (json.JSONDecodeError, KeyError, OSError, ValueError):
            pass

    local_version = version_file.read_text(encoding="utf-8").strip()

    # GitHub API で最新タグを取得
    try:
        result = subprocess.run(
            ["git", "ls-remote", "--tags", "--sort=-v:refname", ERQO_REPO_URL],
            capture_output=True, text=True, timeout=5,
        )
        if result.returncode != 0 or not result.stdout.strip():
            return None

        # 最新タグを抽出
        first_line = result.stdout.strip().splitlines()[0]
        remote_version = first_line.split("refs/tags/")[-1].lstrip("v")
    except (subprocess.TimeoutExpired, OSError, IndexError):
        return None

    # チェック日時を記録
    if check_file:
        check_file.parent.mkdir(parents=True, exist_ok=True)
        check_file.write_text(
            json.dumps({"checked_at": datetime.now(timezone.utc).isoformat(),
                        "local": local_version, "remote": remote_version},
                       ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    if remote_version and remote_version != local_version:
        return (
            "\n## アップデート"
            f"\n新しいバージョン ({remote_version}) が利用可能です (現在: {local_version})"
        )
    return None


def check_git_sync() -> str | None:
    """リモートとの同期状態をチェックし、安全時は自動 pull する。"""
    if IS_SOURCE or not PROJECT_ROOT:
        return None

    # 現在のブランチ名を取得
    branch = _run_git("rev-parse", "--abbrev-ref", "HEAD")
    if not branch:
        return None

    # fetch
    _run_git("fetch", "origin", branch, timeout=10)

    # ローカルとリモートの比較
    local_rev = _run_git("rev-parse", "HEAD")
    remote_rev = _run_git("rev-parse", f"origin/{branch}")
    if not local_rev or not remote_rev:
        return None

    if local_rev == remote_rev:
        return None  # 同期済み

    # リモートが先行しているか
    merge_base = _run_git("merge-base", "HEAD", f"origin/{branch}")
    if merge_base != local_rev:
        return None  # ローカルが先行 or 分岐 → 通知不要

    # リモートが先行: ローカルに未コミットの変更があるか
    status = _run_git("status", "--porcelain")
    if status:
        return f"\n## git 同期\nリモートに新しいコミットがあります ({branch})。ローカルに変更があるため自動 pull しません。"

    # 安全: 自動 pull
    pull_result = _run_git("pull", "--ff-only", "origin", branch, timeout=15)
    if pull_result is not None:
        return f"\n## git 同期\nリモートから最新を取得しました ({branch})"
    return None


def find_interrupted_pipelines() -> list[dict]:
    """中断されたパイプラインの状態ファイルを検出する。"""
    if not STATE_DIR or not STATE_DIR.exists():
        return []

    interrupted = []
    for state_file in STATE_DIR.glob(f"{STATE_FILE_PREFIX}*.json"):
        try:
            data = json.loads(state_file.read_text(encoding="utf-8"))
            interrupted.append(data)
        except (json.JSONDecodeError, OSError):
            continue
    return interrupted


def find_in_progress_tasks() -> list[dict]:
    """TP ページから未完了タスクを検索する。"""
    design_dir = _design_dir()
    if not design_dir or not design_dir.exists():
        return []

    tasks = []
    for tp_file in design_dir.rglob("*.md"):
        try:
            content = tp_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        for line in content.splitlines():
            row = parse_tp_row(line)
            if row and row["status"] in (STATUS_TODO, STATUS_WIP):
                tasks.append(row)
    return tasks


def find_latest_session_log() -> Path | None:
    """直近のセッションログファイルを返す。"""
    log_dir = _log_dir()
    if not log_dir or not log_dir.exists():
        return None
    md_files = sorted(log_dir.rglob(SESSION_LOG_PATTERN), reverse=True)
    return md_files[0] if md_files else None


def extract_decisions(log_path: Path) -> str | None:
    """セッションログから決定事項セクションを抽出する。"""
    try:
        content = log_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    sections = parse_sections(content)
    for sec in sections:
        if "決定事項" in sec["title"] or "決定事項" in sec.get("id", ""):
            return sec["content"].strip() if sec["content"].strip() else None
    return None


# --- コンテキスト構築 ---


def build_orientation_gate() -> str:
    """視点宣言ゲート: セッション開始時に必ず視点とスコープを宣言させる。

    specs/07-scopes.md の 3 スコープ判断を毎セッション冒頭で能動的に照合させ、
    本元 / プロジェクトの取り違えによる致命的な副作用を防ぐ。
    """
    if IS_SOURCE:
        repo_label = "本元 OS (IS_SOURCE=True)"
    else:
        repo_label = "プロジェクト OS (IS_SOURCE=False)"

    return (
        "# 視点宣言ゲート (必須)\n"
        f"現在のリポジトリ: {repo_label}\n"
        "\n"
        "最初の応答の冒頭で、以下を必ず記載してから作業に入ること:\n"
        "- 視点: 本元 OS / プロジェクト OS\n"
        "- 依頼のスコープ: 本元 / プロジェクト / 共通\n"
        "- 根拠: (なぜそう判断したか一言)\n"
        "\n"
        "この宣言が済むまで一切の実作業に進まない。"
    )


def build_normal_context() -> str:
    """通常モード: 視点宣言ゲート + 全7項目を収集。"""
    parts = [build_orientation_gate()]

    # 1. プロジェクト名
    if PROJECT_ROOT and not IS_SOURCE:
        parts.append(f"# プロジェクト: {PROJECT_ROOT.name}")
    else:
        parts.append("# erqo-next 本体リポジトリ")

    # 2. インデックス再生成
    run_reindex()

    # 3. バージョンチェック
    version_msg = check_version()
    if version_msg:
        parts.append(version_msg)

    # 4. git 同期チェック
    sync_msg = check_git_sync()
    if sync_msg:
        parts.append(sync_msg)

    # 5. 中断パイプライン
    interrupted = find_interrupted_pipelines()
    if interrupted:
        parts.append("\n## 中断されたパイプライン")
        for task in interrupted:
            task_id = task.get("task_id", "unknown")
            step = task.get("current_step", "?")
            parts.append(f"- {task_id}: ステップ {step} で中断 (/codi {task_id} で再開できます)")

    # 6. 進行中タスク
    in_progress = find_in_progress_tasks()
    if in_progress:
        parts.append("\n## 進行中のタスク")
        for task in in_progress:
            parts.append(f"- [{task['deps']}] {task['id']}: {task['name']}")

    # 7. 直近セッションログ
    log_path = find_latest_session_log()
    if log_path:
        try:
            content = log_path.read_text(encoding="utf-8")
            lines = content.splitlines()
            summary = "\n".join(lines[:SESSION_LOG_PREVIEW_LINES])
            if len(lines) > SESSION_LOG_PREVIEW_LINES:
                summary += "\n(...省略)"
            parts.append(f"\n## 直近のセッションログ\n{summary}")
        except (OSError, UnicodeDecodeError):
            pass

    return "\n".join(parts)


def build_compact_context() -> str:
    """compact モード: 視点宣言ゲート + 中断パイプライン + 進行中タスク + 直近決定事項。"""
    parts = [build_orientation_gate()]

    # 1. 中断パイプライン
    interrupted = find_interrupted_pipelines()
    if interrupted:
        parts.append("## 中断されたパイプライン")
        for task in interrupted:
            task_id = task.get("task_id", "unknown")
            step = task.get("current_step", "?")
            completed = ", ".join(task.get("completed_steps", []))
            parts.append(f"- {task_id}: ステップ {step} で中断 (完了済み: {completed})")

    # 2. 進行中タスク
    in_progress = find_in_progress_tasks()
    if in_progress:
        parts.append("\n## 進行中のタスク")
        for task in in_progress:
            parts.append(f"- [{task['deps']}] {task['id']}: {task['name']}")

    # 3. 直近決定事項
    log_path = find_latest_session_log()
    if log_path:
        decisions = extract_decisions(log_path)
        if decisions:
            parts.append(f"\n## 直近の決定事項\n{decisions}")

    if not parts:
        return ""
    return "\n".join(parts)


# --- 出力 ---


def output_hook_response(context: str) -> None:
    """SessionStart Hook 用の JSON を stdout に出力する。"""
    if not context:
        print(json.dumps({}))
        return

    if len(context) > MAX_CONTEXT_LENGTH:
        context = context[:MAX_CONTEXT_LENGTH - 50] + "\n\n(...コンテキストが長いため省略されました)"

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    print(json.dumps(output, ensure_ascii=False))


def main() -> None:
    compact = "--compact" in sys.argv

    if compact:
        context = build_compact_context()
    else:
        context = build_normal_context()

    output_hook_response(context)


if __name__ == "__main__":
    main()
