# RSRC-WEBCLONE-CODI-INTEGRATION — /codi へのレイアウト工程組み込み設計案

関連: RSRC-WEBCLONE-STORYBOOK, RSRC-WEBCLONE-PIPELINE, RSRC-WEBCLONE-RULES
タグ: codi, レイアウト工程, パイプライン分岐, 設計案, 実装計画, integration, layout-pipeline, sub-steps, animation, framer-motion, shadcn, three-js

## RSRC-WEBCLONE-CODI-INTEGRATION.概要 — 概要

`RSRC-WEBCLONE-PIPELINE` の 5 フェーズと `RSRC-WEBCLONE-RULES` の管理方針を、erqo-next の既存 `/codi` (5 ステップパイプライン) に組み込むための設計案。「最高精度の再現性」を保証しつつ、ユーザー要望優先・途中修正対応・本棚正本原則を維持する。

**核心方針:** 既存の `/codi` 5 ステップを壊さず、ステップ 2 (implementation) の中身だけを「レイアウトサブパイプライン (7 サブステップ)」に分岐させる。

## RSRC-WEBCLONE-CODI-INTEGRATION.既存構造との関係 — 既存構造との関係

```
/codi TASK-ID
  1. prepare         ← 既存のまま (load.py がレイアウトタスクと判定)
  2. implementation  ← ★ここが分岐
       ├ 通常タスク      → 既存の実装フロー
       └ レイアウトタスク → 7 サブステップに展開
  3. verification    ← 既存 + VRT (pixel-perfect モード) を追加
  4. recording       ← 既存のまま
  5. commit          ← 既存のまま
```

state.py の `PIPELINE_STEPS` は変更しない。サブステップは `current_step="implementation"` の中で別フィールドで追跡する。

## RSRC-WEBCLONE-CODI-INTEGRATION.判定機械化 — 判定の機械化

`load.py` の `_judge_ui` を拡張し、UI タスクの中でさらに「レイアウトタスクか」を判定する。

```python
# core/constants.py に追加
LAYOUT_ID_PATTERNS = ["LAYOUT", "PAGE", "CLONE", "DESIGN"]
LAYOUT_TAG_KEYWORDS = ["クローン", "再現", "レイアウト", "デザイン",
                       "clone", "layout", "design", "ui-clone"]

# core/load.py に追加
def _judge_layout(task_id, task_info, tp_content) -> bool:
    """UI タスクの中でレイアウトタスクを判定。"""
    # ID パターン + タグキーワードのスコアリング (UI 判定と同方式)
```

判定は機械的 (`specs/08-responsibility.md` の「曖昧判断禁止」を順守)。AI が「これはレイアウトっぽい」と自己判定することを禁止。

`task_type` は `"layout"` / `"ui"` / `"all"` の 3 値に拡張。ルールフィルタも 3 値対応。

## RSRC-WEBCLONE-CODI-INTEGRATION.7サブステップ — 7 サブステップ

```
2-1. recon       Playwright CLI で参考サイト 1〜複数から取得
                 (スクショ + DOM + CSS + アセット + アニメ + 動き)
        ↓
2-2. dump        取材結果を .libs/storybook/<部品>/ に書き出す
                 (元サイトの実値そのまま、まだ要望なし)
        ↓
2-3. apply       ユーザー要望を本棚ページに上書き
                 (例: "色は青" "カルーセルは別サイトの方式")
                 ★元サイト < 要望
        ↓
2-4. rules       ハードコ禁止 / iOS safe-area / Tailwind v4 トークン化
                 (rsrc-webclone-rules.md で定義)
        ↓
2-5. build       本棚ページ → .tsx + .stories.tsx を生成
                 (shadcn/ui を base にできるなら使う)
        ↓
2-6. assemble    ページ (page.tsx) に部品を組み込み + SEO 適用
                 (Next.js Metadata API + JSON-LD)
        ↓
2-7. baseline    要望適用後の見た目を VRT 基準スクショとして保存
```

ステップ 3 (verification) で `npx playwright test --project=vrt` を実行し、`baseline` と新しい実装の差分を `threshold: 0, maxDiffPixels: 0` で検証する。

## RSRC-WEBCLONE-CODI-INTEGRATION.アニメ組み込み — アニメーション仕様の組み込み

各サブステップでアニメをどう扱うか:

| サブステップ | アニメに関する処理 |
|---|---|
| 2-1 recon | `element.getAnimations()` で動き抽出 + Playwright で動画記録 |
| 2-2 dump | 取材した動きを本棚ページの「アニメーション仕様」セクションに書く |
| 2-3 apply | 「速さを変えたい」「動きを止めたい」等の要望を上書き |
| 2-5 build | 本棚ページから framer motion variants or CSS keyframes を生成 + 各 phase の story を生成 |
| 2-7 baseline | アニメを停止させた状態 (`prefers-reduced-motion`) で各 phase のスクショを保存 |

**本棚ページでの記載例:**

```
## アニメーション仕様
- 動き名: スクロール時の縮小
- きっかけ: scroll position > 50px
- 元サイト keyframes:
  - opacity: 1 → 0.85
  - transform: translateY(0) → translateY(-4px)
- 速さ: 0.3s
- 動き種類: ease-out
- 実装方式: framer motion (要望で選択)

## アニメ各 phase の story
- Header_Anim_Initial  ← 始まる前
- Header_Anim_Mid      ← 0.15s 時点
- Header_Anim_End      ← 終わった後
```

これでアニメも「本棚ページが正本」原則に統合される。

## RSRC-WEBCLONE-CODI-INTEGRATION.B項目組み込み — shadcn/ui / framer motion / three.js の組み込み箇所

ユーザーの「片隅に意識」事項を、各サブステップでの居場所として確保:

| サブステップ | shadcn/ui | framer motion | three.js |
|---|---|---|---|
| 2-1 recon | – | アニメ取得 | canvas 検出 |
| 2-2 dump | – | 動きの仕様を本棚に記録 | shader/geometry の記録 |
| 2-4 rules | shadcn 既存と統合判定 | – | – |
| 2-5 build | shadcn 拡張で実装 | `motion.div` で実装 | three.js + R3F |
| 2-6 assemble | – | `LayoutGroup` 等 | Canvas マウント |
| 2-7 baseline | – | 静止ショット (`prefers-reduced-motion`) | – |

これらの詳細は次回以降のリサーチで深掘りし、`rsrc-webclone-rules.md` の `todo` セクションに追加していく。

## RSRC-WEBCLONE-CODI-INTEGRATION.新規追加要素 — 新規追加要素一覧

| 種類 | 場所 | 内容 |
|---|---|---|
| 新スクリプト | `core/clone.py` | 7 サブステップを実行する 1 ファイル。サブコマンド: `recon`/`dump`/`apply`/`rules`/`build`/`assemble`/`baseline` |
| 新本棚 | `.libs/storybook/` | `LIBS_SHELVES` に追加 |
| 既存拡張 | `core/load.py` | `_judge_layout` 追加 + `task_type` 3 値化 |
| 既存拡張 | `core/state.py` | サブステップ追跡フィールド (`layout_substep`) を追加 |
| 既存拡張 | `core/constants.py` | `LAYOUT_ID_PATTERNS`, `LAYOUT_TAG_KEYWORDS`, `LAYOUT_SUBSTEPS` 定数追加 |
| 既存拡張 | `core/index.py` | storybook 棚を識別コード収集対象に |
| 仕様更新 | `specs/06-coding-rules.md` | ハードコーディング禁止を TS/TSX に拡張 |
| 仕様更新 | `specs/04-project-guide.md` | storybook 棚を追加 |
| 仕様更新 | `skills/codi/SKILL.md` | レイアウト分岐の説明を追記 |

## RSRC-WEBCLONE-CODI-INTEGRATION.状態管理拡張 — 状態管理の拡張

`state.py` の状態ファイルに `layout_substep` フィールドを追加:

```json
{
  "task_id": "LAYOUT-HOME-CLONE",
  "current_step": 2,
  "completed_steps": ["prepare"],
  "layout_substep": "dump",
  "completed_substeps": ["recon"],
  "started_at": "2026-04-11T...",
  "last_update": "2026-04-11T..."
}
```

サブステップ完了時は `state.py complete_substep recon` を呼ぶ。レイアウトタスク以外では `layout_substep` フィールドは null。

## RSRC-WEBCLONE-CODI-INTEGRATION.実装段階分け — 実装の段階分け

全部一度に作ると context が膨らむ。次の順序で段階的に実装する:

1. **準備フェーズ** (本元の specs と constants の整備)
   - `specs/06-coding-rules.md` を TS/TSX に拡張
   - `specs/04-project-guide.md` に storybook 棚を追加
   - `core/constants.py` に `LAYOUT_*` 定数追加
   - `core/index.py` に storybook 棚を追加

2. **判定機械化フェーズ**
   - `core/load.py` に `_judge_layout` 追加
   - `task_type` を 3 値に拡張
   - 単体テストで判定を確認

3. **clone.py の最小骨格**
   - `core/clone.py` を新規作成、サブコマンド構造のみ
   - 各サブコマンドは「未実装」を返すスタブ
   - `/codi` から呼べるようにする

4. **サブステップを 1 つずつ実装**
   - 順序: `recon` → `dump` → `apply` → `rules` → `build` → `assemble` → `baseline`
   - 各サブステップで動作確認 (手動 + python テスト)

5. **state.py のサブステップ追跡追加**

6. **skills/codi/SKILL.md の更新**

7. **本元での動作確認** (本元では /codi が使えないので、`core/clone.py` 単体で起動する形)

8. **giget 配布** (本元から各プロジェクトへ)

各フェーズは別セッションで進める。1 セッションで 1〜2 フェーズが現実的。

## RSRC-WEBCLONE-CODI-INTEGRATION.次回着手 — 次セッションで着手するもの

最初に手を付けるのは **準備フェーズ** (上記 1)。

具体的なタスク:
- `specs/06-coding-rules.md` の対象を Python から TS/TSX に拡張する文面追加
- `specs/04-project-guide.md` に `storybook/` 棚を追記
- `core/constants.py` の `LIBS_SHELVES` に `"storybook"` を追加
- `core/constants.py` に `LAYOUT_ID_PATTERNS` / `LAYOUT_TAG_KEYWORDS` / `LAYOUT_SUBSTEPS` を追加
- `core/index.py` の reindex 対象に新棚を含める

これらは小規模で副作用が少ないので、次セッションの最初に承認 → 実装の流れで進める。

## RSRC-WEBCLONE-CODI-INTEGRATION.出典 — 出典

(参照日: 2026-04-11)

- `core/load.py` (既存 UI 判定 `_judge_ui`)
- `core/state.py` (既存パイプライン状態管理)
- `core/constants.py` (`PIPELINE_STEPS`, `LIBS_SHELVES`)
- `specs/01-workflow.md` (本元フロー)
- `specs/08-responsibility.md` (責任分担)
- `RSRC-WEBCLONE-PIPELINE` (5 フェーズ実装手順)
- `RSRC-WEBCLONE-RULES` (適用ルール + 管理方針)
- `RSRC-WEBCLONE-STORYBOOK` (調査結果概要)
