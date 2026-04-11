# RSRC-WEBCLONE-STORYBOOK — 参照 URL からの忠実再現 Storybook 自動生成

関連: RSRC-WEBCLONE-PIPELINE, RSRC-WEBCLONE-RULES, RSRC-WEBCLONE-CODI-INTEGRATION
タグ: ウェブクローン, スクリーンショット, ストーリーブック, デザイントークン, 自動生成, 忠実再現, レイアウト, webclone, screenshot, storybook, design-tokens, autogen, pixel-perfect, layout, playwright, claude-code, mcp

## RSRC-WEBCLONE-STORYBOOK.概要 — 概要

参照ウェブサイトの URL を起点に、Claude Code から自動でスクリーンショット取得・コード解析を行い、忠実に再現できる Storybook を生成するパイプラインを構成する手段を調査した。前セッション本題「プロジェクト OS 側の `/codi` レイアウトデザイン工程の定義」の設計材料として位置づける。

調査は次の 5 観点で行った: (1) Playwright 経由の情報取得、(2) ページ解析・デザイントークン抽出、(3) Storybook 自動生成、(4) Claude Code との連携、(5) 忠実度を上げる工夫。

## RSRC-WEBCLONE-STORYBOOK.調査結果 — 調査結果

主要な結論は 3 つ:

1. **2 系統のアプローチが存在する** — スクショ画像から AI が推測して生成する方式 (screenshot-to-code 系) と、DOM + 計算済み CSS を抜き出して再構成する方式 (Perfect Web Clone, JCodesMore/ai-website-cloner-template 系)。後者の方が忠実度・保守性で優れる
2. **Claude Code 公式のツール群が成熟している** — Microsoft 製の Playwright MCP と、より省トークンな Playwright CLI が両立。さらに `/clone-website` のような既存のスキルテンプレートが GitHub で公開済み (JCodesMore は 6000+ stars)
3. **Storybook 自動生成は構造化情報からなら現実的** — CSF + Autodocs の組み合わせで、コンポーネント定義から自動的にストーリーが立つ。フレームワーク非依存のため React / Vue / HTML / Web Components いずれにも適用可

## RSRC-WEBCLONE-STORYBOOK.技術詳細 — 技術詳細

### 1. Playwright で URL の情報を取得する

Playwright は `page.content()` で完全な HTML、`page.screenshot()` で画像、`page.evaluate(() => getComputedStyle(...))` で計算済み CSS を取得できる。アクセシビリティツリー (`browser_snapshot`) は DOM の意味構造を持っているため、ノイズの多い HTML より AI に渡しやすい。動的にロードされる JS-heavy なページでも `page.content()` は実行後の最終 HTML を返す。

### 2. ページ解析・デザイントークン抽出

候補ツール:

- **Dembrandt** (OSS CLI): Playwright + W3C Design Tokens 標準。`dembrandt example.com --dtcg --save-output` でカラー・タイポ・スペーシングを JSON で出力。`--browser=firefox` で bot 検知回避、`--dark-mode` でダークテーマ抽出も可能
- **Superposition** (GUI のみ、無料): macOS / Windows / Linux アプリ。CSS / Scss / JS / Figma 等にエクスポート可。CLI なしのため自動化には不向き
- **`@projectwallace/css-design-tokens`** (npm ライブラリ): CSS 文字列を入力にトークン化。URL からの取得は持たないので Playwright と組み合わせて使う。出力は色・寸法・フォント・シャドウ・イージング等の構造化 JSON
- **Perfect Web Clone の Extraction Phase**: Playwright で DOM + 全 CSS + アセット + テーマを一括抽出するマルチエージェント構成

スクショ単体ではなく **構造化された CSS を抜く** のが現代の主流。

### 3. Storybook 自動生成

- **Component Story Format (CSF)**: ES6 モジュールベースの公開仕様。フレームワーク非依存
- **Storybook Autodocs**: `autodocs` タグを付けると `args` / `argTypes` / `parameters` から自動でドキュメントページを生成
- **screenshot-to-code** (OSS, abi/screenshot-to-code): スクショ・モックアップ・Figma を入力に HTML+Tailwind / React+Tailwind / Vue+Tailwind / Bootstrap / SVG を出力。Web UI のみで CLI なし
- 既存 HTML/CSS から CSF を直接生成する確立されたツールはまだ少ない。実務では「DOM 解析 → コンポーネント分割 → 各コンポーネントを CSF にラップ」を AI 側のロジックで担う

### 4. Claude Code との連携

- **Playwright MCP** (`@playwright/mcp`): Microsoft 公式。`claude mcp add playwright npx '@playwright/mcp@latest'` でセットアップ。25 ツール (navigate / click / snapshot / screenshot 等)。1 タスク約 114k トークンを消費
- **Playwright CLI** (`@playwright/cli`): 同じく Microsoft 公式。スナップショットを YAML、スクショを PNG としてディスクに保存し、エージェントが必要箇所だけ読む。同等タスクで約 27k トークン (4 倍効率)。`playwright-cli install --skills` で Claude Code 統合
- **既存スキル**: `JCodesMore/ai-website-cloner-template` は `/clone-website` を提供。`ericshang98/Perfect-Web-Clone` は 40+ ツールのマルチエージェント構成

省トークンが要求される `/codi` 工程では Playwright CLI が最適と判断できる。

### 5. 忠実度を上げる工夫

- **Visual Regression Test (VRT)**: Playwright の `expect(page).toHaveScreenshot()` で基準画像と差分検出。`maxDiffPixels` / `maxDiffPixelRatio` で許容差を調整
- **Chromatic**: Storybook 専用の VRT クラウドサービス。各 PR で全ストーリーをスナップショット
- **`@playwright/test` + Storybook test runner**: ローカル無料で実装可能。`build-storybook` → `sb extract` → Playwright で各 story の iframe を読みに行く
- **コンポーネント分割の粒度**: Perfect Web Clone のように main agent が DOM を解析してコンポーネント境界を決め、worker agent が並列で各セクションを生成する方式が有効
- **アセット同梱**: フォント・SVG・画像を `public/` にダウンロードしておかないと再現できない (JCodesMore テンプレートが採用)
- **JCodesMore テンプレートのパイプライン**: Recon → Foundation (フォント・色・アセット) → Component Specs → Parallel Build (git worktrees) → Assembly & QA (visual diff) の 5 フェーズ

## RSRC-WEBCLONE-STORYBOOK.比較 — 比較・選択肢

2 系統のアプローチ:

| 観点 | スクショ→コード方式 | DOM/CSS 抽出方式 |
|---|---|---|
| 代表 | abi/screenshot-to-code | Perfect Web Clone, JCodesMore template, Dembrandt |
| 入力 | 画像 / Figma / 動画 | 実 DOM + 計算済み CSS + アセット |
| 忠実度 | 中 (AI の推測に依存) | 高 (実値を保持) |
| 保守性 | 低 (ハードコード px が増えやすい) | 高 (デザイントークン・レスポンシブ保持) |
| 動的状態 | 取得困難 | hover / focus 等を直接観測可 |
| トークン消費 | 中 | 大 (DOM が大きいため、CLI 採用で緩和) |
| 適性 | モックアップ起点・速いプロト | 実サイトの忠実再生・移行 |

`/codi` の「忠実に再現できる Storybook」要件に合うのは **DOM/CSS 抽出方式**。ただし大規模ページでは context overflow を避けるためマルチエージェント (worker agent 並列) が必要になる。

## RSRC-WEBCLONE-STORYBOOK.適用 — プロジェクトへの適用

`/codi` のレイアウトデザイン工程として以下のサブステップを置く案:

1. **取材 (recon)**: Playwright CLI で URL のスクショ + DOM + 計算済み CSS + アセットを取得し、保存パスを返す
2. **トークン抽出**: Dembrandt または `@projectwallace/css-design-tokens` でカラー・タイポ・スペーシングを JSON 化 → Tailwind config に反映
3. **コンポーネント分割設計**: AI が DOM を読み、セクション (header / hero / cards / footer 等) に分けて spec を JSON で書く
4. **並列ビルド**: セクションごとに worker (sub-agent or 単純なファイル分割) で React コンポーネントを生成し、CSF ファイルを並べる
5. **VRT 検証**: Playwright + Storybook test runner で基準スクショと差分を取り、しきい値超えなら工程 4 に戻して修正

erqo-next の責任分担ルール (`specs/08-responsibility.md`) に沿うと、どのステップも **python スクリプトが工程制御**、**AI が内容生成** に分離する。たとえば取材ステップは `core/clone_recon.py` のような新規スクリプトを置き、保存パスとセクション分割のしきい値はスクリプトが決める。

省トークン優先のため Playwright CLI を採用。MCP 版は省く。スクリプトの新設場所は本元リポジトリの `core/` 配下 (共通スコープ)。プロジェクト側で発火する形にする。

## RSRC-WEBCLONE-STORYBOOK.出典 — 出典

(参照日: 2026-04-11)

- [Dembrandt blackpaper](https://www.dembrandt.com/blackpaper) — 自動デザイントークン抽出 CLI
- [Superposition](https://superposition.design/) — GUI 製デザイントークン抽出
- [@projectwallace/css-design-tokens (GitHub)](https://github.com/projectwallace/css-design-tokens) — npm ライブラリ
- [Playwright MCP setup (Simon Willison TIL)](https://til.simonwillison.net/claude-code/playwright-mcp-claude-code) — Claude Code との接続手順
- [Playwright CLI: Token-Efficient Alternative (testcollab)](https://testcollab.com/blog/playwright-cli) — CLI vs MCP のトークン比較
- [Storybook Autodocs (公式)](https://storybook.js.org/docs/writing-docs/autodocs) — CSF + autodocs
- [screenshot-to-code (GitHub: abi)](https://github.com/abi/screenshot-to-code) — スクショ→コード OSS
- [JCodesMore/ai-website-cloner-template (GitHub)](https://github.com/JCodesMore/ai-website-cloner-template) — `/clone-website` テンプレート
- [ericshang98/Perfect-Web-Clone (GitHub)](https://github.com/ericshang98/perfect-web-clone) — DOM/CSS 方式マルチエージェント
- [Playwright VRT in Storybook (pow.rs)](https://pow.rs/blog/playwright-vrt/) — VRT 設定例
- [Visual tests (Storybook 公式)](https://storybook.js.org/docs/writing-tests/visual-testing) — Storybook の VRT
