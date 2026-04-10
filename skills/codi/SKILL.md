---
name: codi
description: "/codi ID-CODE" - 識別コード指定でタスクを5ステップパイプラインで実行する。準備→実装→検証→記録→コミット。
argument-hint: ID-CODE（例: AUTH-SESSION-FLOW）
effort: max
---

# /codi - 実装パイプライン (5ステップ)

## 概要

識別コード `$ARGUMENTS` のタスクを5ステップで一括実行する。
修正タスク（FIX を含む識別コード）も同じパイプラインを通る。

## 状態管理

パイプラインの状態は `state.py` で管理する。AI が直接 JSON を書かない。

**開始時:**
```bash
python "{nxt}/core/state.py" $ARGUMENTS init
```
- 新規: 状態ファイルを作成 + 依存タスク完了チェック
- 中断復旧: 既存の状態ファイルを読み、完了済みステップをスキップ

**各ステップ完了時:**
```bash
python "{nxt}/core/state.py" $ARGUMENTS complete STEP_NAME
```

**全完了時:**
```bash
python "{nxt}/core/state.py" $ARGUMENTS delete
```

ステップ名: `prepare`, `implementation`, `verification`, `recording`, `commit`

## 5ステップ

### ステップ1: 準備 (prepare)

```bash
python "{nxt}/core/state.py" $ARGUMENTS init
python "{nxt}/core/load.py" $ARGUMENTS
```

load.py が以下を収集して出力する:
- TP ページからタスク情報
- UI 判定 (スコアリング方式)
- UI タスクの場合: docs 検索で関連ドキュメント収集
- 同セクション内の全 features ページ
- index.py collect で関連ページ収集
- ルールをスコープフィルタリング付きでロード

出力を読み、タスクの背景・関連機能の仕様を把握した状態で次に進む。

完了後:
```bash
python "{nxt}/core/state.py" $ARGUMENTS complete prepare
```

### ステップ2: 実装 (implementation)

収集したコンテキストを踏まえて実装を行う。

- 関連機能の仕様と矛盾しないこと
- プロジェクトルールを遵守すること
- 承認フロー: 実装方針をユーザーに提示し「これで実装していいですか？ (y/n)」で承認を得る

完了後:
```bash
python "{nxt}/core/state.py" $ARGUMENTS complete implementation
```

### ステップ3: 検証 (verification)

実装内容を自動検証する。プロジェクトに応じて以下を実行:

```bash
# TypeScript 型チェック
npx tsc --noEmit

# ESLint
npx eslint .

# Playwright (e2e + VRT)
npx playwright test

# アクセシビリティ (axe-core)
npx playwright test --grep accessibility

# Lighthouse CI
npx lhci autorun
```

- 全コマンドが成功 → 次へ
- 失敗 → 修正して再検証 (最大3回)
- プロジェクトに該当ツールがない場合はスキップ

完了後:
```bash
python "{nxt}/core/state.py" $ARGUMENTS complete verification
```

### ステップ4: 記録 (recording)

3つの処理を順に実行する:

**4a. features ページ作成:**
```bash
python "{nxt}/core/record.py" $ARGUMENTS
```

新規タスク: テンプレートから空ページを作成し、全6セクション (概要・仕様・設計判断・構成・トラブル・備考) を執筆する。復元可能レベルの詳細さで書く。

FIX タスク:
1. record.py が旧ページを history/ にアーカイブ
2. 変更セクションだけを一時ファイルに書き出す
3. マージを実行:
```bash
python "{nxt}/core/record.py" $ARGUMENTS merge --changed "概要,仕様" --file 一時ファイルパス
```

記録ページを書き終えたらインデックスを更新:
```bash
python "{nxt}/core/index.py" reindex
```

**4b. TP ステータス更新:**
```bash
python "{nxt}/core/record.py" $ARGUMENTS status
```

**4c. ユーザーガイド更新:**
```bash
python "{nxt}/core/record.py" $ARGUMENTS guide SECTION
```
返されたパスに、実装内容を専門用語なしで要約して書き込む。

執筆ルール:
- **専門用語禁止** — コード名、ライブラリ名、技術用語を使わない
- **要約レベル** — 「何ができるか」「どう使うか」に焦点
- **平易な日本語** — 開発者でない人が読んでもわかる表現

書き込み後に index を再生成:
```bash
python "{nxt}/core/record.py" $ARGUMENTS guide_index SECTION
```

完了後:
```bash
python "{nxt}/core/state.py" $ARGUMENTS complete recording
```

### ステップ5: コミット (commit)

```bash
python "{nxt}/skills/gh/handler.py" commit "feat($ARGUMENTS): 実装・記録・ガイド更新"
python "{nxt}/core/state.py" $ARGUMENTS complete commit
python "{nxt}/core/state.py" $ARGUMENTS delete
```

実装 + 記録 + ガイド + ステータスを1コミットにまとめ、状態ファイルを削除する。

## 重要なルール

1. **ステップ順序の厳守** — 必ず1→2→3→4→5の順で実行する。スキップしない
2. **状態管理は state.py** — AI が直接 JSON を書かない。必ずスクリプト経由で管理する
3. **各ステップ完了時に complete を呼ぶ** — 中断復旧に必要
4. **復元可能性** — 記録ページはプロジェクト復元マニュアルとしての詳細さを保つ
5. **AI の担当範囲** — 実装、記録の執筆、ユーザーガイドの要約のみ。ファイル管理・マージ・インデックス・状態管理はスクリプトが担当
6. **FIX タスクの安全性** — 修正時は変更セクションだけ書く。未変更セクションはスクリプトがコピーする
