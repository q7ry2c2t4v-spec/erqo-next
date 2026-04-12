# スクリプトリファレンス

## 構成

本元リポジトリでは下記ツリーが**ルート直下**にあり、プロジェクトでは `.nxt-core/` 配下にある。以下では場所に依存しない形で記載する。

```
core/          ← コアモジュール（全スクリプトの土台）
├── constants.py           ← 固定値の一元管理
├── paths.py               ← パス定数（constants 由来）
├── feedback.py
├── page_parser.py
├── index.py
├── docs.py
├── install.py             ← プロジェクト用セットアップ
├── dev.py                 ← 本体リポジトリ用セットアップ（IS_SOURCE 限定）
├── git_ops.py             ← git 操作ヘルパー（/wrap, /codi, /aud 共通）
├── stage_ops.py           ← 自動ステージング（/wrap 用、ブラックリスト機械適用）
├── write_guard.py         ← PreToolUse Hook 用、保護パス書き込みを事前ブロック
├── coding_rules.py        ← コーディング規約の機械判定（編集前に必ず呼ぶ）
├── coding_rules_hook.py   ← PreToolUse Hook 用、編集前に適用ルールを stderr 通知
├── clone.py               ← /codi レイアウトタスク用 7 サブステップ実行
├── clone_node/            ← Node + Playwright サブプロジェクト（隔離）
│   └── recon.mjs          ←   参考サイト取材（スクショ + DOM/CSS 取得）
├── session.py
├── state.py
├── load.py
└── record.py

skills/        ← スキル定義（SKILL.md ＋ 必要に応じて handler.py）
└── fb/handler.py
```

## 編集ルール

- **本元リポジトリ:** `core/`, `skills/` を直接編集する（システム調整はこちらで行う）
- **プロジェクト:** `.nxt-core/core/`, `.nxt-core/skills/` は**読み取り専用**。プロジェクト固有のスクリプトは `scripts/` に作成する

## コアモジュール

### paths.py — パス解決

全モジュールの土台。上方向探索で CLAUDE.md を見つけてプロジェクトルートを特定する。

| 変数 | 内容 |
|---|---|
| `NXT_ROOT` | nxt のルートディレクトリ |
| `PROJECT_ROOT` | プロジェクトルート |
| `IS_SOURCE` | nxt 本体リポジトリかどうか |
| `LIBS_DIR` | `.libs/` のパス |
| `STATE_DIR` | `.claude/state/` のパス |
| `INDEX_FILE` | `_index.json` のパス |
| `SPECS_DIR` | `specs/` のパス |
| `DOCS_DIR` | `docs/` のパス (デザインリファレンス、NXT_ROOT 配下) |

### feedback.py — フィードバック

統合フィードバックモジュール。

- `init_error_handling()` — 未処理エラーを自動キャッチ → JSON 保存
- `report_error(exc)` — 明示的エラーレポート
- `send_feedback(kind, summary, detail)` — 汎用フィードバック送信
- `with_retry(func)` — 一時的エラーの自動リトライ（最大3回）

### page_parser.py — ページ解析

- `parse_header(text)` — H1 + 関連 + タグを抽出
- `parse_sections(text)` — セクション構造を抽出

### index.py — インデックス管理

| サブコマンド | 内容 |
|---|---|
| `python core/index.py reindex` | 全ページスキャン → `_index.json` 再生成 |
| `python core/index.py collect KW1 KW2` | キーワード検索 + 関連ページ BFS 収集 |
| `python core/index.py rename OLD NEW` | 識別コードリネーム（一括更新） |

### docs.py — デザインリファレンス検索

`docs/` 配下のデザインリファレンス (Apple HIG, shadcn, Tailwind, M3, Motion 等) を検索する。`layo.py` から呼ばれる。

| サブコマンド | 内容 |
|---|---|
| `python core/docs.py search KW1 KW2` | `docs/` 内キーワード検索 |
| `python core/docs.py list [category]` | カテゴリ・ファイル一覧 |
| `python core/docs.py show CAT PATH` | ファイル内容表示 |

### layo.py — レイアウトコンテキスト収集

`/layo` スキルのオーケストレーター。`load.py` と同じパターンで、スクリプトがコンテキストを機械収集する。

| コマンド | 内容 |
|---|---|
| `python core/layo.py TASK-ID` | モード判定 + input.md + docs 検索 + ルール + 関連ページを収集 |

### install.py — セットアップ

プロジェクト用。本体リポジトリでは `IS_SOURCE` ガードで止まる。

| コマンド | 内容 |
|---|---|
| `python core/install.py` | 新規インストール (8ステップ) |
| `python core/install.py --update` | アップデート (選択的更新) |

### dev.py — 本体リポジトリ向けセットアップ

本体リポジトリ専用。本体で `/wrap`, `/ret` などのスキルを使えるようにする。プロジェクトで実行するとエラー終了する。

| コマンド | 内容 |
|---|---|
| `python core/dev.py setup` | 初回: Hook + スキルコピー + マニフェスト |
| `python core/dev.py update` | スキルのみ再コピー |
| `python core/dev.py _sync` | PostToolUse Hook 内部用（stdin 経由） |

`install.py` の `setup_hooks` / `setup_skills` / `setup_os_skills_manifest` を再利用するため、ロジックは一元管理されている。

### git_ops.py — git 操作ヘルパー

`/codi` ステップ5、`/wrap`、`/aud`、手動の差分確認で使う git ラッパー。プロジェクト・本体リポジトリ両方で動く（IS_SOURCE ガードなし）。

| コマンド | 内容 |
|---|---|
| `python core/git_ops.py check` | 差分確認 |
| `python core/git_ops.py commit "msg"` | git add -A → commit |

push が必要な時は `git` を直接呼ぶ（`/wrap` がそうしている）。

### stage_ops.py — 自動ステージング

`/wrap` のステージングを機械化するスクリプト。`git status --short` で得た変更ファイルから `STAGE_BLACKLIST_PREFIXES`（`constants.py`）に該当するものを除外して `git add` する。AI が手動でファイル指定することを禁止し、`specs/08-responsibility.md` の「曖昧判断禁止」を実装する。

| コマンド | 内容 |
|---|---|
| `python core/stage_ops.py collect` | 対象を表示（dry-run、git add しない） |
| `python core/stage_ops.py stage` | 対象を実際に git add |

### write_guard.py — 保護パス書き込みガード

`PreToolUse` Hook から呼ばれる事前検証スクリプト。`Write` / `Edit` / `NotebookEdit` の実行直前に stdin で渡される JSON から `tool_input.file_path` を抽出し、`PROTECTED_PATH_PREFIXES`（`.git/`, `.claude/`、ただし `PROTECTED_PATH_EXCEPTIONS` の `commands/agents/skills/worktrees` は除外）に該当する場合は `exit 2` でブロックする。Claude Code の保護パス確認プロンプトが発生する前に AI 作業を止めて事故を防ぐ。

`CLAUDE_PROJECT_DIR` が無い・JSON が不正・プロジェクト外パス・例外発生などは全て fail-open（`exit 0`）で素通しする。

| 動作 | 終了コード |
|---|---|
| 保護パスへの書き込み検出 | `2` （ツール実行ブロック + stderr に日本語メッセージ） |
| 保護パス外 / 取得不能 / 例外 | `0` （素通し） |

### coding_rules.py — コーディング規約の機械判定

AI がコード編集前に必ず呼ぶスクリプト。ファイルパスから適用すべきルールファイル一覧（L1 ハブ + 該当する L2 / L3）を機械的に判定する。AI の自己判断は一切挟まない（`specs/08-responsibility.md`）。

判定ロジック:

- 常時: `specs/06-coding-rules.md`（L1 汎用共通ハブ）
- `.py`: + `specs/coding/l2-python.md`
- `.ts` / `.tsx` / `.mts` / `.cts`: + `specs/coding/l2-typescript.md`
  - プロジェクトルートに `next.config.ts|mjs|js` があれば: + `specs/coding/l3-nextjs.md`
  - プロジェクトルートに `wrangler.jsonc|json|toml` があるか、対象ファイルパスに `workers/` が含まれていれば: + `specs/coding/l3-cloudflare.md`

| コマンド | 内容 |
|---|---|
| `python core/coding_rules.py <file_path>` | 該当ルールファイル一覧を stdout に出力（1 行 1 ファイル） |

終了コード: 正常 `0` / 引数不正 `2` / ファイル未発見 `3`。詳細は `specs/06-coding-rules.md` §0 適用マトリックス。

### coding_rules_hook.py — 編集前ルール通知 Hook

`PreToolUse` Hook（matcher: `Write|Edit|NotebookEdit`）から呼ばれ、`coding_rules.get_applicable_rules()` を使って対象ファイルに適用されるルール一覧を **stderr に通知するだけ**。ブロックはしない（情報提供のみ、`exit 0`）。

- L1 のみ（コードでない `.md` 等）の場合は黙って終了
- L2 / L3 が含まれるとき（＝コードファイル）だけ stderr に「## 適用コーディングルール」ヘッダ + ファイル一覧を出力
- `file_path` 取得不能・JSON 不正・例外発生は fail-open（`exit 0`）
- 順序は同 matcher 内で `write_guard.py`（ブロック）→ `coding_rules_hook.py`（情報提供）

### clone.py — レイアウトサブパイプライン

`/codi` ステップ2 がレイアウトタスク（`LAYOUT-*` / `PAGE-*` / `CLONE-*` / `DESIGN-*`）の場合に呼ばれる 7 サブステップ実行スクリプト。本元リポジトリでは `/codi` 自体が使えないため、`clone.py` 単体での起動にも対応する（`IS_SOURCE` ガードなし）。

| サブコマンド | 内容 |
|---|---|
| `python core/clone.py recon TASK-ID` | 取材（Node + Playwright で参考サイトからスクショ + 6 項目取材） |
| `python core/clone.py dump TASK-ID` | 本棚化（`.libs/storybook/<slug>/<slug>.md` に下書き生成） |
| `python core/clone.py apply TASK-ID` | 要望適用（元サイト < 要望） |
| `python core/clone.py rules TASK-ID` | ルール適用（Tailwind v4 `@theme` トークン + iOS / ハードコ禁止） |
| `python core/clone.py build TASK-ID` | 部品実装指示（`.tsx` + `.stories.tsx` 雛形） |
| `python core/clone.py assemble TASK-ID` | ページ統合指示（`page.tsx` + Metadata + JSON-LD） |
| `python core/clone.py baseline TASK-ID` | VRT 基準スクショ（pixel-perfect `threshold:0`） |

各サブステップは `.libs/storybook/<slug>/<slug>.md` を正本にセクション単位で冪等置換する。`.tsx` / `page.tsx` の直接編集は禁止（修正は必ず `input.md` → `recon` / `apply` 経由）。

取材には `core/clone_node/recon.mjs`（Node + Playwright）が使われる。`clone.py` 本体は Python 標準ライブラリのみで書かれており、Node 依存は `clone_node/` サブディレクトリに隔離されている（`specs/coding/l2-python.md` §1 の本元ルール）。

#### アニメーション取材・再現の組み込み (段階 1 導入済)

RSRC-WEBANIM-{CAPTURE,REPLAY,HARDCASE} の基本セットを `clone.py` + `recon.mjs` + `diff.mjs` に組み込んだ:

- **recon 拡張**: `recon.mjs` が `detectLibs()` (ライブラリ同定) + `collectScrollSamples()` (120 分割サンプリング) + Lottie/Rive 自動 DL (`page.on('response')`) を実行する
- **検出パターン SSOT**: `core/clone_node/anim_lib_patterns.json` が `recon.mjs` と `clone.py` の共通パターン DB。追加・修正はこの JSON 1 箇所
- **新セクション 3 つ**: `_format_libraries_section` / `_format_scroll_mapping_section` / `_format_assets_section` が本棚ページに「採用ライブラリ」「スクロール連動マッピング」「アセット取材」を生成
- **build 雛形分岐**: `_detect_adopted_library()` が本棚ページと input.md から採用ライブラリを機械決定し、`_build_tsx_skeleton_motion / _gsap / _lenis / _r3f / _lottie` の 5 雛形を出し分ける (既定は従来の pure-CSS 雛形)
- **差分検証**: `cmd_baseline` 末尾で `_compare_recon_vs_baseline()` が `diff.mjs` (pixelmatch + pngjs) を呼び、元サイト vs 再現の差分率を `.libs/storybook/<slug>/diff/` に保存する。`record.py` が features ページに「再現度検証」セクションとして自動転記
- **一元定数**: `constants.py` の `ANIM_LIB_PATTERNS_FILENAME` / `SCROLL_SAMPLING_STEPS` / `SCROLL_TRACKED_SELECTORS` / `RECON_ASSETS_DIR_NAME` / `DIFF_*` が SSOT

段階 2〜5 (Spector.js / 時間偽装 / rrweb / Vision LLM / VRT 差分自動修正ループ) は別セッションで段階投入する。設計は `.libs/research/webanim/` の 3 ページに固定済み。

### clone_node/diff.mjs — 元サイト vs 再現の差分検証 (Node)

`cmd_baseline` が baseline スクショ撮影の直後に呼ぶ。`pixelmatch` + `pngjs` を使い、共通矩形にトリミングした上で差分画像を生成し、最終行に 1 行 JSON で `mismatchRatio` 等を返す契約。

| 引数 | 内容 |
|---|---|
| `--baseline` | 再現側 PNG (`.libs/storybook/<slug>/baseline/baseline-<vp>.png`) |
| `--reference` | 元サイト側 PNG (`.libs/storybook/<slug>/recon/site-1/screenshot-<vp>.png`) |
| `--output` | 差分画像の保存先 PNG |
| `--threshold` | pixelmatch 閾値 (既定: `constants.DIFF_PIXELMATCH_THRESHOLD`) |

プロジェクト側は `starter/package.json` に `pixelmatch` + `pngjs` を dep として宣言している (bootstrap.py 経由で自動インストール)。

### session.py — セッション管理

SessionStart Hook から呼ばれる。

| コマンド | 内容 |
|---|---|
| `python core/session.py` | 通常モード (7項目注入) |
| `python core/session.py --compact` | compact モード (3項目注入) |

### state.py — パイプライン状態

| コマンド | 内容 |
|---|---|
| `python core/state.py TASK-ID init` | 状態ファイル作成 + 依存チェック |
| `python core/state.py TASK-ID complete STEP` | ステップ完了記録 |
| `python core/state.py TASK-ID get` | 現在状態を JSON 出力 |
| `python core/state.py TASK-ID delete` | 状態ファイル削除 |

### load.py — タスク読み込み

| コマンド | 内容 |
|---|---|
| `python core/load.py TASK-ID` | タスク情報 + UI 判定 + コンテキスト収集 |

### record.py — 記録統合

| コマンド | 内容 |
|---|---|
| `python core/record.py TASK-ID` | features ページ作成 / FIX 準備 |
| `python core/record.py TASK-ID merge ...` | FIX セクションマージ |
| `python core/record.py TASK-ID status` | TP ステータス更新 |
| `python core/record.py TASK-ID guide SECTION` | ガイドファイルパス |
| `python core/record.py TASK-ID guide_index SECTION` | index.md 再生成 |

## スキルスクリプト

### skills/fb/handler.py

| コマンド | 内容 |
|---|---|
| `python skills/fb/handler.py <kind> <summary> [detail]` | フィードバック送信 |

## テンプレート (specs/templates/)

プロジェクト初期化時に `core/install.py` の `setup_qa_configs()` が配布する QA 設定テンプレート群。配置先は `core/paths.py` の `TEMPLATES_DIR = NXT_ROOT / "specs" / "templates"` で定義される。既存ファイルは上書きしない。

| ファイル | 用途 |
|---|---|
| `eslint.config.mjs` | ESLint Flat Config（`specs/coding/l3-nextjs.md` §5 準拠） |
| `playwright.config.ts` | Playwright の `webServer` + `reuseExistingServer` パターン |
| `lighthouserc.js` | Lighthouse CI 設定 |

追加・変更するときは `core/constants.py` の `QA_CONFIG_TEMPLATES` 一覧と合わせて更新する（リテラル集約、L1 §1.1 ハードコ禁止）。コピー先の各プロジェクトは手動で追従する必要がある点に注意。

## 依存関係

```
constants.py ← 全モジュール（リテラル禁止のため）
paths.py ← 全モジュール（constants.py に依存）
feedback.py ← 全モジュール
page_parser.py ← index.py, record.py, session.py
index.py ← load.py, layo.py, session.py
docs.py ← layo.py, load.py (UI タスクのみ)
state.py ← /codi (全ステップ)
load.py ← /codi ステップ1
layo.py ← /layo ステップ1,5 → docs.py, load.collect_rules, index.py, page_parser.py
record.py ← /codi ステップ4
git_ops.py ← /codi ステップ5, /wrap, /aud
stage_ops.py ← /wrap ステップ 5-4
write_guard.py ← PreToolUse Hook (Write|Edit|NotebookEdit)
coding_rules.py ← 01-workflow.md 本元フロー / skills/codi/SKILL.md ステップ2 / coding_rules_hook.py
coding_rules_hook.py ← PreToolUse Hook (Write|Edit|NotebookEdit)
clone.py ← /layo ステップ3,4 (recon/dump/apply/rules) + /codi ステップ2-B (build/assemble/baseline) → clone_node/recon.mjs, clone_node/baseline.mjs, clone_node/diff.mjs, clone_node/anim_lib_patterns.json
install.py ← dev.py（ヘルパー再利用） / specs/templates/ から QA 設定を配布
fb/handler.py ← /fb
```
