# スクリプトリファレンス

## 構成

```
.nxt-core/
├── core/          ← コアモジュール（全スクリプトの土台）
│   ├── constants.py   ← 固定値の一元管理
│   ├── paths.py       ← パス定数（constants 由来）
│   ├── feedback.py
│   ├── page_parser.py
│   ├── index.py
│   ├── docs.py
│   ├── install.py     ← プロジェクト用セットアップ
│   ├── dev.py         ← 本体リポジトリ用セットアップ（IS_SOURCE 限定）
│   ├── git_ops.py     ← git 操作ヘルパー（/wrap, /codi 共通）
│   ├── session.py
│   ├── state.py
│   ├── load.py
│   └── record.py
└── skills/        ← スキル定義（SKILL.md ＋ 必要に応じて handler.py）
    └── fb/handler.py
```

## プロジェクト固有スクリプトの配置ルール

**`.nxt-core/` は読み取り専用。** プロジェクト固有のスクリプトは `scripts/` に作成する。

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

### docs.py — ドキュメント検索

| サブコマンド | 内容 |
|---|---|
| `python core/docs.py search KW1 KW2` | `.libs/docs/` 内キーワード検索 |
| `python core/docs.py list [category]` | カテゴリ・ファイル一覧 |
| `python core/docs.py show CAT PATH` | ファイル内容表示 |

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

`/wrap` と `/codi` ステップ5 から共通で使われる git ラッパー。プロジェクト・本体リポジトリ両方で動く（IS_SOURCE ガードなし）。

| コマンド | 内容 |
|---|---|
| `python core/git_ops.py check` | 差分確認 |
| `python core/git_ops.py commit "msg"` | git add -A → commit |
| `python core/git_ops.py commit "msg" --files A B C` | 指定ファイルのみ commit |
| `python core/git_ops.py push` | push |
| `python core/git_ops.py full "msg"` | commit + push |

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

## 依存関係

```
constants.py ← 全モジュール（リテラル禁止のため）
paths.py ← 全モジュール（constants.py に依存）
feedback.py ← 全モジュール
page_parser.py ← index.py, record.py, session.py
index.py ← load.py, session.py
docs.py ← load.py
state.py ← /codi (全ステップ)
load.py ← /codi ステップ1
record.py ← /codi ステップ4
git_ops.py ← /codi ステップ5, /wrap
install.py ← dev.py（ヘルパー再利用）
fb/handler.py ← /fb
```
