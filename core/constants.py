"""constants.py — エル子の固定値定数

パス以外の固定値を一元管理する。パス（Path オブジェクト）は paths.py 側。

このモジュールは他の core モジュールに依存しない（循環 import 防止）。
"""

# --- プロジェクト構造ディレクトリ名 ---

CLAUDE_DIR_NAME = ".claude"
LIBS_DIR_NAME = ".libs"
UI_SPECS_DIR_NAME = ".ui-specs"
STATE_DIR_NAME = "state"
SKILLS_DIR_NAME = "skills"
SCRIPTS_DIR_NAME = "scripts"
SPECS_DIR_NAME = "specs"
TEMPLATES_DIR_NAME = "templates"
FEEDBACK_DIR_NAME = "feedback"
HISTORY_DIR_NAME = "history"

# --- .libs/ 配下の棚名 ---

LIBS_SHELVES = ["design", "features", "docs", "research", "rules", "session-logs", "archive"]

# --- ファイル名 ---

CLAUDE_MD_FILENAME = "CLAUDE.md"
SKILL_MD_FILENAME = "SKILL.md"
INDEX_MD_FILENAME = "index.md"
SETTINGS_FILENAME = "settings.json"
GITIGNORE_FILENAME = ".gitignore"
VERSION_FILENAME = "VERSION"
INDEX_FILENAME = "_index.json"
OS_SKILLS_FILENAME = "_os_skills.json"
VERSION_CHECK_FILENAME = "_version_check.json"
TAG_ALIASES_FILENAME = "tag_aliases.json"

# --- ファイル名パターン ---

TP_FILE_PATTERN = "tp-*.md"
SESSION_LOG_PATTERN = "slog-*.md"
STATE_FILE_PREFIX = "codi_"

# --- インストール時の生成物 ---

QA_CONFIG_TEMPLATES = ["eslint.config.mjs", "playwright.config.ts", "lighthouserc.js"]

DEFAULT_GITIGNORE_LINES = [
    ".claude/state/",
    ".claude/settings.local.json",
    "node_modules/",
    ".next/",
]

# --- 共通 permission 設定（本元・プロジェクト両方に適用） ---

PERMISSION_DEFAULTS_ALLOW = ["Bash", "Edit", "Write", "Read"]
PERMISSION_DEFAULTS_MODE = "bypassPermissions"

# --- TP テーブルのステータス文字列 ---

STATUS_DONE = "完了"
STATUS_TODO = "未着手"
STATUS_WIP = "進行中"

# --- /codi パイプラインのステップ ---

PIPELINE_STEPS = [
    "prepare",        # 1. 準備（タスク読み込み + コンテキスト収集）
    "implementation", # 2. 実装
    "verification",   # 3. 検証
    "recording",      # 4. 記録（features + ステータス + ガイド）
    "commit",         # 5. コミット
]

# --- 外部 URL ---

ERQO_REPO_URL = "https://github.com/q7ry2c2t4v-spec/erqo-next.git"

# --- セッション関連の数値 ---

VERSION_CHECK_INTERVAL_SEC = 86400  # 1日
MAX_CONTEXT_LENGTH = 10000
SESSION_LOG_PREVIEW_LINES = 30
