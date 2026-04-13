# RSRC-WEBANIM-HARDCASE — 難所攻略: WebGL / 独自実装 / 複雑演出の別ルート

関連: RSRC-WEBANIM-CAPTURE, RSRC-WEBANIM-REPLAY
タグ: アニメーション, WebGL, シェーダ, 逆解析, WebGL API, getAttachedShaders, Spector, rrweb, 時間偽装, vision LLM, Lottie, Rive, pixelmatch, VRT, 差分ループ, hardcase, shader, reverse-engineer, time-virtualization, webgl-standard-api

## RSRC-WEBANIM-HARDCASE.概要 — 概要

CAPTURE / REPLAY で攻略しきれない 3 つの難所 — **(A) WebGL / シェーダ背景**, **(B) ライブラリ非使用の独自 JS 実装**, **(C) 複数レイヤが絡む複雑演出の微調整** — を別ルートから攻める。「ダメもとでも諦めない」スタンスで、単独では 100% 到達できなくても**組み合わせで実用レベルに持ち上げる**手筋を棚卸しする。

スコープ: 2025 H2 〜 2026 Q1。Spector.js / rrweb / Replit の deterministic capture / Gemini 2.5 Pro / Claude Sonnet 4.6 / Shader Web Background / Lottie JSON 抽出ツール / Playwright+pixelmatch を一次ソースに採用。

## RSRC-WEBANIM-HARDCASE.調査結果 — 調査結果

### 難所別の攻略ルートマップ

| 難所 | 第一ルート | 補完ルート | 最後の砦 |
|---|---|---|---|
| (A) WebGL シェーダ背景 | **Spector.js** で frame capture → GLSL ソース抽出 | Three.js シーン traverse (`window.__THREE__`) | Shadertoy 風 AI 生成 + 視覚差分ループ |
| (B) 独自 JS 実装 | **rAF / setTimeout / Date monkey-patch** で時間虚構化し決定的に取材 | `rrweb` 型 DOM 時系列記録 | Vision LLM (Gemini 2.5 Pro / Claude 4.6) で動画→コード生成 |
| (C) 複雑演出の微調整 | **VRT 差分自動修正ループ** (Playwright + pixelmatch + AI) | `rrweb` 録画で挙動正本化 | 手動最終詰め (Figma / Storybook 横並びレビュー) |

### 全ルートに共通する補助手筋

- **Lottie / Rive 検出** — 元サイトが `.lottie` / `.riv` を使っていれば、ファイル自体を DL すれば完全一致。検出は `<script>` URL + Wappalyzer 方式。
- **動画 + 時間虚構化** — Replit の「ブラウザにウソの時間を教える」法で、実再生より遅い重処理ページでもフレーム欠けなしに取材できる。
- **AI 自己修正ループ** — 差分スクショを LLM に渡して「原因の仮説 + 修正パッチ」を出させ、VRT 再実行で収束させる。100% ではないが 70% → 90% に引き上げる装置として機能。

## RSRC-WEBANIM-HARDCASE.技術詳細 — 技術詳細

### 1. WebGL 完全取材 — 標準 API 経由 (getAttachedShaders + getShaderSource)

**前提の転換 (2026-04-13 実測):** 当初は Babylon.js チームの `Spector.js` を standalone ライブラリとして Playwright から `addScriptTag` で流し込む設計だった。しかし実測したところ、Spector の capture は **描画フレームの call 列のみ** を記録し、初期化フェーズの `compileShader` / `shaderSource` / `linkProgram` は対象外だった (187 commands 中に shader init 呼び出し 0 件)。このため GLSL 原文の抽出には使えない。

代わりに **WebGL 標準 API (`getAttachedShaders` + `getShaderSource`)** で `CURRENT_PROGRAM` から直接取得する方式に切り替えた。副産物として CDN 依存も消え、オフラインで動作する。

```js
// Playwright で recon.mjs から呼ぶ spector.mjs の captureWebGLShaders
const shaders = await page.evaluate(() => {
  const canvases = [...document.querySelectorAll('canvas')];
  const programs = [];
  canvases.forEach((c, ci) => {
    let gl;
    try { gl = c.getContext('webgl2') || c.getContext('webgl'); } catch { return; }
    if (!gl) return;
    const prog = gl.getParameter(gl.CURRENT_PROGRAM);
    if (!prog) return;
    const attached = gl.getAttachedShaders(prog) || [];
    let vertex = null, fragment = null;
    for (const shader of attached) {
      const type = gl.getShaderParameter(shader, gl.SHADER_TYPE);
      const source = gl.getShaderSource(shader);
      if (!source) continue;
      if (type === gl.VERTEX_SHADER) vertex = source;
      else if (type === gl.FRAGMENT_SHADER) fragment = source;
    }
    if (vertex || fragment) {
      programs.push({ id: `canvas-${ci}-current`, canvasIndex: ci, vertexShader: vertex, fragmentShader: fragment });
    }
  });
  return { programs };
});
```

取れるもの:
- **CURRENT_PROGRAM の vertex / fragment shader ソース** (GLSL 原文、ミニファイされていない状態)
- **canvas ごとの寸法・WebGL バージョン** (`getContext('webgl2')` → `'webgl'` の順で判定)

取れないもの (制約):
- **複数 program を bind し分けるパイプラインの非アクティブ program** — 描画ループ最終フレームで `useProgram` された 1 本のみ抽出される
- **uniforms / textures / attributes の実値** — 構造は `gl.getActiveUniform` 等で取れるが、bind 済みの具体値は別系統
- **WebGPU** (`canvas.getContext('webgpu')`) — 別 API 系統 (今後対応)

これを `React Three Fiber` 側に移植するときは `shaderMaterial` の `vertexShader` / `fragmentShader` に GLSL をそのまま貼り、`uniforms` は元サイト側のコードヒント (`new THREE.Uniform(...)`) を参考に組み立てる。**Three.js RawShaderMaterial を使うサイトではここで 9 割再現できる。** 全 program 履歴が必要な場合は `addInitScript` で `WebGLRenderingContext.prototype.useProgram` をフックして全 bind 履歴を記録する拡張 (段階 4 以降) で対応する。

**(参考) Spector.js の位置付け:** 手動デバッグツールとしては依然強力 (frame 内の draw call 時系列 + textures + uniforms + VAO が網羅的に取れる)。取材自動化には向かないが、抽出した GLSL が動かないときの逆解析には使える。`core/clone_node/spector.mjs` のファイル名はこの経緯から歴史的名称として残している (中身は WebGL 標準 API 実装)。

### 2. rAF 時間偽装法 — 決定的フレーム取材

Replit が動画レンダラーで使った手筋。**`setTimeout` / `setInterval` / `requestAnimationFrame` / `Date` / `Date.now()` / `performance.now()` を全て monkey-patch** し、仮想時計で動かす。ブラウザは「実時間は 1 秒かかったが 16ms しか経っていない」と信じるので、重いページでも 60fps フレームを欠けなく取材できる。

```js
// ページコンテキスト注入 (Playwright page.addInitScript)
(() => {
  let vt = 0;                      // virtual time (ms)
  const rafQueue = [];
  const timeouts = [];

  window.Date = class extends Date { constructor(...a) { super(...(a.length ? a : [vt])); } };
  window.Date.now = () => vt;
  performance.now = () => vt;
  window.requestAnimationFrame = cb => { const id = rafQueue.length; rafQueue.push({ id, cb }); return id; };
  window.setTimeout = (cb, ms = 0) => { timeouts.push({ fireAt: vt + ms, cb }); };
  window.setInterval = (cb, ms = 0) => {
    const schedule = () => timeouts.push({ fireAt: vt + ms, cb: () => { cb(); schedule(); } });
    schedule();
  };

  // 外部から frame(dtMs) を呼んで進める
  window.__step__ = (dtMs) => {
    vt += dtMs;
    timeouts.filter(t => t.fireAt <= vt).forEach(t => t.cb());
    rafQueue.splice(0).forEach(r => r.cb(vt));
  };
})();
```

Playwright 側から `await page.evaluate(dt => window.__step__(dt), 1000/60)` でフレームを進め、毎ステップ後に `page.screenshot` + `getAnimations()` dump を取る。**ライブラリ非使用の rAF 手書きアニメでも、フレーム単位で数値が取れる。**

注意点:
- CSS アニメーションは仮想時計に追従しないため、`document.getAnimations().forEach(a => a.currentTime = vt)` で手動同期する
- ネイティブ video 要素は `video.currentTime = vt/1000` で同期
- Chrome の deterministic rendering (`chrome-headless-shell` + `--deterministic-mode`) を併用するとさらに安定

### 3. rrweb 型 DOM 時系列記録

`rrweb` はセッションリプレイ基盤として有名だが、**「動画より軽くて、動画より精確」に DOM 変化を再生できる** ため、アニメーション取材にも流用できる。

仕組み:

1. **Full snapshot** — 初回に DOM 全体をシリアライズし、ID → Node のマップを作る
2. **Incremental snapshots** — `MutationObserver` で attribute / childList / characterData を**タイムスタンプ付き** で記録。`attributeOldValue: true` + `attributeFilter: ['style', 'class', 'transform']` で必要属性だけ絞れる
3. **最適化** — 同一 callback 内で同属性が複数回変わったときは最終値だけ残す (textarea resize 等で効く)
4. **イベント** — マウス / スクロール / input も 20ms / 500ms で throttle しつつ時系列化

このフォーマットを取材結果として保存すれば:
- **正本** として再生可能 (検証 UI に流し込める)
- **LLM に食わせやすい構造化データ** (JSON の時系列)
- **差分比較** の基礎 (再現実装を同じスクリプトで rrweb 録画し、diff)

```js
import { record } from 'rrweb';
const events = [];
const stop = record({
  emit(ev) { events.push(ev); },
  recordCanvas: true,              // canvas 録画オプション
  sampling: { mousemove: 20, scroll: 100, input: 'all' },
  slimDOMOptions: 'all',
});
// ...取材シナリオ実行...
stop();
await fs.writeFile('rrweb.json', JSON.stringify(events));
```

### 4. Vision LLM による動画→コード生成

**Gemini 2.5 Pro** は動画直接入力対応 (20MB 未満) + VideoMME 84.8% で、「この動画の動きを p5.js で」プロンプトから実際にコードを吐ける実績あり。**Claude Sonnet 4.6** は GLSL シェーダ生成 / ポーティング / 最適化が得意 (ホログラム / ディゾルブ / スキャンライン系)。

運用パターン:

| 入力 | モデル | 出力 | 用途 |
|---|---|---|---|
| 元サイト録画 (10-30 秒) | Gemini 2.5 Pro | GSAP / Motion コード雛形 | 独自 JS 実装の初回案 |
| フレーム連番 (60-120 枚 JPEG) | Claude Sonnet 4.6 | GLSL fragment shader | WebGL 背景の近似再現 |
| 差分スクショ + 現行コード | Claude Sonnet 4.6 | 修正パッチ | VRT 差分ループ |
| rrweb events JSON | Claude Sonnet 4.6 | Motion `useTransform` LUT | スクロール連動マッピング変換 |

フレーム連番法 (video → JPEG × N → LLM) は 1M コンテキストなら 10 分動画クラスまで入る。`ffmpeg -i input.mp4 -vf fps=2 frame_%03d.jpg` で秒 2 枚抽出が実用ライン。

**限界**: どのモデルも「参考と**並べて区別付かない**」水準まで 1 発で出すのは難しい。しかし「70% の初稿を出して VRT ループで 90% に追い込む」には十分。

### 5. Lottie / Rive 検出と抽出

元サイトが `.lottie` (JSON) / `.riv` (バイナリ) を使っているなら**ファイル DL で完全一致**。

検出:
- ネットワーク: `*.json` で `{ "v": "5.", "layers": [...], "assets": [...] }` パターンは Lottie
- `<script src>`: `lottie-web`, `@lottiefiles/*`, `@rive-app/canvas`, `rive-wasm`
- グローバル: `window.lottie`, `window.rive`
- DOM: `lottie-player`, `rive-canvas` カスタム要素

Playwright で:

```js
const lottieUrls = [];
page.on('response', async r => {
  const url = r.url();
  if (/\.(json|lottie|riv)(\?|$)/.test(url)) {
    const buf = await r.body().catch(() => null);
    if (buf) lottieUrls.push({ url, size: buf.length, buf });
  }
});
await page.goto(target);
```

取れたら `@lottiefiles/react-lottie-player` / `@rive-app/react-canvas` で React 側に埋め込み。MiroMiro 等の専用ツールもあるが、取材自動化には Playwright 直で十分。

### 6. AI によるシェーダ生成と Shadertoy 互換基盤

Spector.js でも取れないブラックボックス背景は、**視覚特性から逆算で AI にシェーダを書かせる**。

- Claude Sonnet 4.6 / Opus 4.6 は GLSL fragment shader を Shadertoy 形式で書ける (`void mainImage(out vec4 fragColor, in vec2 fragCoord)`)
- 実行基盤は [`shader-web-background`](https://github.com/xemantic/shader-web-background) が最短 — Shadertoy 互換 + 複数パス + FBO 対応。WebGL1/2 の差分も吸収してくれる
- 初稿 → スクショ → 目視 or pixelmatch 差分 → 修正プロンプト のループを 5 周程度回すと粒子 / ノイズ / グロー系は目視で区別つかないレベルまで寄る

```tsx
import shaderWebBackground from 'shader-web-background';
shaderWebBackground.shade({
  shaders: {
    image: { uniforms: { iTime: (gl, loc) => gl.uniform1f(loc, performance.now()/1000) } }
  }
});
```

限界: 物理ベースのボリューメトリック系 / 明示的な 3D シーンは無理。そこは R3F + 手動モデリング領域。

### 7. VRT 差分自動修正ループ

Playwright の toHaveScreenshot() は内部で pixelmatch を使い、1280x720 なら <50ms で diff 画像を返す。この出力を LLM に渡して自己修正する。

ループ:

```
1. Playwright で元サイト録画 (frames_ref/*.png)
2. Playwright で自作サイト録画 (frames_now/*.png)
3. pixelmatch で per-frame diff (frames_diff/*.png)
4. 差分が閾値超のフレームとコードを LLM に渡す
5. LLM がパッチ生成 → 適用
6. 1 に戻る (収束 or 上限ラウンド到達まで)
```

設定:
- `threshold: 0.1` (色許容) + `maxDiffPixels: 100` くらいから始める
- 動きの最中は必ず diff が出るので、`animations: 'allow'` + **同一仮想時刻でのフレーム対** を比較する (時間偽装法と併用)
- 大きい全体差分が出たら「イージング違い」の可能性大 → LLM に渡すコンテキストにイージング候補を入れる
- 小さい点在差分 → サブピクセルのアンチエイリアス。`threshold: 0.2` で許容

この装置は **100% を目指すものではない**。「AI が 80% 出す → ループで 95% に詰める」装置として使う。最後の 5% は人手で詰めるか諦める。

## RSRC-WEBANIM-HARDCASE.比較 — 比較・選択肢

### 取れるものと限界

| 手法 | 強み | 弱み | コスト |
|---|---|---|---|
| WebGL 標準 API (getAttachedShaders) | CURRENT_PROGRAM の GLSL 抽出、CDN 依存なし | 最終 program のみ、WebGPU 非対応、独自 binary 不可 | 低 (Playwright の evaluate 1 回) |
| 時間偽装 (rAF patch) | ライブラリ非依存、決定的 | Web Worker / OffscreenCanvas で漏れる | 中 (init script 注入) |
| rrweb | 軽量な動作正本 | WebGL/canvas は別録画オプション必要 | 低 (公式ライブラリ) |
| Vision LLM (動画→コード) | 独自実装の初稿生成 | 厳密な数値一致は不保証 | 中〜高 (API 呼出コスト) |
| Lottie/Rive 検出 | 完全一致 | 使っていないサイトには無力 | 低 |
| AI シェーダ生成 | ブラックボックス背景の近似 | 物理ベース系は限界 | 中 (反復コスト) |
| VRT 差分ループ | 精度の最後の詰め | 収束しない場合あり | 中 (Playwright + LLM) |

### 組み合わせ推奨

- **WebGL ありサイト** → WebGL 標準 API (getAttachedShaders) + R3F 移植 + VRT ループ
- **ライブラリ不明サイト** → 時間偽装 + rrweb + Vision LLM 初稿 + VRT ループ
- **Lottie/Rive 使用サイト** → DL + 埋込 (単純一致)
- **複雑多層演出** → rrweb 正本 + 時間偽装取材 + VRT ループ多段

単独手法は必ず穴がある。**穴が違う手法を重ねる** のが要点。

## RSRC-WEBANIM-HARDCASE.適用 — プロジェクトへの適用

本元 (エル子) の `core/clone.py` / `clone_node/recon.mjs` / 新規 `clone_node/capture.mjs` への拡張方針:

1. **WebGL 標準 API で recon のサブステップとして取材** — `hasWebGL: true` 判定後に `getAttachedShaders` + `getShaderSource` で CURRENT_PROGRAM の GLSL を抽出し、`shaders.json` を `.libs/storybook/<slug>/webgl/` に保存。build 雛形が R3F + shaderMaterial を生成する。**(段階 2 で導入済み — SLOG-20260413-003)**
2. **`clone_node/time-virtualize.mjs`** を新規追加 — Playwright `addInitScript` で仮想時計を注入する独立モジュール。通常 recon と deterministic recon の 2 モードを切替可能に。
3. **rrweb 録画を recon 標準に** — DOM 時系列が JSON で取れるので、その場で `scroll-samples.json` を拡張する形。`rrweb.json` を保存し、apply 工程が「元サイトの動きをどこまで残すか」の判断材料に使う。
4. **Lottie / Rive 自動検出** — `page.on('response')` で `.json` / `.riv` を拾い、ファイル本体を `.libs/storybook/<slug>/assets/` に保存。本棚ページに `採用ライブラリ: Lottie` と書かれたら build は `@lottiefiles/react-lottie-player` 雛形を出す。
5. **VRT 差分ループを `/codi` の verification ステップに追加** — 現行 VRT は baseline 比較のみ。**元サイト vs 再現** の差分計測ステップを追加し、閾値超なら AI 修正を提案ループする。ループ上限は 5 周 (無限ループ回避)。
6. **Vision LLM 呼出をフェイルセーフ扱いに** — 既定は無効。取材が失敗 (WebGL 抽出不可 / 独自実装で rrweb も穴だらけ) のときだけフォールバックとして起動する。コスト制御のため `--llm-fallback` フラグで明示オプトイン。
7. **`採用ライブラリ` に複数許容** — 元サイトが GSAP + Lenis + R3F + Lottie 併用の場合、全部入りの雛形を出す。引き算は apply で行う。

実装は別タスクとして TP で扱う。本ページは難所攻略のルート探索の根拠を固定する。

## RSRC-WEBANIM-HARDCASE.出典 — 出典

- Spector.js — [GitHub BabylonJS/Spector.js](https://github.com/BabylonJS/Spector.js/) (参照: 2026-04-13)
- Spector.js — [Real-Time Rendering: Debugging WebGL with SpectorJS](https://www.realtimerendering.com/blog/debugging-webgl-with-spectorjs/) (参照: 2026-04-13)
- Replit Blog — [We Built a Video Rendering Engine by Lying to the Browser About What Time It Is](https://blog.replit.com/browsers-dont-want-to-be-cameras) (参照: 2026-04-13)
- rrweb — [observer.md](https://github.com/rrweb-io/rrweb/blob/master/docs/observer.md) (参照: 2026-04-13)
- MDN — [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver), [MutationObserver.observe()](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver/observe) (参照: 2026-04-13)
- Google Developers — [Advancing the frontier of video understanding with Gemini 2.5](https://developers.googleblog.com/en/gemini-2-5-video-understanding/) (参照: 2026-04-13)
- Simon Willison — [Feed a video to a vision LLM as a sequence of JPEG frames](https://simonw.substack.com/p/feed-a-video-to-a-vision-llm-as-a) (参照: 2026-04-13)
- Claude Sonnet 4.6 — [Review (Medium)](https://medium.com/@leucopsis/claude-sonnet-4-6-review-e01cc9d31273), [Unity × Claude Code shader workflow](https://claudelab.net/en/articles/claude-code/unity-claude-code-advanced-workflow) (参照: 2026-04-13)
- Rive / Lottie — [Rive vs Lottie](https://rive.app/blog/rive-as-a-lottie-alternative), [MiroMiro Lottie Extractor](https://miromiro.app/features/lottie-extractor) (参照: 2026-04-13)
- Shader Web Background — [GitHub xemantic/shader-web-background](https://github.com/xemantic/shader-web-background) (参照: 2026-04-13)
- Playwright + Pixelmatch — [Visual Regression Testing Guide 2026 (Bug0)](https://bug0.com/knowledge-base/playwright-visual-regression-testing) (参照: 2026-04-13)
