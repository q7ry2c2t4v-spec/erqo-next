"""state.py - /codi パイプラインの状態管理

状態ファイルの作成・更新・読取・削除を行う。
atomic write (fsync + rename) で中断安全性を保証する。

レイアウトタスク (LAYOUT-* / PAGE-* / CLONE-* / DESIGN-*) は自動的に
サブステップ追跡フィールド (layout_substep / completed_substeps) を
状態ファイルに持つ。完了は `complete_substep` で記録する。

使い方:
    python .nxt-core/core/state.py TASK-ID init
    python .nxt-core/core/state.py TASK-ID complete STEP
    python .nxt-core/core/state.py TASK-ID complete_substep SUBSTEP
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
    LAYOUT_ID_PATTERNS,
    LAYOUT_SUBSTEPS,
)
from page_parser import parse_tp_row
from feedback import init_error_handling

init_error_handling()


def _state_file(task_id: str) -> Path:
    """状態ファイルのパスを返す。"""
    return STATE_DIR / f"{STATE_FILE_PREFIX}{task_id}.json"


def _is_layout_task(task_id: str) -> bool:
    """task_id の ID パターンから機械的にレイアウトタスクかを判定する。

    load.py の _judge_layout はタグも参照するが、state.py は IS_SOURCE でも
    動く必要があるので ID パターン検査のみ。LAYOUT-* / PAGE-* / CLONE-* /
    DESIGN-* 規約で運用する前提。
    """
    segments = task_id.split("-")
    return any(seg.upper() in LAYOUT_ID_PATTERNS for seg in segments)


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
    """パイプライン開始時に状態ファイルを作成する。

    task_id がレイアウトタスク (LAYOUT-* / PAGE-* / CLONE-* / DESIGN-*) なら
    layout_substep / completed_substeps フィールドも初期化する。
    """
    path = _state_file(task_id)
    is_layout = _is_layout_task(task_id)

    # 既存の状態ファイルがあれば中断復旧モード
    existing = _read_state(task_id)
    if existing:
        completed = existing.get("completed_steps", [])
        step_num = len(completed)
        print("codi_state: 既存の状態ファイルを検出 (中断復旧)")
        print(f"  完了済み: {', '.join(completed) if completed else 'なし'}")
        print(f"  次のステップ: {PIPELINE_STEPS[step_num] if step_num < len(PIPELINE_STEPS) else '全完了'}")
        if "layout_substep" in existing:
            completed_subs = existing.get("completed_substeps", [])
            current_sub = existing.get("layout_substep")
            print(
                f"  レイアウトサブステップ: {current_sub or '全完了'} "
                f"(完了済み: {', '.join(completed_subs) if completed_subs else 'なし'})"
            )
        print(json.dumps(existing, ensure_ascii=False))
        return

    # 依存タスク完了チェック
    incomplete = check_deps(task_id)
    if incomplete:
        print(f"codi_state: 警告 - 未完了の依存タスクがあります: {', '.join(incomplete)}")

    state: dict = {
        "task_id": task_id,
        "current_step": 1,
        "completed_steps": [],
        "started_at": _now_iso(),
        "last_update": _now_iso(),
    }

    if is_layout:
        state["layout_substep"] = LAYOUT_SUBSTEPS[0]
        state["completed_substeps"] = []

    _atomic_write_json(path, state)
    print(f"codi_state: 状態ファイル作成 -> {path}")
    if is_layout:
        print(
            f"  レイアウトタスク: サブステップ追跡を有効化 "
            f"(開始: {LAYOUT_SUBSTEPS[0]})"
        )


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


def complete_substep(task_id: str, substep_name: str) -> None:
    """レイアウトタスクのサブステップ完了を記録する。

    completed_substeps に追加し、layout_substep を次のサブステップに進める。
    最後のサブステップが完了したら layout_substep は None になる。
    """
    if substep_name not in LAYOUT_SUBSTEPS:
        print(f"エラー: 不明なサブステップ '{substep_name}'", file=sys.stderr)
        print(f"有効なサブステップ: {', '.join(LAYOUT_SUBSTEPS)}", file=sys.stderr)
        sys.exit(1)

    state = _read_state(task_id)
    if state is None:
        print(
            f"エラー: {task_id} の状態ファイルがありません。先に init してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    if "layout_substep" not in state:
        print(
            f"エラー: {task_id} はレイアウトタスクとして init されていません。"
            "(ID に LAYOUT/PAGE/CLONE/DESIGN のいずれかを含める必要があります)",
            file=sys.stderr,
        )
        sys.exit(1)

    completed = state.get("completed_substeps", [])
    if substep_name not in completed:
        completed.append(substep_name)
    state["completed_substeps"] = completed

    # 次の substep を設定 (最後のサブステップが完了したら None)
    idx = LAYOUT_SUBSTEPS.index(substep_name)
    if idx + 1 < len(LAYOUT_SUBSTEPS):
        state["layout_substep"] = LAYOUT_SUBSTEPS[idx + 1]
    else:
        state["layout_substep"] = None

    state["last_update"] = _now_iso()
    _atomic_write_json(_state_file(task_id), state)
    print(
        f"codi_state: layout サブステップ {substep_name} 完了 "
        f"({len(completed)}/{len(LAYOUT_SUBSTEPS)})"
    )
    if state["layout_substep"]:
        print(f"  次のサブステップ: {state['layout_substep']}")
    else:
        print("  全サブステップ完了")


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
        print(
            "usage: python core/state.py TASK-ID "
            "[init|complete STEP|complete_substep SUB|get|delete]",
            file=sys.stderr,
        )
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
    elif action == "complete_substep":
        if len(sys.argv) < 4:
            print(
                "usage: python core/state.py TASK-ID complete_substep SUBSTEP",
                file=sys.stderr,
            )
            sys.exit(1)
        complete_substep(task_id, sys.argv[3])
    elif action == "get":
        get(task_id)
    elif action == "delete":
        delete(task_id)
    else:
        print(f"エラー: 不明なアクション '{action}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
