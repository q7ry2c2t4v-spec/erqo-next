"""feedback.py — エラー報告・フィードバック送信モジュール

未処理エラーの自動キャッチ、明示的エラーレポート、
汎用フィードバック送信、一時的エラーの自動リトライを提供する。
"""

import json
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

from paths import VERSION_FILE, FEEDBACK_DIR


def _get_nxt_version() -> str:
    """VERSION ファイルからバージョン文字列を読み取る。"""
    version_file = VERSION_FILE
    if version_file.exists():
        return version_file.read_text(encoding="utf-8").strip()
    return "unknown"


def _feedback_dir() -> Path:
    """フィードバック保存ディレクトリを返す（なければ作成）。"""
    FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
    return FEEDBACK_DIR


def _save_report(data: dict) -> Path:
    """レポートを JSON ファイルとして保存する。"""
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = _feedback_dir() / f"{data['kind']}-{ts}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def report_error(exc: BaseException) -> Path:
    """明示的エラーレポートを保存する。"""
    data = {
        "kind": "error",
        "summary": str(exc),
        "detail": traceback.format_exception(type(exc), exc, exc.__traceback__),
        "version": _get_nxt_version(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return _save_report(data)


def send_feedback(kind: str, summary: str, detail: str = "") -> Path:
    """汎用フィードバックを保存する。

    保存後、erqo-feedback 共有リポジトリへの push も試みる (失敗は警告のみ)。
    本元では push せず保存のみ (本元は /fb を持たない設計)。
    """
    data = {
        "kind": kind,
        "summary": summary,
        "detail": detail,
        "version": _get_nxt_version(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    path = _save_report(data)
    # 共有リポジトリへの push は best-effort (循環 import 回避のため遅延 import)
    try:
        from feedback_sync import push_report
        push_report(path)
    except Exception as exc:  # noqa: BLE001 (degraded mode: 失敗時は警告のみ)
        print(f"[feedback] erqo-feedback への push をスキップ: {exc}", file=sys.stderr)
    return path


def init_error_handling() -> None:
    """sys.excepthook を上書きし、未処理エラーを自動キャッチする。"""

    def _hook(exc_type, exc_value, exc_tb):
        if exc_type is KeyboardInterrupt:
            sys.__excepthook__(exc_type, exc_value, exc_tb)
            return
        report_error(exc_value)
        sys.__excepthook__(exc_type, exc_value, exc_tb)

    sys.excepthook = _hook


def with_retry(func, max_retries: int = 3, delay: float = 1.0):
    """一時的エラーの自動リトライ（最大 max_retries 回）。"""
    last_exc = None
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as exc:
            last_exc = exc
            if attempt < max_retries - 1:
                time.sleep(delay)
    raise last_exc
