---
name: fb
target: project
description: /fb — erqo-next 本体への改善提案・エラー報告・その他のフィードバック送信 (プル子からのみ使用)
---

# /fb — フィードバック送信スキル

## 概要

erqo-next への改善提案・エラー報告・その他のフィードバックを送信する。
ローカル (`.claude/state/feedback/`) に JSON 保存後、`erqo-feedback` 共有リポジトリ
の `inbox/` にも push される。本元 (エル子) はセッション開始時に pull + 新着通知。

## いつ使うか

- erqo-next の動作に問題があったとき
- 改善のアイデアがあるとき
- その他のフィードバックを送りたいとき

## 実行手順

### 1. ユーザーとの対話

フィードバックの内容を確認する:
- **種類**: suggestion (改善提案) / error (エラー報告) / other (その他)
- **概要**: 1行で内容を要約
- **詳細**: (任意) 詳しい説明 — マークダウン本文・コード・パイプ記号 `|` 含む長文も可

### 2. フィードバック送信

**シェル特殊文字 (`|` / `&` / `>` / バッククォート 等) を含まない短い detail:**

```bash
python "{nxt}/skills/fb/handler.py" <kind> "<summary>" "<detail>"
```

**`|` 等を含む / 改行を含む / 長い detail:** 一時ファイルに書いてから `--detail-file` で渡す

```bash
# Windows + Git Bash で detail に | を含めると CMD の論理 OR (||) として誤解釈される
# 事故を防ぐため、長い/特殊文字を含む detail は必ずファイル経由
python "{nxt}/skills/fb/handler.py" <kind> "<summary>" --detail-file <path>
```

例 (詳細なバグレポートをファイルから送る):

```bash
python "{nxt}/skills/fb/handler.py" error "record.py status の substring match バグ" --detail-file fb-detail.md
```

### 3. 結果確認

保存先のパスが標準出力に表示される。並行して `erqo-feedback` リポジトリへ push が
試行される (`.libs/fb-shared/` が clone 済みなら自動)。

未 clone / リポジトリ未作成時は warning が出るのみで、ローカルの JSON 保存は成功する。
この場合はユーザーに「erqo-feedback リポジトリの作成 + clone」を依頼する。

## 配送経路の理解

```
プル子 /fb 実行
   │
   ├─ ローカル: <PROJECT>/.claude/state/feedback/<kind>-<ts>.json
   │
   └─ 共有リポ: erqo-feedback/inbox/<project_name>-<kind>-<ts>.json
                   ↑ push                          ↓ pull
                                                エル子セッション開始時に新着通知
```

`.libs/fb-shared/` が clone されていれば全自動。されていなければローカル保存のみで
配送は手動 (ユーザーが内容を本元に伝える)。

## 重要なルール

1. **ユーザーの承認** — フィードバック内容をユーザーに確認してから送信する
2. **種類の選択** — 内容に合った kind を選ぶ (suggestion / error / other)
3. **シェル特殊文字を含む detail は必ず `--detail-file` 経由** — 直接渡しは Windows 環境で化ける
4. **失敗してもパニックしない** — 共有リポへの push が失敗してもローカル保存は成功している。本元への手動転送を案内する
