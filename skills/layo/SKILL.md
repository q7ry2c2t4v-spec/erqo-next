---
name: layo
target: project
description: "/layo ID-CODE" - レイアウトデザインの策定・修正。参考サイト解析 + デザインリファレンス + ルール参照で本棚ページを作成・更新する。何度でも実行可能。
argument-hint: ID-CODE（例: LAYOUT-HERO）
effort: max
---

# /layo - レイアウトデザイン策定

## 概要

識別コード `$ARGUMENTS` のレイアウトデザインを策定・修正する。
本棚ページ (`.libs/storybook/<slug>/<slug>.md`) が正本。

何度でも実行でき、実行のたびに以下が可能:
- 新しい参考 URL を追加して解析
- 要望の追加・修正
- デザインの調整・削除
- トークン (色・フォント・サイズ) の変更

完成したら `/codi $ARGUMENTS` で実装に進む。

## フロー

### ステップ 1: コンテキスト収集

```bash
python "{nxt}/core/layo.py" $ARGUMENTS
```

スクリプトが以下を機械的に収集して出力する:
- モード判定 (新規 / 更新)
- input.md の内容 (あれば)
- 関連デザインリファレンス (docs/ から自動検索)
- コーディングルール (L3-nextjs.md §1 トークンルール)
- プロジェクトルール (スコープ: layout/ui/all)
- 関連ページ (index.py collect)
- 現在の本棚ページ (更新モード時)

**出力に含まれるリファレンスとルールファイルを全て Read する。**
AI が独自にリファレンスやルールを探さない (スクリプトが決定する)。

### ステップ 2: ユーザーとの対話

**新規モードの場合:**
- 「参考にしたいサイトの URL はありますか？（なくても OK）」
- 「どんなデザインにしたいですか？」

**更新モードの場合:**
- 現在の本棚ページの概要を見せる
- 「何を変えたいですか？」

ユーザーの回答をもとに `.libs/storybook/<slug>/input.md` を作成・更新する。
AI が直接 input.md を編集する (ユーザーにファイル操作を求めない)。

input.md のフォーマット:
```markdown
# <TASK-ID> — 入力

## <TASK-ID>.参考サイト
- https://example.com (該当ページの説明)

## <TASK-ID>.要望
- ヒーローは大きな画像 + キャッチコピー
- 色は青系で統一

## <TASK-ID>.メモ
```

### ステップ 3: 参考サイト解析 (recon)

input.md に参考 URL がある場合のみ実行:

```bash
python "{nxt}/core/clone.py" recon $ARGUMENTS
```

- URL がない場合 (テキストだけモード) はスキップされる (text-only.json マーカーで成功扱い)
- 完了後、recon ディレクトリのスクショ画像を Read してユーザーに見せる
- recon は自動で以下も取材する (段階 1 組み込み済):
  - **採用ライブラリ同定** — GSAP / Motion / Lenis / Three.js / Lottie / Rive 等を `<script src>` + グローバル変数で検出
  - **スクロール連動サンプリング** — ページ高さを 120 分割して `transform / opacity / filter` を実測
  - **Lottie / Rive 自動 DL** — 検出時はバイナリを `recon/site-N/assets/` に保存
- 取材根拠: **RSRC-WEBANIM-CAPTURE** (`.libs/research/webanim/`)

### ステップ 4: 本棚ページ生成 + 要望反映 + ルール適用

3 コマンドを順に実行する:

```bash
# 取材データから本棚ページの下書きを生成/更新
python "{nxt}/core/clone.py" dump $ARGUMENTS

# ユーザーの要望を本棚ページに反映
python "{nxt}/core/clone.py" apply $ARGUMENTS

# Tailwind v4 @theme トークン定義 + iOS ルール適用
python "{nxt}/core/clone.py" rules $ARGUMENTS
```

各コマンドは冪等 (`_replace_or_append_section`)。何度実行しても安全。

### ステップ 5: 結果検証

```bash
python "{nxt}/core/layo.py" $ARGUMENTS
```

再度コンテキストを収集し、更新後の本棚ページを含む出力を確認する。

本棚ページの以下をユーザーに見せる:
- 色トークン候補
- フォント・サイズ候補
- 要望の反映状況
- レイアウト構成

「これでいいですか？ 変更したい部分があれば教えてください。」

- 変更がある → ステップ 2 に戻る
- OK → ステップ 6 に進む

### ステップ 6: 完了

```bash
python "{nxt}/core/index.py" reindex
```

「設計が完了しました。`/codi $ARGUMENTS` で実装に進めます。」

## 重要なルール

1. **スクリプト駆動** — リファレンス検索・ルール判定は `layo.py` が行う。AI が独自に検索しない (`specs/08-responsibility.md`)
2. **本棚ページが正本** — `.tsx` や `page.tsx` をこのスキルでは作らない。それは `/codi` の担当
3. **input.md 経由で変更** — 参考 URL と要望は必ず input.md に書く
4. **何度でも再実行可能** — recon/dump/apply/rules は冪等。安心して何度でも回せる
5. **対話ベース** — 全工程を一括で走らせない。ユーザーと会話しながら進める。承認フロー (`specs/00-identity.md`) を守る
6. **スクショ確認** — recon 後にスクショ画像を Read してユーザーに見せる
7. **コーディングルールのロード不要** — このスキルではコードファイルを編集しないため `coding_rules.py` は不要。ただし `layo.py` がトークン設計に必要なルール参照を出力するので、それを読んで設計に反映する
