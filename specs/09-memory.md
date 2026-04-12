# 記憶層と記録の優先順位

エル子は複数の「記憶層」を持つが、erqo-next OS の記録機能を必ず最優先とする。

## 記憶層の種類

| 層 | 場所 | 永続性 | マルチデバイス共有 |
|---|---|---|---|
| OS 記録 | `.libs/`, `.claude/state/`, `specs/` | 永続 | ✓ git で共有 |
| Claude Code メモリー | `~/.claude/projects/.../memory/` | 永続 | ✗ デバイス依存 |
| 会話履歴 | セッション内コンテキスト | 一時 | × |

## 優先順位

1. **OS 記録が正本**
   - 知識・ルール・経験・セッションログはすべて OS 記録（`.libs/`, `.claude/state/`, `specs/`）に保存する
   - git で管理されるため複数デバイス間で同期される
   - これが「マルチデバイス・マルチプロジェクト」の理念を支える

2. **Claude Code メモリーは補助のみ**
   - Claude Code 自身のシステム上どうしても必要な範囲では使ってよい（例: Claude Code の操作 tips）
   - erqo-next 自体の知識・ルールは OS 記録に置く
   - 同じ情報を両方に持つ場合は OS 記録が正本。Claude Code メモリーは複製として扱う

3. **会話履歴に依存しない**
   - 機械的に取得できる情報源（`git diff` / スクリプト出力 / `state.py` / ファイルシステム）から判断する
   - これは `specs/08-responsibility.md` の「AI 記憶への依存禁止」と整合する

## OS 記録の保存先早見表

| 種類 | 配置先 | 作成方法 |
|---|---|---|
| OS 全体ルール | `specs/`（本元） | 手動編集 |
| プロジェクト固有ルール | `.libs/rules/` | `/ruru` |
| 設計（大枠） | `.libs/design/project-spec/` | `/dsgn` |
| タスク計画 | `.libs/design/<section>/` | `/tp` |
| 実装記録 | `.libs/features/` | `/codi` |
| ウェブリサーチ | `.libs/research/` | `/rsrc` |
| セッションログ | `.libs/session-logs/` | `/wrap` |
| ランタイム状態 | `.claude/state/` | 各種スクリプト |

## 既知の制約: Claude Code の保護パス

Claude Code は以下を「保護パス」として扱い、`bypassPermissions` モードでも書き込み時に確認プロンプトを出す:

- `.git/` 配下（全て）
- `.claude/` 配下（例外: `commands/`, `agents/`, `skills/`, `worktrees/` の 4 つのみ）

設定による Override は存在しない。`--dangerously-skip-permissions` フラグでも保護パスは例外のままである。

### Hook による事前ブロック

erqo-next は `core/write_guard.py` を `PreToolUse` Hook（matcher: `Write|Edit|NotebookEdit`）に登録し、保護パスへの書き込みを **Claude Code の確認プロンプトが出る前に** ブロックする。AI が間違えて保護パスに書き込もうとしても `exit 2` でツール実行が止まり、日本語のエラーメッセージが返る。設定の出どころは `core/constants.py` の `PROTECTED_PATH_PREFIXES` と `PROTECTED_PATH_EXCEPTIONS` で一元管理している。

### 一時ファイル・ランタイムデータの配置ルール

新しい一時ファイル・ランタイムデータの置き場所を決めるときは:

1. `.git/` と `.claude/`（例外 4 つを除く）は絶対に避ける
2. プロジェクトルート直下のドット始まりファイル（例: `.commit_msg_tmp.txt`）、または保護パス外の新規ディレクトリに置く

`.git/` や `.claude/` 配下への書き込みを見つけたら、配置先を上記ルールに従って変更する。`write_guard.py` が事前ブロックするが、ルール自体を AI が知っていないと誤った設計判断を生むため、このルール本文も合わせて維持する。
