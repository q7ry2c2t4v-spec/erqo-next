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
DOCS_DIR_NAME = "docs"
STARTER_DIR_NAME = "starter"
STACKS_DIR_NAME = "stacks"  # variant 別装備のルートディレクトリ名

# specs/ サブディレクトリ
CODING_DIR_NAME = "coding"

# --- .libs/ 配下の棚名 ---

STORYBOOK_SHELF_NAME = "storybook"
LIBS_SHELVES = [
    "design", "features", "research", "rules", "session-logs",
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

# --- コーディングルール分割ファイル ---
# specs/06-coding-rules.md (ハブ) と specs/coding/ 配下の層別ファイル。
# core/coding_rules.py がファイルパスから適用ルールを機械判定する。

CODING_HUB_FILENAME = "06-coding-rules.md"
CODING_L2_PYTHON_FILENAME = "l2-python.md"
CODING_L2_TYPESCRIPT_FILENAME = "l2-typescript.md"
CODING_L3_NEXTJS_FILENAME = "l3-nextjs.md"
CODING_L3_CLOUDFLARE_FILENAME = "l3-cloudflare.md"

# --- OS specs ファイル一覧 ---
# 本元 CLAUDE.md (手動維持) と プロジェクト CLAUDE.md (install.py が生成) の
# 両方が @import する specs/ 直下の Markdown 一覧。
# specs の追加・削除はこの一覧を更新するだけでプロジェクト側は自動追従する
# (本元 CLAUDE.md は手動で揃える)。この定数が唯一の正本。

OS_SPECS_FILES = (
    "00-identity.md",
    "01-workflow.md",
    "02-skills.md",
    "03-tools.md",
    "04-project-guide.md",
    "05-session.md",
    "06-coding-rules.md",
    "07-scopes.md",
    "08-responsibility.md",
    "09-memory.md",
    "10-proposal.md",
)

# 既存 CLAUDE.md を同期するときに目印にする見出し
# (install.py:_sync_os_imports_in_claude_md が使う)
OS_SECTION_HEADING = "## erqo-next OS"

# PROJECT-SERVERS 照合 Hook (project_servers_hook.py) が参照するページのパス
# (プロジェクトルート相対、specs/07-scopes.md 外部サーバー操作のプロジェクト境界)
PROJECT_SERVERS_PAGE_REL = ".libs/design/project-spec/servers.md"

# --- ファイル名パターン ---

TP_FILE_PATTERN = "tp-*.md"
SESSION_LOG_PATTERN = "slog-*.md"
STATE_FILE_PREFIX = "codi_"

# --- 本元 (エル子) でのスキル除外は SKILL.md フロントマター `target: project` で宣言する ---
# かつては SOURCE_EXCLUDED_SKILLS 定数でハードコしていたが、`skills/<name>/SKILL.md`
# の frontmatter が唯一の正本になった。install.py:_scan_skills() が各 SKILL.md を
# 読んで target を解釈する。ここに定数は置かない (追従忘れ防止)。

# --- インストール時の生成物 ---

QA_CONFIG_TEMPLATES = ["eslint.config.mjs", "playwright.config.ts", "lighthouserc.js"]

DEFAULT_GITIGNORE_LINES = [
    ".claude/state/",
    ".claude/settings.local.json",
    "node_modules/",
    ".next/",
    "storybook-static/",
    "test-results/",
    "playwright-report/",
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

# --- baseline: VRT 基準スクショ自動取得 ---
# cmd_baseline が baseline.mjs を呼び出し、Storybook ストーリーの基準スクショを撮影する。
# Storybook が起動していなければ自動起動 → 撮影 → 停止する。

BASELINE_NODE_SCRIPT_FILENAME = "baseline.mjs"
BASELINE_NODE_TIMEOUT_SEC = 180
BASELINE_OUTPUT_DIR_NAME = "baseline"
BASELINE_STORYBOOK_PORT = 6099
BASELINE_SCREENSHOT_PREFIX = "baseline-"

# --- recon: アニメーションライブラリ検出 / スクロールサンプリング / アセット取得 ---
# 検出パターン DB は recon.mjs (Node) と clone.py (Python) の両方から参照するため、
# core/clone_node/anim_lib_patterns.json を SSOT とする。編集はこの JSON 1 箇所のみ。
# RSRC-WEBANIM-CAPTURE §技術詳細 1 "ライブラリ同定" に準拠。

ANIM_LIB_PATTERNS_FILENAME = "anim_lib_patterns.json"

# スクロール連動サンプリング (ページ高さを何段階で sweep するか)
# RSRC-WEBANIM-CAPTURE §技術詳細 6 "スクロール連動マッピングの抽出"
SCROLL_SAMPLING_STEPS = 120

# スクロール連動の観察対象セレクタ (recon.mjs へ CLI 引数で渡す)
# 採用基準: 意味タグ + アニメ命名の慣用クラス。過不足は recon 結果で調整する。
SCROLL_TRACKED_SELECTORS = (
    "[data-anim]",
    "section",
    "[class*=parallax]",
    "[class*=reveal]",
    "[class*=sticky]",
    "[class*=fade]",
    "[class*=slide]",
)

# --- recon: Lottie / Rive 自動検出 ---
# page.on('response') で拾うレスポンス URL / コンテンツのパターン。
# recon.mjs は内部定数として同じ regex を 1 度だけ使う (L1 §1.4 例外)。
# Lottie 判定: レスポンス JSON に "v" と "layers" が含まれるか (BodyMovin 形式)
# Rive 判定: 拡張子 .riv またはマジックバイト "RIVE"

RECON_ASSETS_DIR_NAME = "assets"
SCROLL_SAMPLES_FILENAME = "scroll-samples.json"

# --- diff: 元サイト vs 再現の差分検証 (段階 1: レポートのみ、自動修正は段階 5) ---
DIFF_NODE_SCRIPT_FILENAME = "diff.mjs"
DIFF_NODE_TIMEOUT_SEC = 60
DIFF_OUTPUT_DIR_NAME = "diff"
DIFF_IMAGE_PREFIX = "diff-"
DIFF_RESULT_FILENAME = "diff-result.json"
# pixelmatch の色差許容 (0.0=完全一致, 1.0=全許容)
DIFF_PIXELMATCH_THRESHOLD = 0.1
# 「再現度不足」と features ページに記録する上限差分率
DIFF_MAX_MISMATCH_RATIO = 0.05

# --- 段階 2: WebGL / シェーダ取材 (Spector.js 組み込み) ---
# RSRC-WEBANIM-HARDCASE §1 "WebGL 完全取材 — Spector.js 統合" に準拠。
# recon.mjs が collectReport 内で hasWebGL を判定し、true のときだけ
# core/clone_node/spector.mjs の captureWebGLShaders を呼んで
# programs[*].shaders.{vertex,fragment}.source を shaders.json に保存する。
# capture に失敗しても recon 全体は止めない (HARDCASE §1 の「9 割再現」方針)。

WEBGL_OUTPUT_DIR_NAME = "webgl"
WEBGL_SHADERS_FILENAME = "shaders.json"

# --- 段階 3: 背景動画アセット DL + 時間偽装 (決定的 recon) ---
# RSRC-WEBANIM-HARDCASE §2 "rAF 時間偽装法" / §5 "Lottie/Rive" の動画拡張に準拠。
# recon.mjs の --deterministic で core/clone_node/time-virtualize.mjs を addInitScript し、
# Date / performance.now / requestAnimationFrame / setTimeout / setInterval を仮想時計に
# 差し替えて決定的なフレーム取材を行う。背景動画は page.on('response') で .mp4/.webm/.ogg
# を自動 DL し、clone.py の _format_video_section が本棚ページに埋める。

VIDEO_EXTENSIONS = (".mp4", ".webm", ".ogg")
# 仮想時計の 1 ステップ (ms)。60fps 相当で起動後の初期アニメーションを進める。
DETERMINISTIC_STEP_MS = 16
# 起動後にウォームアップ目的で進めるフレーム数 (= 約 1 秒分)。
DETERMINISTIC_WARMUP_FRAMES = 60

# --- 段階 4: rrweb 型 DOM 時系列記録 ---
# RSRC-WEBANIM-HARDCASE §3 "rrweb 型 DOM 時系列記録" に準拠。
# recon.mjs が rrweb-record.mjs 経由で UMD バンドルを addInitScript で注入し、
# 取材シナリオ中の Mutation / scroll / mousemove / input を
# `.libs/storybook/<slug>/recon/site-<i>/rrweb.json` に保存する。
# clone.py の _format_rrweb_section が本棚ページに「動きの時系列記録」セクションを追加する。
# 未インストールの環境では recon は rrweb をスキップして続行する (警告のみ)。

RRWEB_OUTPUT_FILENAME = "rrweb.json"
# 本棚ページに埋め込む冒頭イベントのプレビュー数 (巨大な events 全文は埋めない)
RRWEB_MAX_EVENTS_PREVIEW = 10


# --- コーディングルール判定 (coding_rules.py) ---
# ファイル拡張子からカテゴリを機械判定するための定数。
# AI の自己判断を排除する (specs/08-responsibility.md)。

PYTHON_FILE_EXTENSIONS = (".py",)
TYPESCRIPT_FILE_EXTENSIONS = (".ts", ".tsx", ".mts", ".cts")

# プロジェクトルート直下にあれば Next.js プロジェクトと判定するマーカー
NEXTJS_MARKER_FILES = (
    "next.config.ts",
    "next.config.mjs",
    "next.config.js",
)

# プロジェクトルート直下にあれば Cloudflare Workers プロジェクトと判定するマーカー
CLOUDFLARE_MARKER_FILES = (
    "wrangler.jsonc",
    "wrangler.json",
    "wrangler.toml",
)

# パス部に含まれていれば Cloudflare Workers と判定するディレクトリ名
WORKERS_DIR_NAME = "workers"

# --- coding_rules_hook.py: PreToolUse 出力フォーマット ---
# Hook が stderr に出すメッセージ。L2/L3 が増えた時 (= L1 だけでない時) のみ
# 出力する。L1 のみ (=コードでない) なら何も出さない (ノイズ防止)。

CODING_RULES_HOOK_HEADER = (
    "## 適用コーディングルール (実装前に必ず Read してください)"
)
CODING_RULES_HOOK_FOOTER = (
    "詳細: specs/06-coding-rules.md §0 適用マトリックス / specs/08-responsibility.md"
)

# --- variant (プル子 / プタ子 の識別子) ---
# プロジェクトの .claude/state/variant.json に保存される印の値。
# 本元 (IS_SOURCE) では variant 概念を使わない (read_variant が VARIANT_DEFAULT を返す)。
# 印がないプロジェクトは既存プル子として扱う (後方互換)。
# SKILL.md frontmatter の variant: も同じ値空間 (+ VARIANT_BOTH) を使う。

VARIANT_NEXTJS = "nextjs"     # プル子 (Next.js プロジェクト、/layo 付き)
VARIANT_GENERIC = "generic"   # プタ子 (任意スタック、/layo 非配布)
VARIANT_BOTH = "both"         # SKILL.md frontmatter での「両対応」
VARIANTS = (VARIANT_NEXTJS, VARIANT_GENERIC)  # 印の有効値
VARIANT_DEFAULT = VARIANT_NEXTJS              # 印なし時のフォールバック (既存プル子互換)

# .claude/state/variant.json のファイル名と鍵
VARIANT_FILE_NAME = "variant.json"
VARIANT_JSON_KEY = "variant"

# SKILL.md frontmatter の鍵
SKILL_FRONTMATTER_TARGET_KEY = "target"
SKILL_FRONTMATTER_VARIANT_KEY = "variant"

# --- 外部 URL ---

ERQO_REPO_URL = "https://github.com/q7ry2c2t4v-spec/erqo-next.git"

# --- セッション関連の数値 ---

VERSION_CHECK_INTERVAL_SEC = 86400  # 1日
MAX_CONTEXT_LENGTH = 10000
SESSION_LOG_PREVIEW_LINES = 30
