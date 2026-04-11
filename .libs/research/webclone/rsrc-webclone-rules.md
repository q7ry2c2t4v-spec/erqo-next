# RSRC-WEBCLONE-RULES — ウェブクローン適用ルールと Storybook 管理方針

関連: RSRC-WEBCLONE-STORYBOOK, RSRC-WEBCLONE-PIPELINE, RSRC-WEBCLONE-CODI-INTEGRATION
タグ: ルール, ハードコーディング禁止, iOS対応, SEO, Storybook管理, 本棚正本原則, no-hardcoding, ios, safe-area, viewport-fit, seo, metadata, json-ld, storybook-management, single-source-of-truth

## RSRC-WEBCLONE-RULES.概要 — 概要

`RSRC-WEBCLONE-PIPELINE` の 5 フェーズパイプラインを実行する際に適用すべきルール群と、Storybook 部品の実装後の管理方針をまとめる。「最高精度の再現」を保証しつつ、ユーザー要望を最優先で取り入れられる仕組みを定義する。

## RSRC-WEBCLONE-RULES.hardcoding — ハードコーディング禁止 (フロントエンド拡張)

`specs/06-coding-rules.md` のハードコーディング禁止ルールは現状 Python 限定 (`core/`, `skills/`, `scripts/`)。ウェブクローン用には **Next.js のフロントエンド (TS/TSX) にも拡張** する必要がある。

**禁止される書き方:**

```typescript
// NG: 直書き
<div style={{ color: '#3b82f6', padding: '17px' }}>
<div className="bg-[#3b82f6] p-[17px]">
```

**推奨される書き方 (Tailwind v4 `@theme` 経由):**

```typescript
// OK: トークン経由
<div className="bg-extracted-primary p-extracted-17">
```

**理由:** 元サイトの実値はすべて Phase 2 で `@theme` に新規トークンとして登録される。直書きを許すと「どこに何の値があるか」が散らばり、要望の上書きや差し替えが困難になる。

## RSRC-WEBCLONE-RULES.ios — iOS / Apple 系対応

iOS Safari で起きやすい問題と、全部品で適用すべき対策。

| 起きる問題 | 対策 |
|---|---|
| 画面下のホームインジケーター領域にボタンが隠れる | `env(safe-area-inset-bottom)` で余白を取る |
| 画面端まで背景が伸びない | `<meta name="viewport" content="viewport-fit=cover">` を `layout.tsx` に設定 |
| Modal/Drawer の下端に隙間が出る (iOS 26 既知バグ) | Backdrop を画面全体に伸ばす |
| ボタンが押しづらい | タップ領域を最低 **44×44pt** で保証 |
| 100vh が誤動作 | `100dvh` を使う (動的 viewport) |

**実装方針:**

1. **safe-area トークン化** — `@theme` に safe-area 用変数を登録:
   ```css
   @theme {
     --spacing-safe-bottom: env(safe-area-inset-bottom);
     --spacing-safe-top: env(safe-area-inset-top);
     --spacing-tap-min: 44px;
   }
   ```
2. **layout.tsx で viewport-fit=cover を強制** — フォーマットは Next.js 16 の `viewport` export を使う
3. **タップ可能な部品の最小サイズチェック** — Phase 5 (QA) で `--spacing-tap-min` を満たさない要素を検出する自動チェックを追加

## RSRC-WEBCLONE-RULES.seo — SEO 最適化 (Next.js 16)

部品レベルではなく **ページ統合 (Phase 4 後半)** で適用するルール。

1. **Metadata API** — 静的は `metadata` オブジェクト、動的は `generateMetadata` 関数で `app/layout.tsx` または `app/<route>/page.tsx` から export
2. **Open Graph** — 1200×630 画像、絶対 URL、`summary_large_image` 形式
3. **構造化データ (JSON-LD)** — Schema.org 準拠で server-rendered。`<script type="application/ld+json">` を SSR 経由で埋め込む
4. **title 60 文字以内** — 検索結果での切り捨て回避
5. **`app/robots.ts` と `app/sitemap.ts`** — robots.txt と sitemap を動的生成
6. **画像最適化** — `next/image` を必須、`alt` 属性は verbatim から取得

**統計:** 構造化データを入れるとクリック率が 20〜30% 向上するという報告がある。

## RSRC-WEBCLONE-RULES.management — Storybook 実装後の管理方針

**核心原則: 「本棚ページが正本」**

すべての修正を本棚ページ (`.libs/storybook/<part>/<part-name>.md`) 経由で行う。コード (`.tsx` / `.stories.tsx`) を直接編集しない。

**理由:**

1. **二重情報源を作らない** — 本棚とコードを両方手で触ると必ずズレる
2. **「なぜこの値か」が必ず追跡できる** — 本棚に要望が書いてあるので半年後でも理由がわかる
3. **責任分担と整合** — `specs/08-responsibility.md` の「python が制御 / AI が内容生成」と一致

### 3 種類の修正パターン

**A. 小さい修正 (色・文字・余白の調整):**

```
本棚ページの該当箇所を編集
  → スクリプトが .tsx と .stories.tsx を再生成
  → VRT (機械的見た目チェック) で確認
```

**B. 状態追加・構造変更 (新しい状態追加、子要素追加):**

```
本棚ページの「状態リスト」または「DOM 構造」に追記
  → スクリプトが再生成
  → VRT で確認
```

**C. 大きな差し替え (別サイトのカルーセルを取り入れる等):**

```
本棚ページに新しい参考 URL を追加
  → 該当部分だけ再取材スクリプト実行 (元サイト全体は触らない)
  → 取材結果が本棚ページの該当ブロックを上書き
  → 要望を上書き (例: "色は元の青のまま")
  → 再生成 + VRT
```

### 禁止事項

- `.tsx` / `.stories.tsx` の **直接編集禁止** — 本棚との不整合を生む
- 例外: VRT が見つけた微差をスクリプトが自動修正する場合のみ可

### 本棚ページ構成案 (1 部品 = 1 ページ)

```
# STORY-HEADER-MAIN — メインヘッダー部品

関連: 関連部品の識別コード
タグ: ヘッダー, ナビゲーション, 上部固定, header, navigation, sticky

## 参考ソース
- 主参考: https://example.com/ (取材日: 2026-04-11)
- カルーセル参照: https://example2.com/ (取材日: 2026-04-12)

## 要望 (元サイトより優先)
- 背景色: 青 (元サイトの白を上書き)
- ロゴサイズ: 1.2 倍

## DOM 構造
[Phase 3 spec から流し込み]

## Computed Styles (要望適用後)
[Phase 3 spec から流し込み + 要望差分]

## 状態一覧 (Storybook stories)
- Default
- Scrolled (背景半透明)
- Mobile (390px)

## 適用ルール
- ハードコーディング禁止: ✓
- safe-area: ✓ (top inset 適用)
- タップ領域 44px: ✓

## 生成物
- src/components/Header.tsx
- src/components/Header.stories.tsx
```

## RSRC-WEBCLONE-RULES.todo — 後程詰める事項

ユーザーから「片隅に意識しておく」と指示があった項目。具体化は次セッション以降。

### 1. shadcn/ui への対応

JCodesMore のテンプレートは shadcn/ui を採用している。shadcn/ui は「コピペ式」のコンポーネント集で、`npx shadcn add button` で `src/components/ui/` にコードがコピーされる。

**検討点:**
- 抽出した部品が shadcn/ui の既存コンポーネントと類似している場合、shadcn/ui を base にして上書きするか、独自実装するか
- shadcn/ui のテーマ変数 (`--background`, `--foreground` 等) と `@theme` の `--color-extracted-*` をどう統合するか
- アクセシビリティ (Radix UI) の恩恵を受けつつ、見た目は元サイトに合わせる方法

### 2. framer motion への対応

スクロール連動・ホバーアニメ・ページ遷移などに使われる定番ライブラリ。

**検討点:**
- 元サイトの CSS animation / transition / keyframes を framer motion の `motion.div` の `animate` / `variants` にどうマッピングするか
- スクロール連動 (`useScroll`, `useTransform`) を Phase 3 spec の「states & behaviors」からどう生成するか
- アニメーションの timing (`duration`, `ease`) を CSS から framer motion props に変換する手順

### 3. three.js への対応

3D 表現・WebGL を使ったページの再現。元サイトが three.js を使っている場合、DOM 解析だけでは情報が取れない。

**検討点:**
- canvas 内のシーン情報を取得する方法 (Spector.js / Three Inspector 等のリサーチ必要)
- shader / geometry / texture の抽出と再現
- スクショベースだと特に苦手なので、別アプローチが必要

### 4. アニメーション・エフェクトの解析と管理

「模倣したいアニメーション」の取材・記録・実装の流れ。

**検討点:**
- Playwright で `Animation` API (`element.getAnimations()`) や `KeyframeEffect` を取得できるか
- Lenis などのスムーススクロールライブラリの検出と再現方法
- アニメーション仕様を本棚ページにどう書くか (動画リンク + keyframes + duration + ease)
- 「動き」専用の本棚棚 (`motion/`?) を分けるか、各部品ページに統合するか

これらは次セッション以降で 1 つずつ深掘りしてリサーチページに追加する。

## RSRC-WEBCLONE-RULES.出典 — 出典

(参照日: 2026-04-11)

- [Designing Websites for iPhone X (WebKit)](https://webkit.org/blog/7929/designing-websites-for-iphone-x/) — safe-area-inset と viewport-fit
- [Adding support for iOS' safe areas in your web app](https://jipfr.nl/blog/supporting-ios-web/) — 実装ガイド
- [iOS 26 Drawer bottom gap (mui issue)](https://github.com/mui/material-ui/issues/46953) — 最新バグ報告
- [Next.js Metadata API (公式)](https://nextjs.org/docs/app/getting-started/metadata-and-og-images) — Metadata と OG
- [Next.js generateMetadata (公式)](https://nextjs.org/docs/app/api-reference/functions/generate-metadata) — 動的メタデータ
- [Next.js SEO Optimization Guide 2026](https://www.djamware.com/post/697a19b07c935b6bb054313e/next-js-seo-optimization-guide--2026-edition) — 2026 版 SEO 総合
- [Complete Next.js SEO Guide (BetterLink)](https://eastondev.com/blog/en/posts/dev/20251219-nextjs-seo-guide/) — Metadata + 構造化データ
