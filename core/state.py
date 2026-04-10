"""state.py - /codi パイプラインの状態管理

状態ファイルの作成・更新・読取・削除を行う。
atomic write (fsync + rename) で中断安全性を保証する。

使い方:
    python .nxt-core/core/state.py TASK-ID init
    python .nxt-core/core/state.py TASK-ID complete STEP
    python .nxt-core/core/state.py TASK-ID get
    python .nxt-core/core/state.py TASK-ID delete
"""

import io
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import STATE_DIR, DESIGN_DIR
from constants import (
    TP_FILE_PATTERN,
    STATUS_DONE,
    STATE_FILE_PREFIX,
    PIPELINE_STEPS,
)
from page_parser import parse_tp_row
from feedback import init_error_handling

init_error_handling()


def _state_file(task_id: str) -> Path:
    """状態ファイルのパスを返す。"""
    return STATE_DIR / f"{STATE_FILE_PREFIX}{task_id}.json"


def _now_iso() -> str:
    """現在時刻を ISO 8601 形式で返す。"""
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _atomic_write_json(target: Path, data: dict) -> None:
    """JSON を atomic write する (fsync + rename)。"""
    target.parent.mkdir(parents=True, exist_ok=True)

    tmp_fd, tmp_path = tempfile.mkstemp(dir=target.parent, suffix=".tmp")
    try:
        with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        Path(tmp_path).replace(target)
    except BaseException:
        Path(tmp_path).unlink(missing_ok=True)
        raise


def _read_state(task_id: str) -> dict | None:
    """状態ファイルを読み込む。存在しなければ None。"""
    path = _state_file(task_id)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def check_deps(task_id: str) -> list[str]:
    """TP テーブルから依存タスクを取得し、未完了のものを返す。

    Returns: 未完了の依存タスク ID リスト (空なら全完了)
    """
    if not DESIGN_DIR or not DESIGN_DIR.exists():
        return []

    # TP テーブルから対象タスクの依存を探す
    deps = []
    all_tasks = {}  # id -> status

    for tp_file in DESIGN_DIR.rglob(TP_FILE_PATTERN):
        try:
            content = tp_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        for line in content.splitlines():
            row = parse_tp_row(line)
            if not row:
                continue

            all_tasks[row["id"]] = row["status"]

            if row["id"] == task_id and row["deps"] and row["deps"] != "なし":
                deps = [d.strip() for d in re.split(r"[,、]", row["deps"])]

    if not deps:
        return []

    # 依存タスクの完了チェック
    return [d for d in deps if all_tasks.get(d) != STATUS_DONE]


def init(task_id: str) -> None:
    """パイプライン開始時に状態ファイルを作成する。"""
    path = _state_file(task_id)

    # 既存の状態ファイルがあれば中断復旧モード
    existing = _read_state(task_id)
    if existing:
        completed = existing.get("completed_steps", [])
        step_num = len(completed)
        print("codi_state: 既存の状態ファイルを検出 (中断復旧)")
        print(f"  完了済み: {', '.join(completed) if completed else 'なし'}")
        print(f"  次のステップ: {PIPELINE_STEPS[step_num] if step_num < len(PIPELINE_STEPS) else '全完了'}")
        print(json.dumps(existing, ensure_ascii=False))
        return

    # 依存タスク完了チェック
    incomplete = check_deps(task_id)
    if incomplete:
        print(f"codi_state: 警告 - 未完了の依存タスクがあります: {', '.join(incomplete)}")

    state = {
        "task_id": task_id,
        "current_step": 1,
        "completed_steps": [],
        "started_at": _now_iso(),
        "last_update": _now_iso(),
    }

    _atomic_write_json(path, state)
    print(f"codi_state: 状態ファイル作成 -> {path}")


def complete(task_id: str, step_name: str) -> None:
    """ステップ完了を記録する。"""
    if step_name not in PIPELINE_STEPS:
        print(f"エラー: 不明なステップ '{step_name}'", file=sys.stderr)
        print(f"有効なステップ: {', '.join(PIPELINE_STEPS)}", file=sys.stderr)
        sys.exit(1)

    state = _read_state(task_id)
    if state is None:
        print(f"エラー: {task_id} の状態ファイルがありません。先に init してください。", file=sys.stderr)
        sys.exit(1)

    completed = state.get("completed_steps", [])
    if step_name not in completed:
        completed.append(step_name)

    step_index = PIPELINE_STEPS.index(step_name)
    state["current_step"] = step_index + 2
    state["completed_steps"] = completed
    state["last_update"] = _now_iso()

    _atomic_write_json(_state_file(task_id), state)
    print(f"codi_state: {step_name} 完了を記録 ({len(completed)}/{len(PIPELINE_STEPS)})")


def get(task_id: str) -> None:
    """現在の状態を JSON で出力する。"""
    state = _read_state(task_id)
    if state is None:
        print("{}")
        return
    print(json.dumps(state, ensure_ascii=False, indent=2))


def delete(task_id: str) -> None:
    """状態ファイルを削除する。"""
    path = _state_file(task_id)
    if path.exists():
        path.unlink()
        print(f"codi_state: 状態ファイル削除 -> {path}")
    else:
        print(f"codi_state: 状態ファイルが存在しません ({path})")


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: python core/state.py TASK-ID [init|complete STEP|get|delete]", file=sys.stderr)
        sys.exit(1)

    task_id = sys.argv[1].upper()
    action = sys.argv[2]

    if action == "init":
        init(task_id)
    elif action == "complete":
        if len(sys.argv) < 4:
            print("usage: python core/state.py TASK-ID complete STEP", file=sys.stderr)
            sys.exit(1)
        complete(task_id, sys.argv[3])
    elif action == "get":
        get(task_id)
    elif action == "delete":
        delete(task_id)
    else:
        print(f"エラー: 不明なアクション '{action}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
