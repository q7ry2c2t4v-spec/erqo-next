---
name: codi
target: project
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

**必須: コーディングルールの事前ロード**

実際にファイルを編集する前に、対象ファイルのパスを `coding_rules.py` に渡して
適用ルールを機械判定し、返ってきたルールファイルを**全て Read してから編集に入る**:

```bash
python "{nxt}/core/coding_rules.py" <編集対象のファイルパス>
```

出力例:
```
specs/06-coding-rules.md                 (L1 汎用 — 常時適用)
specs/coding/l2-typescript.md            (L2 TypeScript)
specs/coding/l3-nextjs.md                (L3 Next.js)
```

判定は機械的に行われるため AI の自己判断は挟まない (`specs/06-coding-rules.md` §0
/ `specs/08-responsibility.md`)。さらに `PreToolUse` Hook の `coding_rules_hook.py`
が `Write` / `Edit` / `NotebookEdit` 実行直前に同じルール一覧を stderr に通知する
ため、見落とさず必ず Read すること。

#### 2-A. 通常タスク (UI / API / その他)

承認後、ステップ 1 で収集したコンテキストに従って直接実装する。

#### 2-B. レイアウトタスク (LAYOUT / PAGE / CLONE / DESIGN)

task_id が `LAYOUT-*` / `PAGE-*` / `CLONE-*` / `DESIGN-*` のいずれかで始まる場合、
ステップ 2 は `clone.py` の **7 サブステップ** に自動展開される。`state.py` が
`layout_substep` フィールドでサブステップ進捗を追跡する。

**事前準備:** ユーザーが取材入力ファイルを用意していること。
```
.libs/storybook/<task-slug>/input.md
```
`## <TASK-ID>.参考サイト` / `## <TASK-ID>.要望` / `## <TASK-ID>.メモ` の
3 セクションを持つ Markdown。URL ゼロでも要望があれば「テキストだけモード」で進行する。

**7 サブステップを順に実行する:**

```bash
# 2-1. 取材 (Node + Playwright で参考サイトから 6 項目取材 + スクショ)
python "{nxt}/core/clone.py" recon $ARGUMENTS
python "{nxt}/core/state.py" $ARGUMENTS complete_substep recon

# 2-2. 本棚化 (元サイト実値だけで本棚ページの下書きを作る)
python "{nxt}/core/clone.py" dump $ARGUMENTS
python "{nxt}/core/state.py" $ARGUMENTS complete_substep dump

# 2-3. 要望適用 (「要望反映指示」セクションを本棚ページに追記)
python "{nxt}/core/clone.py" apply $ARGUMENTS
python "{nxt}/core/state.py" $ARGUMENTS complete_substep apply

# 2-4. ルール適用 (Tailwind v4 @theme トークン定義 + iOS 対応)
python "{nxt}/core/clone.py" rules $ARGUMENTS
python "{nxt}/core/state.py" $ARGUMENTS complete_substep rules

# 2-5. 部品実装 (本棚ページのビルド指示 + 雛形を読み .tsx / .stories.tsx を書く)
python "{nxt}/core/clone.py" build $ARGUMENTS
# → AI がここで本棚ページを読み、実際の .tsx / .stories.tsx を src/components/<slug>/ に作成
python "{nxt}/core/state.py" $ARGUMENTS complete_substep build

# 2-6. ページ統合 (page.tsx 組み込み + Next.js Metadata + JSON-LD)
python "{nxt}/core/clone.py" assemble $ARGUMENTS
# → AI が assemble 指示セクションを読んで実際に page.tsx を編集
python "{nxt}/core/state.py" $ARGUMENTS complete_substep assemble

# 2-7. VRT 基準スクショ (pixel-perfect threshold:0 基準を保存)
python "{nxt}/core/clone.py" baseline $ARGUMENTS
# → AI が Storybook + playwright vrt --update-snapshots で基準を更新
python "{nxt}/core/state.py" $ARGUMENTS complete_substep baseline
```

**重要:**
- 各サブステップは **本棚ページ (`.libs/storybook/<slug>/<slug>.md`) が正本**。`.tsx` / `.stories.tsx` を直接編集してはいけない (修正は必ず input.md → recon/apply から)。
- 冪等: 途中で要望を変えた場合、`input.md` を編集し apply / rules / build を再実行すれば本棚ページが最新化される。
- 各サブステップ完了時に `state.py complete_substep` を呼び、`layout_substep` を次に進める。

#### 2 共通: 完了記録

全サブステップ (レイアウトタスクの場合) または通常実装 (通常タスクの場合) が
終わったら、ステップ 2 自体の完了を記録する:

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

新規タスク: テンプレートから空ページを作成し、全7セクション (概要・仕様・設計判断・構成・トラブル・参考リサーチ・備考) を執筆する。復元可能レベルの詳細さで書く。参考リサーチセクションには実装中に使ったウェブリサーチを記録する (なければ「該当なし」と明記)。

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
python "{nxt}/core/git_ops.py" commit "feat($ARGUMENTS): 実装・記録・ガイド更新"
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
