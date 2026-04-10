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

from paths import STATE_DIR, VERSION_FILE


def _get_nxt_version() -> str:
    """VERSION ファイルからバージョン文字列を読み取る。"""
    version_file = VERSION_FILE
    if version_file.exists():
        return version_file.read_text(encoding="utf-8").strip()
    return "unknown"


def _feedback_dir() -> Path:
    """フィードバック保存ディレクトリを返す（なければ作成）。"""
    d = STATE_DIR / "feedback"
    d.mkdir(parents=True, exist_ok=True)
    return d


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
    """汎用フィードバックを保存する。"""
    data = {
        "kind": kind,
        "summary": summary,
        "detail": detail,
        "version": _get_nxt_version(),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return _save_report(data)


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
