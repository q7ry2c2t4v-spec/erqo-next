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

STORYBOOK_SHELF_NAME = "storybook"
LIBS_SHELVES = [
    "design", "features", "docs", "research", "rules", "session-logs",
    STORYBOOK_SHELF_NAME, "archive",
]

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

# --- 本元（IS_SOURCE）でのみ除外するスキル ---
# プロジェクト側には引き続き全スキルが配信される。
# 本元では使う場面がないスキルをここに列挙し、_scan_skills() がフィルタする。

SOURCE_EXCLUDED_SKILLS = frozenset({"dsgn", "tp", "codi"})

# --- インストール時の生成物 ---

QA_CONFIG_TEMPLATES = ["eslint.config.mjs", "playwright.config.ts", "lighthouserc.js"]

DEFAULT_GITIGNORE_LINES = [
    ".claude/state/",
    ".claude/settings.local.json",
    "node_modules/",
    ".next/",
]

# --- 自動ステージング時のブラックリスト ---
# stage_ops.py がコミット候補から機械的に除外するパス。
# .gitignore に書いてあれば git status から消えるが、追跡済みファイルや
# 設計上 .gitignore に入れない一時ファイルを念のため二重で弾く。
# プロジェクトルートからの相対パス前方一致でマッチさせる。

STAGE_BLACKLIST_PREFIXES = (
    ".claude/state/",
    ".claude/settings.local.json",
    ".commit_msg_tmp.txt",
)

# --- Claude Code 保護パス ---
# Claude Code は以下を「保護パス」として扱い、bypassPermissions モードでも
# 書き込み時に確認プロンプトを出す。設定による無効化は存在しない。
# write_guard.py が PreToolUse Hook 経由で事前ブロックするための定数。
# 例外サブディレクトリ (commands/agents/skills/worktrees) は書き込み許可される。
# プロジェクトルートからの相対パス前方一致でマッチさせる。

PROTECTED_PATH_PREFIXES = (
    ".git/",
    ".claude/",
)

PROTECTED_PATH_EXCEPTIONS = (
    ".claude/commands/",
    ".claude/agents/",
    ".claude/skills/",
    ".claude/worktrees/",
)

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

# --- UI / レイアウト判定キーワード ---
# load.py の _judge_ui / _judge_layout がスコアリングで参照する。
# LAYOUT は UI のサブタイプ (layout ⊂ ui) — LAYOUT_ID_PATTERNS の語は
# UI_ID_PATTERNS にも含め、レイアウトタスクが UI 判定でも true になるようにする。

UI_ID_PATTERNS = ["UI", "CARD", "VIEWER", "THEME", "COLOR", "LAYOUT", "NAV", "PAGE"]
UI_TAG_KEYWORDS = ["ui", "コンポーネント", "レイアウト", "画面", "component", "layout", "page"]

LAYOUT_ID_PATTERNS = ["LAYOUT", "PAGE", "CLONE", "DESIGN"]
LAYOUT_TAG_KEYWORDS = [
    "クローン", "再現", "レイアウト", "デザイン",
    "clone", "layout", "design", "ui-clone",
]

# --- レイアウトサブパイプラインのサブステップ ---
# /codi ステップ 2 (implementation) がレイアウトタスクの場合に展開する 7 サブステップ。
# 詳細: .libs/research/webclone/rsrc-webclone-codi-integration.md

LAYOUT_SUBSTEPS = [
    "recon",      # 1. 取材 (Playwright CLI で参考サイトから取得)
    "dump",       # 2. 本棚化 (.libs/storybook/ に下書き)
    "apply",      # 3. 要望適用 (元サイト < 要望)
    "rules",      # 4. ルール適用 (ハードコ禁止 / iOS / Tailwind v4)
    "build",      # 5. 部品実装 (.tsx + .stories.tsx 生成)
    "assemble",   # 6. ページ統合 (page.tsx + SEO)
    "baseline",   # 7. VRT 基準作成 (pixel-perfect 基準スクショ)
]

# --- レイアウトサブパイプラインの入力ファイル ---
# .libs/storybook/<task-slug>/input.md に置かれる取材入力。
# 「本棚ページが正本」原則 (RSRC-WEBCLONE-CODI-INTEGRATION 決定事項 3) に基づき、
# 参考サイト URL / 要望 / メモを 1 ファイルに集約する。

STORYBOOK_INPUT_FILENAME = "input.md"
RECON_REFERENCE_SECTION_SUFFIX = ".参考サイト"
RECON_REQUEST_SECTION_SUFFIX = ".要望"
RECON_NOTE_SECTION_SUFFIX = ".メモ"

# --- recon: Playwright / Node スクリプト取材 ---
# `.libs/storybook/<task-slug>/recon/` 配下に取材成果物を配置する。
# 複数 URL のときは site-1 / site-2 ... のサブディレクトリに分けて保存する。

RECON_OUTPUT_DIR_NAME = "recon"
RECON_SITE_DIR_PREFIX = "site-"
RECON_DESKTOP_VIEWPORT = (1440, 900)
RECON_MOBILE_VIEWPORT = (390, 844)
RECON_SCREENSHOT_DESKTOP_FILENAME = "screenshot-desktop.png"
RECON_SCREENSHOT_MOBILE_FILENAME = "screenshot-mobile.png"
RECON_JSON_DESKTOP_FILENAME = "recon-desktop.json"
RECON_JSON_MOBILE_FILENAME = "recon-mobile.json"
RECON_PLAYWRIGHT_TIMEOUT_SEC = 60
RECON_NODE_TIMEOUT_SEC = 120

# recon で取材する解像度のリスト。(名前, viewport, screenshot ファイル名, JSON ファイル名) の順。
# 将来 tablet 等を追加する場合はこのリストに行を足すだけで拡張できる。
RECON_VIEWPORTS = [
    ("desktop", RECON_DESKTOP_VIEWPORT,
     RECON_SCREENSHOT_DESKTOP_FILENAME, RECON_JSON_DESKTOP_FILENAME),
    ("mobile",  RECON_MOBILE_VIEWPORT,
     RECON_SCREENSHOT_MOBILE_FILENAME,  RECON_JSON_MOBILE_FILENAME),
]

# --- recon: Node スクリプト (clone_node) 配置 ---
# core/ 直下を Python のみに保つため、.mjs ファイルはサブディレクトリに置く。
# giget 配布で .nxt-core/core/clone_node/ に自動でコピーされる。

RECON_NODE_DIR_NAME = "clone_node"
RECON_NODE_SCRIPT_FILENAME = "recon.mjs"

# --- recon: テキストだけモード ---
# input.md に参考 URL がゼロでも要望セクションがあれば続行する。
# 本棚ページの雛形は dump 段階で生成し、recon は「URL なしで完了」扱いで抜ける。

RECON_TEXT_ONLY_MARKER_FILENAME = "text-only.json"

# --- 外部 URL ---

ERQO_REPO_URL = "https://github.com/q7ry2c2t4v-spec/erqo-next.git"

# --- セッション関連の数値 ---

VERSION_CHECK_INTERVAL_SEC = 86400  # 1日
MAX_CONTEXT_LENGTH = 10000
SESSION_LOG_PREVIEW_LINES = 30
