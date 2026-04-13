"""variant.py — プル子 / プタ子 の識別子を読み書きする。

プロジェクトの .claude/state/variant.json を SSOT とする印を、スクリプトが
機械的に読み書きする。AI の自己判断は挟まない (specs/08-responsibility.md)。

設計方針:
- 本元 (IS_SOURCE) では variant 概念を使わない (常に VARIANT_DEFAULT 扱い)
- 印がないプロジェクトは VARIANT_DEFAULT (nextjs) に倒す (既存プル子の後方互換)
- 不正な値が書かれていた場合も VARIANT_DEFAULT に倒す

このモジュールは Python 標準ライブラリのみを使う (本元 core の制約)。
"""

import json

from constants import VARIANT_DEFAULT, VARIANT_JSON_KEY, VARIANTS
from paths import IS_SOURCE, STATE_DIR, VARIANT_FILE


def read_variant() -> str:
    """プロジェクトの variant を返す。

    本元 (IS_SOURCE) では常に VARIANT_DEFAULT。
    プロジェクトで印がない・読み込み失敗・不正値なら VARIANT_DEFAULT にフォールバック。
    """
    if IS_SOURCE or VARIANT_FILE is None or not VARIANT_FILE.exists():
        return VARIANT_DEFAULT
    try:
        data = json.loads(VARIANT_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError, UnicodeDecodeError):
        return VARIANT_DEFAULT
    value = data.get(VARIANT_JSON_KEY)
    if value in VARIANTS:
        return value
    return VARIANT_DEFAULT


def write_variant(value: str) -> None:
    """variant.json に印を書き込む。

    本元で呼ばれたら何もしない (variant 概念を使わないため)。
    VARIANTS にない値を渡されたら ValueError を raise (呼び出し元のバグ)。
    """
    if IS_SOURCE:
        return
    if value not in VARIANTS:
        raise ValueError(f"invalid variant: {value!r} (expected one of {VARIANTS})")
    if VARIANT_FILE is None or STATE_DIR is None:
        return
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    VARIANT_FILE.write_text(
        json.dumps({VARIANT_JSON_KEY: value}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
