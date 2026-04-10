"""paths.py — パス解決モジュール

上方向探索で CLAUDE.md を見つけてプロジェクトルートを特定する。
全モジュール・スキルが共通で使うパス定数を提供する。
"""

from pathlib import Path

# NXT_ROOT: core/ の親ディレクトリ（nxt 本元ではリポジトリルート、PJ では .nxt-core/）
NXT_ROOT = Path(__file__).resolve().parent.parent


def find_project_root() -> Path | None:
    """CLAUDE.md を上方向探索してプロジェクトルートを特定する。"""
    current = Path(__file__).resolve().parent
    while current != current.parent:
        if (current / "CLAUDE.md").exists():
            return current
        current = current.parent
    return None


PROJECT_ROOT = find_project_root()

# nxt 本元/PJ 判定
IS_SOURCE = PROJECT_ROOT is not None and NXT_ROOT == PROJECT_ROOT

# 派生パス
LIBS_DIR = PROJECT_ROOT / ".libs" if PROJECT_ROOT else None
STATE_DIR = PROJECT_ROOT / ".claude" / "state" if PROJECT_ROOT else None
INDEX_FILE = STATE_DIR / "_index.json" if STATE_DIR else None
SPECS_DIR = NXT_ROOT / "specs"

# .libs/ サブディレクトリ
DESIGN_DIR = LIBS_DIR / "design" if LIBS_DIR else None
FEATURES_DIR = LIBS_DIR / "features" if LIBS_DIR else None
RULES_DIR = LIBS_DIR / "rules" if LIBS_DIR else None
DOCS_DIR = LIBS_DIR / "docs" if LIBS_DIR else None
LOGS_DIR = LIBS_DIR / "session-logs" if LIBS_DIR else None

# プロジェクト派生パス
UI_SPECS_DIR = PROJECT_ROOT / ".ui-specs" if PROJECT_ROOT else None
VERSION_FILE = NXT_ROOT / "VERSION"
