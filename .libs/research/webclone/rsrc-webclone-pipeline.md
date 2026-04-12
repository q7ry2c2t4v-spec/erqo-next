# RSRC-WEBCLONE-PIPELINE — 最高精度ウェブクローンの実装手順

関連: RSRC-WEBCLONE-STORYBOOK, RSRC-WEBCLONE-RULES, RSRC-WEBCLONE-CODI-INTEGRATION, RSRC-WEBANIM-CAPTURE
タグ: 実装手順, パイプライン, 5フェーズ, 最高精度, ピクセルパーフェクト, tailwind-v4, theme, csf, vrt, jcodesmore, pipeline, recon, foundation, spec, build, qa

## RSRC-WEBCLONE-PIPELINE.概要 — 概要

`RSRC-WEBCLONE-STORYBOOK` で得た 2 系統アプローチのうち、**DOM/CSS 抽出方式** を最高精度で運用するための具体的な実装手順をまとめる。出典の中心は `JCodesMore/ai-website-cloner-template` の SKILL.md (30KB) で、これに Tailwind v4 `@theme`、CSF 化、VRT pixel-perfect モードを組み合わせる。

## RSRC-WEBCLONE-PIPELINE.recon — Phase 1: 取材 (Reconnaissance)

**目的:** 元サイトの全情報を漏らさず取得する。後工程で AI が推測で補完する余地を消す。

**処理:**

1. **フルページスクショを 2 解像度で取得** — 1440px (desktop) と 390px (mobile)、`docs/design-references/` に保存
2. **フォント抽出** — `<link rel="stylesheet">` の Google Fonts 等 + 全要素の `getComputedStyle().fontFamily` を enum
3. **色 enumeration** — 全要素の `color` / `backgroundColor` / `borderColor` を `getComputedStyle()` で集計
4. **アセット enumeration** — `<img>`, `<video>`, CSS の `background-image` を URL リスト化 (JS スニペットで一括取得)
5. **インタラクション全 sweep** — scroll / click / hover / responsive を踏破し、`docs/research/BEHAVIORS.md` に記録
6. **ページトポロジー** — section の上から順、fixed vs flow、z-index、interaction model (scroll-driven / click-driven / static / time-driven) を `docs/research/PAGE_TOPOLOGY.md` に書く
7. **アニメーション / ライブラリ / スクロール連動 / Lottie・Rive** — WAAPI dump + ライブラリ同定 + 120 分割サンプリング + 自動 DL。詳細は **RSRC-WEBANIM-CAPTURE §技術詳細** を参照。recon.mjs が自動実行する

**出力:** スクショ 2 枚 + BEHAVIORS.md + PAGE_TOPOLOGY.md + assets JSON

## RSRC-WEBCLONE-PIPELINE.foundation — Phase 2: 基盤 (Foundation)

**目的:** `npm run build` が通る土台を完成させる。コンポーネント実装の前に「動く Next.js プロジェクト」を作る。

**順序 (sequential):**

1. **フォント設定** — `src/app/layout.tsx` に `next/font/google` で実フォントを import
2. **色トークン** — `src/app/globals.css` に CSS 変数で色を登録 (Phase 3 で `@theme` に昇格)
3. **TypeScript 型定義** — `src/types/content.ts` に観測したデータ構造を interface 化
4. **SVG アイコン抽出** — 全 inline `<svg>` を `src/components/icons.tsx` に export
5. **アセットダウンロード** — `scripts/download-assets.mjs` を生成・実行し `public/` に配置

**検証:** `npm run build` がゼロエラーで通ること

## RSRC-WEBCLONE-PIPELINE.spec — Phase 3: 仕様化 (Component Spec)

**目的:** 各セクションを「実装に推測の入る余地がない」レベルで仕様化する。

**spec ファイル形式** (`docs/research/components/<ComponentName>.spec.md`、150 行以下):

1. **Overview** — target file / screenshot path / interaction model
2. **DOM Structure** — 階層を箇条書きで
3. **Computed Styles** — 要素ごとに `getComputedStyle()` の生値を全プロパティ列挙
4. **States & Behaviors** — scroll/click/hover の **before/after 両方の CSS 値**
5. **Per-State Content** — verbatim (元サイトのテキストをそのまま)
6. **Assets** — public/ のローカルパス
7. **Responsive Behavior** — 1440 / 768 / 390 の各レイアウト

**Computed Styles 抽出スニペット** (browser MCP / CLI 経由で実行):

```javascript
(function(selector) {
  const cs = getComputedStyle(document.querySelector(selector));
  const props = ['fontSize','fontWeight','fontFamily','color','backgroundColor',
    'padding','margin','width','height','display','flexDirection',
    'borderRadius','boxShadow','opacity','transform','transition'];
  const out = {};
  props.forEach(p => { if (cs[p] && cs[p] !== 'none') out[p] = cs[p]; });
  return out;
})('YOUR_SELECTOR');
```

**重要:** spec が 150 行を超えたら section が大きすぎる → サブコンポーネントに分割。

## RSRC-WEBCLONE-PIPELINE.build — Phase 4: 並列ビルド (Parallel Build)

**目的:** spec ファイルから React コンポーネントを生成する。各コンポーネントは独立した builder agent (Task ツール) に担当させて並列化。

**Builder Agent への prompt template:**

```
You are building a React component for a pixel-perfect website clone.
TARGET FILE: src/components/HeroSection.tsx
SPECIFICATION: [spec ファイル全文を貼る]
SCREENSHOT REFERENCE: docs/design-references/hero-section.png

REQUIREMENTS:
1. Exact CSS values from spec (no approximations)
2. Import icons from 'src/components/icons'
3. Use cn() utility for conditional classes
4. Implement all states: scroll-triggered, hover effects
5. Responsive: mobile 390px, tablet 768px, desktop 1440px

VERIFICATION: Run `npx tsc --noEmit` — must pass with zero errors.
```

**各 agent 完了後:** worktree merge → `npm run build` → 型エラー即修正 → commit

## RSRC-WEBCLONE-PIPELINE.qa — Phase 5: 視覚的検証 (Visual QA Diff)

**目的:** pixel-perfect 一致を機械的に保証する。

**VRT pixel-perfect モード** (Playwright):

```typescript
await expect(page).toHaveScreenshot('reference.png', {
  threshold: 0,        // 色差ゼロ (デフォルト 0.2)
  maxDiffPixels: 0,    // 不一致ピクセルゼロ
});
```

`threshold: 0` は pixelmatch ライブラリで完全一致モードを意味する。1 ピクセルでもズレたら失敗。

**比較対象:** 1440px / 390px の側面比較 + 全インタラクション (scroll, click, hover) を踏破。

**不一致時のループ:** spec 値が間違っていれば再抽出 → spec 更新 → builder 再走 → VRT 再実行。「修正は spec 経由で行う」のが原則 (component 直接修正は spec とのズレを生む)。

## RSRC-WEBCLONE-PIPELINE.tailwind — Tailwind v4 トークン流し込み

**核心:** 任意値 (`pl-[17px]`) を使うと style drift になる。元サイトの実値を `@theme` ディレクティブですべて token として登録し、生成された utility class を component で使う。

```css
/* src/app/globals.css */
@import "tailwindcss";

@theme {
  /* Phase 1 で抽出した実値をそのまま登録 */
  --color-extracted-primary: oklch(70% 0.15 240);
  --color-extracted-bg: oklch(98% 0.01 250);
  --spacing-extracted-17: 17px;
  --spacing-extracted-23: 23px;
  --font-extracted-display: "Inter", sans-serif;
  --radius-extracted-card: 13px;
}
```

これで `bg-extracted-primary`, `p-extracted-17`, `font-extracted-display` 等の utility が自動生成される。**元サイトの値の完全一致を保証しつつ Tailwind の utility 駆動を維持する**。oklch 採用で perceptually uniform を確保。

## RSRC-WEBCLONE-PIPELINE.storybook — CSF 化 (Storybook 化)

JCodesMore のテンプレートは Next.js page にマウントするだけで Storybook を持たない。「忠実再現 Storybook」要件を満たすには **各コンポーネントに `.stories.tsx` を生成する追加ステップ** が必要。

**生成テンプレート** (spec の Per-State Content から args を抽出):

```typescript
import HeroSection from './HeroSection';
import type { Meta, StoryObj } from '@storybook/react';

const meta: Meta<typeof HeroSection> = {
  component: HeroSection,
  tags: ['autodocs'],     // Storybook Autodocs を有効化
};
export default meta;
type Story = StoryObj<typeof HeroSection>;

// spec の Per-State Content から 1 state = 1 story
export const Featured: Story = { args: { content: { heading: '...', cards: [...] } } };
export const Productivity: Story = { args: { content: { heading: '...', cards: [...] } } };
```

**仕組み:** CSF 3 では args を渡せば render 関数不要。`react-docgen` が argTypes を自動推論。`tags: ['autodocs']` で Storybook が `args` / `argTypes` / `parameters` から docs ページを自動生成。

## RSRC-WEBCLONE-PIPELINE.requirements — 最高精度を保証する 5 原則

JCodesMore のテンプレートが「Critical Requirements」として明文化している原則:

1. **Completeness Beats Speed** — `getComputedStyle()` の生値・実アセット・verbatim テキスト・コンポーネント構造を agent に渡す前に全部集める
2. **Small Tasks, Perfect Results** — spec ファイルが 150 行を超えたら section が大きすぎる。サブコンポーネントに分割
3. **Extract Every State** — 全 tab を click、全 trigger を scroll、全 interactive を hover。before/after の CSS を両方取る
4. **Identify Interaction Model First** — scroll-driven / click-driven / static / time-driven の判定を最初にやる。間違えると全書き直し
5. **Spec Files Are Source of Truth** — spec なしに builder agent は走らない。spec は監査可能な抽出アーティファクトとして残す

## RSRC-WEBCLONE-PIPELINE.適用 — erqo-next /codi への適用

`/codi` に「レイアウトデザイン工程」として組み込む場合、`specs/08-responsibility.md` の責任分担 (python が工程制御 / AI が内容生成) に沿ってスクリプト化する:

| Phase | 対応スクリプト案 | AI 担当 |
|---|---|---|
| 1. recon | `core/clone_recon.py` (Playwright CLI 起動 + ファイル配置) | BEHAVIORS / PAGE_TOPOLOGY 執筆 |
| 2. foundation | `core/clone_foundation.py` (layout/globals/types/icons/download スクリプト生成) | フォント・色トークン値の決定 |
| 3. spec | `core/clone_spec.py` (getComputedStyle 実行 + spec テンプレ生成) | spec の Per-State Content 執筆 |
| 4. build | `core/clone_dispatch.py` (spec を読み Task ツール用 prompt 構築) | コンポーネント実装 (builder agent) |
| 5. qa | `core/clone_qa.py` (VRT 実行 + 不一致箇所を spec に紐付け) | spec 修正案の判定 |

**配置:** 本元リポジトリ (`core/` 直下、共通スコープ)。Tailwind v4 `@theme` は Phase 2 で生成、CSF stories は Phase 4 の builder の責務に追加。

## RSRC-WEBCLONE-PIPELINE.出典 — 出典

(参照日: 2026-04-11)

- [JCodesMore/ai-website-cloner-template SKILL.md (raw)](https://raw.githubusercontent.com/JCodesMore/ai-website-cloner-template/master/.claude/skills/clone-website/SKILL.md) — 30KB の完全な手順書
- [Design Tokens That Scale (Tailwind v4) - Mavik Labs](https://www.maviklabs.com/blog/design-tokens-tailwind-v4-2026) — `@theme` パターン、style drift 警告
- [Tailwind v4 Theme variables (公式)](https://tailwindcss.com/docs/theme) — `@theme` ディレクティブ仕様
- [Playwright SnapshotAssertions (公式)](https://playwright.dev/docs/api/class-snapshotassertions) — `threshold` / `maxDiffPixels` パラメータ
- [Storybook CSF (公式)](https://storybook.js.org/docs/api/csf/) — CSF 3 形式
- [Storybook Autodocs (公式)](https://storybook.js.org/docs/writing-docs/autodocs) — `tags: ['autodocs']` の仕組み
- [Storybook TypeScript stories (公式)](https://storybook.js.org/docs/writing-stories/typescript) — `Meta` / `StoryObj` 型
