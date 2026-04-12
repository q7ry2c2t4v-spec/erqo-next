# RSRC-WEBANIM-CAPTURE — 参考サイトのアニメーションを AI が忠実に取材する手法

関連: RSRC-WEBANIM-REPLAY, RSRC-WEBANIM-HARDCASE, RSRC-WEBCLONE-PIPELINE, RSRC-WEBCLONE-STORYBOOK
タグ: アニメーション, エフェクト, 解析, 取材, スクロール連動, パララックス, DevTools, WAAPI, Playwright, CDP, ライブラリ検出, animation, effect, capture, reverse-engineering, scroll-linked, parallax, cubic-bezier

## RSRC-WEBANIM-CAPTURE.概要 — 概要

本ページは「任意のウェブサイトで動いているアニメーション / エフェクト (スライダー、スクロール連動、パララックス、WebGL 等) を AI が **数値レベルで** 解析し、後工程 (REPLAY) で **参考サイトと並べて区別が付かない** 精度で再現するための取材手順」をまとめる。

忠実性が最重要。「だいたい動く」で妥協しない。イージング曲線・タイミング・進捗マッピング・ライブラリ種別まで全て数値化して REPLAY に引き渡す。既存の `core/clone.py` recon サブステップの拡張方針としても機能する。

情報収集範囲: 2025 H2 〜 2026 Q1。公式仕様 (W3C / WHATWG / MDN) と主要ライブラリの公式ドキュメントを一次ソースに採用。

## RSRC-WEBANIM-CAPTURE.調査結果 — 調査結果

忠実取材は 6 レイヤの複合で成立する。単独手法では必ず取りこぼしが出る。

1. **ライブラリ同定** — スクリプト URL パターン + グローバル変数検出で `GSAP / Motion / Lenis / Locomotive / Three.js / OGL / Splide / Swiper` などを特定。再現側で「同じライブラリを選ぶ」判断の根拠になる。
2. **WAAPI ランタイム取材** — `element.getAnimations({subtree:true})` で CSS Animations / Transitions / WAAPI / ScrollTimeline / ViewTimeline すべてを統一的に列挙。`getComputedTiming()` で duration / delay / easing / iterations をミリ秒単位で取得。
3. **CDP Animation ドメイン** — `Animation.enable` + `animationCreated` / `animationStarted` イベントでページ全体の発火タイミングを時系列で記録。ユーザー入力不要で自動取材可能。
4. **DevTools Animations パネル (手動補助)** — 視覚的に cubic-bezier を抽出できる最後の砦。自動では取りこぼすトランジションの確認に使う。
5. **スクロール進捗マッピング抽出** — `IntersectionObserver` / `scroll` / `scrollend` を仕込み、`scrollY` → `transform / opacity / filter` のサンプリングを間引きなしで取得 (後で多項式フィッティング or LUT 化)。
6. **視覚トレース** — フレーム連番スクショ + 動画キャプチャで「ライブラリが検出できなかったブラックボックス」や「Shader / Canvas」を視覚側から再現材料にする。

## RSRC-WEBANIM-CAPTURE.技術詳細 — 技術詳細

### 1. ライブラリ同定

**スクリプト URL パターン (Wappalyzer 方式):**

| ライブラリ | `<script src>` パターン | グローバル変数 |
|---|---|---|
| GSAP | `gsap.min.js`, `gsap/dist/*`, `TweenMax` | `window.gsap`, `window.ScrollTrigger` |
| Motion (旧 Framer Motion) | `motion`, `framer-motion` | `window.Motion` (UMD), バンドル内 |
| Lenis | `lenis`, `@studio-freight/lenis` | `window.Lenis` (UMD), data 属性 `data-lenis-prevent` |
| Locomotive Scroll | `locomotive-scroll` | `window.LocomotiveScroll`, DOM `data-scroll` |
| Three.js | `three.min.js`, `three/build/*` | `window.THREE` |
| Swiper / Splide | `swiper-bundle`, `splide.min.js` | `window.Swiper`, `window.Splide` |

Wappalyzer は HTML / `script src` / HTTP ヘッダ / cookie / グローバル変数の 5 種を正規表現で照合する (src/technologies/ のパターン DB)。同じ戦略を Playwright + `page.evaluate` で実装できる。

```js
// Playwright で取材
const detected = await page.evaluate(() => {
  const out = { globals: [], scripts: [] };
  const keys = ['gsap','ScrollTrigger','Motion','Lenis','LocomotiveScroll','THREE','Swiper','Splide'];
  for (const k of keys) if (window[k]) out.globals.push(k);
  for (const s of document.scripts) if (s.src) out.scripts.push(s.src);
  return out;
});
```

### 2. WAAPI ランタイム取材 — `element.getAnimations()`

ブラウザが内部で動かしている **全てのアニメーション** (CSS Animations / CSS Transitions / JS の `element.animate()` / `ScrollTimeline` / `ViewTimeline`) を 1 つの API で列挙できる。Baseline widely available (2020-07〜)。

```js
const animations = document.documentElement.getAnimations({ subtree: true });
const dump = animations.map(a => {
  const eff = a.effect; // KeyframeEffect | null
  const t = eff?.getComputedTiming?.() ?? {};
  return {
    target: eff?.target?.outerHTML?.slice(0, 200),
    duration: t.duration,        // ミリ秒 or "auto"
    delay: t.delay,              // ミリ秒
    endDelay: t.endDelay,
    iterations: t.iterations,
    easing: t.easing,            // "linear" / "cubic-bezier(.17,.67,.83,.67)" / "steps(5, end)"
    direction: t.direction,
    fill: t.fill,
    keyframes: eff instanceof KeyframeEffect ? eff.getKeyframes() : null,
    playState: a.playState,
    timeline: a.timeline?.constructor?.name  // DocumentTimeline / ScrollTimeline / ViewTimeline
  };
});
```

取材タイミングが重要: ページロード直後だけでなく、**マウス操作・スクロール・hover・click をスクリプトで発火させた直後** にも dump を取る。イントロ以外のインタラクションアニメはトリガ後にしか登場しない。

### 3. Chrome DevTools Protocol — Animation ドメイン

CDP の `Animation` ドメインは CSS Animation / Transition / WAAPI を **ブラウザ側の視点で一括監視** できる。Playwright の CDPSession 経由で叩ける:

```js
const client = await page.context().newCDPSession(page);
await client.send('Animation.enable');
await client.send('Animation.setPlaybackRate', { playbackRate: 1 });
client.on('Animation.animationCreated', e => log.push({ kind: 'created', ...e }));
client.on('Animation.animationStarted', e => log.push({ kind: 'started', ...e.animation }));
client.on('Animation.animationCanceled', e => log.push({ kind: 'canceled', ...e }));
```

`animation.source.keyframesRule.keyframes` で keyframe ごとの `offset` / `easing` / `style` が取れる。WAAPI 側に現れない内部管理アニメーション (例: Chrome のスクロールアンカリング) もここで見える。

### 4. Chrome DevTools Animations パネル (手動補助)

`More tools > Animations` で:
- トリガ後のアニメを自動キャプチャしタイムラインに並べる
- タイムラインを 10-50% でスロー再生 (再現検証用)
- Styles タブから cubic-bezier アイコンをクリックすると `cubic-bezier(x1,y1,x2,y2)` 値を直接コピーできる

自動取材で失敗した 1-2 箇所の「肉眼で合わせる」作業の最後の砦。通常は WAAPI + CDP で十分。

### 5. Playwright 自動取材パイプライン

```js
// 1. ページ初期化（reduced-motion 無効で実物の動きを取る）
await page.emulateMedia({ reducedMotion: 'no-preference' });
await page.goto(url, { waitUntil: 'load' });

// 2. ライブラリ同定
const libs = await page.evaluate(detectLibs);

// 3. 初期 WAAPI dump
const initial = await page.evaluate(dumpAnimations);

// 4. CDP Animation 監視
const client = await page.context().newCDPSession(page);
await client.send('Animation.enable');
const cdpLog = [];
client.on('Animation.animationStarted', e => cdpLog.push(e.animation));

// 5. スクロール連動サンプリング
const scrollSamples = await page.evaluate(async () => {
  const h = document.documentElement.scrollHeight;
  const out = [];
  for (let y = 0; y <= h; y += h / 120) {
    window.scrollTo(0, y);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    const targets = document.querySelectorAll('[data-anim], section, [class*="parallax"], [class*="reveal"]');
    const frame = [...targets].map(el => {
      const cs = getComputedStyle(el);
      return { sel: el.tagName + '.' + el.className, transform: cs.transform, opacity: cs.opacity, filter: cs.filter };
    });
    out.push({ y, frame });
  }
  return out;
});

// 6. スクショ連番（視覚トレース）
for (let i = 0; i < 60; i++) {
  await page.screenshot({ path: `frames/${String(i).padStart(3,'0')}.png`, animations: 'allow' });
  await page.waitForTimeout(100);
}

// 7. 動画
await page.video()?.path();
```

`animations: 'allow'` は Playwright 1.20+ で追加。デフォルトは `disabled` で動きが止まるため **取材時は明示的に allow** する (VRT 時は逆に disabled)。

### 6. スクロール連動マッピングの抽出

「`scrollY` が X のとき、ある要素の `translateY` / `opacity` / `filter` がどう変化するか」を取り切れば、REPLAY 側で `useTransform` / ScrollTrigger `scrub` / `animation-timeline` のどれを選んでも再現できる。

- **サンプリング粒度**: ページ高さの 120 分割程度で十分 (120 段階あればグラフとして 1px 以下の誤差で再現可能)
- **安定化**: `requestAnimationFrame` を 2 回待ってから `getComputedStyle` を読む (Paint 完了後)
- **後処理**: `(scrollY, 値)` の配列を REPLAY 側で以下のどれかに変換:
  - **線形区間**: `useTransform(progress, [0, 0.5, 1], [0, -100, -200])` のキーフレーム化
  - **三次曲線**: cubic-bezier 1 本で近似できる場合は易しい
  - **LUT**: 複雑すぎる場合は値テーブルを JSON で持ち、補間関数で参照
- **進捗の基準**: ページ全体の `scrollY` か、要素の `IntersectionObserver` 進捗 (要素ベースの場合は Motion の `useScroll({target, offset:["start end", "end start"]})` と対応)

### 7. WebGL / Canvas 取材

DOM に出ないエフェクト (ヒーローのパーティクル、シェーダ背景等) は別取材:

- `document.querySelectorAll('canvas')` を列挙し、`getContext('webgl2') || getContext('webgl')` が取れるか確認
- `canvas.getContext('webgl2').getSupportedExtensions()` と `getParameter(gl.SHADING_LANGUAGE_VERSION)` で環境把握
- `WEBGL_debug_shaders` 拡張 (`getTranslatedShaderSource`) が使えるとコンパイル済 GLSL が抜ける (Chrome 開発者モード限定、通常サイトは不可のケース多)
- Three.js (`window.THREE`) / OGL / Babylon.js 使用時は **バンドル済ミニファイ JS を読むより、scene を walk する** ほうが速い: `window.__SCENE__?.traverse(o => ...)`
- 取れない場合は **動画 + フレームごとのカラーヒストグラム** を記録し、REPLAY 側で Shader から近似再現 (ShaderToy 互換パターン)

## RSRC-WEBANIM-CAPTURE.比較 — 比較・選択肢

| 手法 | 取れるもの | 取れないもの | 信頼度 |
|---|---|---|---|
| `getAnimations()` | WAAPI / CSS 全般、ScrollTimeline | requestAnimationFrame で手書きの JS 駆動、WebGL | 高 |
| CDP Animation | ブラウザ内部管理のアニメ全般 | JS 駆動 (setInterval / rAF)、WebGL | 高 |
| `getComputedStyle` サンプリング | スクロール連動の値マッピング | 瞬間変化、WebGL | 中 (粒度依存) |
| DevTools Animations パネル | cubic-bezier 視覚抽出 | 自動化不可 (手動) | 補助 |
| スクショ / 動画 | 全部 (視覚だけ) | 数値そのもの | 低 (目で合わせる) |
| Wappalyzer 方式同定 | ライブラリ種別 | カスタム実装 | 中〜高 |

**推奨: 全部重ねる。** 単独手法は必ず穴があり、忠実性の要件を満たせない。

## RSRC-WEBANIM-CAPTURE.適用 — プロジェクトへの適用

本元 (エル子) の `core/clone.py` recon サブステップ / `clone_node/recon.mjs` の拡張指針:

1. **recon.mjs に `detectLibs()` 追加** — 現行は DOM + スクショのみ。Wappalyzer 方式の `script src` + グローバル検出を追加し、「採用ライブラリ宣言」を `<slug>.md` に書き出す。REPLAY で `/codi` 実装時にライブラリ選定の根拠になる。
2. **`dumpAnimations()` を recon 標準化** — `getAnimations({subtree:true})` の結果を JSON で `.libs/storybook/<slug>/animations.json` に保存。本棚ページで参照する。
3. **CDP Animation ログ保存** — recon 中に `Animation.enable` で監視し、トリガ時系列を `cdp-animations.ndjson` に記録。
4. **スクロールサンプリング統合** — 現状の recon 2 解像度スクショに加え、ページ高さ 120 分割での `getComputedStyle` サンプリングを `scroll-samples.json` に保存。apply 工程が「要望反映時にどこまで元の動きを保つか」を判断できる材料にする。
5. **WebGL 検出ゲート** — `<canvas>` + WebGL context があれば本棚ページに `hasWebGL: true` フラグを立て、REPLAY 側で React Three Fiber / OGL を初期選択肢にする分岐を用意。
6. **`reducedMotion: 'no-preference'`** — recon 時のみ強制。`/codi` VRT baseline では `'reduce'` のままにする (既存の `baseline.mjs` の挙動と競合しない)。

コード実装は別タスクとして TP で扱う。本ページはあくまで方針と根拠を固定する。

## RSRC-WEBANIM-CAPTURE.出典 — 出典

- Chrome for Developers — [Animations: Inspect and modify CSS animation effects](https://developer.chrome.com/docs/devtools/css/animations) (参照: 2026-04-13)
- Chrome DevTools Protocol — [Animation domain](https://chromedevtools.github.io/devtools-protocol/tot/Animation/) (参照: 2026-04-13)
- MDN — [Element: getAnimations() method](https://developer.mozilla.org/en-US/docs/Web/API/Element/getAnimations) (参照: 2026-04-13)
- MDN — [Using the Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API) (参照: 2026-04-13)
- MDN — [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) (参照: 2026-04-13)
- Playwright docs — [Auto-waiting](https://playwright.dev/docs/actionability), [Visual comparisons](https://playwright.dev/docs/test-snapshots) (参照: 2026-04-13)
- The Green Report — [Automating Animation Testing with Playwright](https://www.thegreenreport.blog/articles/automating-animation-testing-with-playwright-a-practical-guide/automating-animation-testing-with-playwright-a-practical-guide.html) (参照: 2026-04-13)
- Wappalyzer — [GitHub リポジトリ (検出パターン DB)](https://github.com/tomnomnom/wappalyzer) (参照: 2026-04-13)
- MDN — [Detect WebGL](https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/By_example/Detect_WebGL) (参照: 2026-04-13)
