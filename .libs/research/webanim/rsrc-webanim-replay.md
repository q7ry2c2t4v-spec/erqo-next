# RSRC-WEBANIM-REPLAY — Next.js でアニメーションを忠実に再現する実装パターン

関連: RSRC-WEBANIM-CAPTURE, RSRC-WEBANIM-HARDCASE, RSRC-WEBCLONE-RULES, RSRC-NEXTJS-ARCH
タグ: アニメーション, 再現, Motion, Framer Motion, GSAP, ScrollTrigger, Lenis, View Transitions, scroll-timeline, Next.js, React, Three Fiber, animation, replay, useGSAP, useScroll, parallax, scroll-driven

## RSRC-WEBANIM-REPLAY.概要 — 概要

CAPTURE で取材した数値 (ライブラリ種別 / duration / easing / スクロール進捗マッピング / Keyframes / WebGL 有無) を **Next.js 15+ の App Router プロジェクト上で参考サイトと区別の付かないレベルで再現** するための実装パターン集。

選定原則は **「元サイトと同じライブラリを使う」**。Framer Motion で GSAP を無理に代用しない。ここでの「忠実」は見た目だけでなく、タイミング特性 (慣性 / オーバーシュート / スクラブ遅延) まで含む。

スコープ: Next.js 15 (App Router) / React 19 / Tailwind v4。2025 H2 〜 2026 Q1 の公式ドキュメント状況に準拠。

## RSRC-WEBANIM-REPLAY.調査結果 — 調査結果

### 使い分けマトリックス

| 参考サイトの特徴 | 第一選択 | 備考 |
|---|---|---|
| スクロール連動のみ (慣性不要) | **CSS Scroll-Driven Animations** | `animation-timeline: scroll()` / `view()`。コンポジタ駆動で最速 |
| 慣性スムーススクロール (Locomotive / Lenis 系の挙動) | **Lenis** + ScrollTrigger | `duration: 1.2s` `easing` 既定値で近似。必要なら取材値で上書き |
| 複雑なタイムライン / Pin / ScrollSmoother / SVG モーフ | **GSAP + ScrollTrigger** (`useGSAP`) | 参考サイトが GSAP を使っていたら迷わずこれ |
| React コンポーネントの入退場 / gesture / layout | **Motion for React** (`motion/react`) | Framer Motion の後継。`whileInView` / `useScroll` |
| ページ間トランジション | **View Transitions API** | Next.js 15.2+ `viewTransition: true` |
| WebGL / 3D / シェーダ背景 | **React Three Fiber** (+ drei / postprocessing) | Three.js のシーンをそのまま移植 |
| スライダー / カルーセル | 元が Swiper/Splide → 同じものを採用 | 独自実装での再現は基本非推奨 |

### 重要な 2026 時点の状況

- `framer-motion` は 2024 末に **`motion`** にリブランド。import は `motion/react`。Motion for React は内部で `ScrollTimeline` を検出してネイティブ駆動に切り替える (ハードウェアアクセラレーション) ため、新 API の恩恵をそのまま受けられる。
- CSS Scroll-Driven Animations は Chrome/Edge 115+, Safari 17.4+ 対応。Firefox は flag 付き。**Baseline 未到達** だが主要ブラウザでは使える。未対応環境は `@supports not` でフォールバック必須。
- Next.js 15.2 で `next.config.js` の `experimental.viewTransition: true` が入り、App Router でも View Transitions を使える。
- `@gsap/react` の `useGSAP` が App Router での **事実上の必須** (cleanup / 重複登録問題を自動解決)。

## RSRC-WEBANIM-REPLAY.技術詳細 — 技術詳細

### 1. Motion for React (旧 Framer Motion)

```bash
npm i motion
```

```tsx
"use client";
import { motion, useScroll, useTransform, useMotionValueEvent } from "motion/react";

export function Parallax() {
  const ref = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"], // 要素が画面に入りきる〜抜けきる
  });
  // 取材した LUT をそのまま入れる
  const y = useTransform(scrollYProgress, [0, 1], [0, -200]);
  const opacity = useTransform(scrollYProgress, [0, 0.1, 0.9, 1], [0, 1, 1, 0]);

  useMotionValueEvent(scrollYProgress, "change", v => { /* 検証用ログ */ });

  return <motion.div ref={ref} style={{ y, opacity }}>…</motion.div>;
}
```

- **`useScroll`** が返すのは MotionValue 4 種 (`scrollX / scrollY / scrollXProgress / scrollYProgress`)。target を渡すと要素相対、省略で window 相対。
- **`useTransform`** で `[入力範囲] → [出力範囲]` の補間。3 点以上で非線形カーブを表現できる。取材 LUT の離散値をそのまま差し込める。
- **`whileInView`** / `useInView` は IntersectionObserver を pooled で共有するため大量要素でも軽い。
- **必ず `"use client"`**。Server Component では動かない。

### 2. GSAP + ScrollTrigger + `useGSAP`

```bash
npm i gsap @gsap/react
```

```tsx
"use client";
import { useRef } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(useGSAP, ScrollTrigger);

export function PinnedSection() {
  const root = useRef<HTMLDivElement>(null);

  useGSAP(() => {
    gsap.to(".layer", {
      yPercent: -50,
      ease: "none", // スクラブ時は linear 推奨
      scrollTrigger: {
        trigger: root.current,
        start: "top top",
        end: "+=1200",
        scrub: 0.5,   // 慣性を入れたいとき。取材値に合わせる
        pin: true,
        anticipatePin: 1,
      },
    });
  }, { scope: root, revertOnUpdate: true });

  return <div ref={root}><div className="layer">…</div></div>;
}
```

- **`useGSAP(fn, { scope, dependencies, revertOnUpdate })`** が cleanup を全て面倒見る。`scope` を渡すと内部の `gsap.to(".layer")` がそのスコープに閉じる (名前衝突回避)。
- **`ScrollTrigger.refresh()`** は画像 load 後など高さが変わった時に呼ぶ。Next.js の Suspense / 遅延読み込みと併用時は必須。
- **プラグインの登録はグローバルで 1 回** (`providers.tsx` の `"use client"` コンポーネントで `gsap.registerPlugin(...)`)。
- **Scrub 値**: `true`=即座追従 / 数値=秒単位の慣性遅延。取材動画でラグが見えるなら `0.5〜1.5` 相当。

### 3. Lenis (ReactLenis + useLenis)

```bash
npm i lenis
```

```tsx
"use client";
import { ReactLenis, useLenis } from "lenis/react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useEffect } from "react";

const LENIS_OPTIONS = {
  duration: 1.2,          // デフォルト。取材値があれば上書き
  easing: (t: number) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // expo-out
  smoothWheel: true,
  touchMultiplier: 1,
};

export function LenisProvider({ children }: { children: React.ReactNode }) {
  return <ReactLenis root options={LENIS_OPTIONS}>{children}</ReactLenis>;
}
```

GSAP ScrollTrigger との同期 (公式推奨):

```tsx
const lenis = useLenis(ScrollTrigger.update);
useEffect(() => {
  gsap.ticker.add(t => lenis?.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
}, [lenis]);
```

- `root` prop で `html` / `body` のスクロールを置き換え。ネストしたスクロールコンテナを避けたいとき用。
- **Motion for React とも併用可**。Motion 側の `useScroll` は `window` スクロールイベントを購読するだけなので、Lenis が駆動していても数値は正しく取れる。
- スクロールを止めたい要素 (モーダル内スクロール等) には `data-lenis-prevent`。

### 4. CSS Scroll-Driven Animations

JS ゼロで scroll/view に連動する。コンポジタ駆動で最速。単純なパララックス・進捗バー・リビールはこれで十分。

```css
/* 進捗バー */
body { scroll-timeline: --page block; }
.progress {
  position: fixed; inset: 0 auto auto 0; height: 4px; background: #fff;
  transform-origin: left;
  animation: bar linear;
  animation-timeline: --page;
}
@keyframes bar { from { transform: scaleX(0); } to { transform: scaleX(1); } }

/* 要素単位のリビール */
.card {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 40%; /* 入り始め〜40% 通過 */
}
@keyframes reveal {
  from { opacity: 0; transform: translateY(40px); }
  to   { opacity: 1; transform: translateY(0);    }
}

/* フォールバック */
@supports not (animation-timeline: view()) {
  .card { opacity: 1; transform: none; } /* or IntersectionObserver で代替 */
}
```

- `animation-range` キーワード: `cover` / `entry` / `exit` / `contain` / `entry-crossing` / `exit-crossing`。取材した「開始/終了 scrollY」をこれに変換する。
- **Baseline 未到達** (2026-04 時点)。Firefox flag。プロジェクト要件で IE/旧 Firefox を切れるなら採用、切れないなら JS ライブラリ経由が安全。

### 5. View Transitions API (Next.js 15.2+)

```ts
// next.config.ts
export default { experimental: { viewTransition: true } };
```

```tsx
"use client";
import { unstable_ViewTransition as ViewTransition } from "react";

<ViewTransition>
  <Image src={hero} alt="" />
</ViewTransition>
```

CSS で名前付きトランジション:

```css
::view-transition-old(hero),
::view-transition-new(hero) { animation-duration: 400ms; animation-timing-function: cubic-bezier(.22,1,.36,1); }
```

- 同一ドキュメント内 (SPA 風) は全モダンブラウザ対応。**クロスドキュメント** (`@view-transition { navigation: auto; }`) は Chrome 126+, Edge 126+, Safari 18.2+。Firefox 未対応。
- Next.js App Router では `next-view-transitions` (shuding) または `unstable_ViewTransition` どちらかを選ぶ。前者は安定、後者は React 公式に寄せる実験実装。
- モーション酔い対策で `@media (prefers-reduced-motion)` の 0 duration を必ず書く。

### 6. WebGL / 3D — React Three Fiber

```bash
npm i three @react-three/fiber @react-three/drei
```

```tsx
"use client";
import { Canvas, useFrame } from "@react-three/fiber";
import { useRef } from "react";

function Shader() {
  const mat = useRef<THREE.ShaderMaterial>(null);
  useFrame(({ clock }) => { if (mat.current) mat.current.uniforms.uTime.value = clock.elapsedTime; });
  return (
    <mesh>
      <planeGeometry args={[2, 2]} />
      <shaderMaterial ref={mat} uniforms={{ uTime: { value: 0 } }} vertexShader={vs} fragmentShader={fs} />
    </mesh>
  );
}
```

- DOM 要素と混ぜる場合は Canvas を `position: fixed; inset: 0; z-index: -1;` で背景に敷き、`drei` の `<ScrollControls>` で DOM スクロールと同期する。
- 取材した動画の視覚特性 (粒子の動き / ノイズ / 歪み) を元に `fragmentShader` を組む。ShaderToy 互換 (`iTime` / `iResolution` / `iMouse`) を uniform で流し込むと再現検索が効く。
- Next.js では **必ず Client Component**。`ssr: false` の dynamic import でフォールバック SVG を出すと Lighthouse が嫌がらない。

### 7. スライダー / カルーセル

参考サイトが Swiper / Splide を使っていたら **同じものを使う**。カスタム実装で慣性・スナップ・アクセシビリティを一致させるのは割に合わない。

```bash
npm i swiper
```

```tsx
"use client";
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation, Pagination, EffectFade, Autoplay } from "swiper/modules";
```

取材時に `window.Swiper` の params (speed / effect / loop / autoplay.delay) を読めばそのまま移植できる。

## RSRC-WEBANIM-REPLAY.比較 — 比較・選択肢

| 比較軸 | Motion for React | GSAP + ScrollTrigger | Lenis | CSS scroll-timeline |
|---|---|---|---|---|
| ランタイム | ~32KB gzip | ~23KB gzip (コア) | ~3KB gzip | 0 |
| スクロール連動 | `useScroll` + `useTransform` | `scrollTrigger: { scrub }` | 自前 (ScrollTrigger 必要) | `animation-timeline` |
| Pin / 複雑タイムライン | 弱い | 最強 | N/A | 弱い |
| React 入退場 | 最強 (`whileInView`) | 可 (`useGSAP`) | N/A | `view()` で可 |
| ハードウェア加速 | `ScrollTimeline` 自動検出 | 手動 (`will-change`, `force3D`) | CSS transform に委譲 | コンポジタ駆動 |
| Next.js SSR 相性 | `"use client"` 必須 | `"use client"` + `useGSAP` | `"use client"` + root provider | そのまま |
| 2026 推奨度 | 入退場・gesture | スクロール演出の主砲 | 慣性スクロールの主砲 | 軽量案件・未来向け |

**忠実性のガイドライン**:

- 参考サイトが GSAP を使っていて ScrollTrigger で pin + scrub している → **絶対に GSAP を使う**。Motion の `useScroll` だけでは scrub 遅延特性が合わない
- 参考サイトが Lenis を使っている → **Lenis を入れる**。CSS の `scroll-behavior: smooth` で代用不可 (慣性カーブが違う)
- 参考サイトが素の CSS アニメーション (GSAP 等なし) → CSS Scroll-Driven Animations で最短再現
- 参考サイトが Three.js/Canvas → React Three Fiber。CSS で頑張らない

## RSRC-WEBANIM-REPLAY.適用 — プロジェクトへの適用

本元 (エル子) の `core/clone.py` build / assemble サブステップと `.nxt-core/specs/coding/l3-nextjs.md` への反映方針:

1. **本棚ページのセクションに `# 採用ライブラリ` を必須化** — CAPTURE の `detectLibs()` 結果を書く。`/layo` apply で編集可能、`/codi` build がここを読んで実装方針を分岐。
2. **`build` サブステップでライブラリ別の実装雛形を出し分け** — `clone.py` の `_build_*_section()` を拡張し、「GSAP / Motion / Lenis / R3F / pure-CSS」5 パターンの雛形を用意。本棚ページの `採用ライブラリ` に従って選択。
3. **`useGSAP` / ReactLenis / Motion の provider テンプレを starter に追加** — プル子側で `app/providers.tsx` に GSAP plugin 登録と `<ReactLenis root>` が最初から入っている状態にする (不要なら消す方針で書く)。
4. **scroll サンプリング LUT の `useTransform` への自動変換** — CAPTURE で取った `scroll-samples.json` を `[[progress, value]]` の配列に変換し、build 雛形の `useTransform(progress, input, output)` に埋め込むヘルパを `clone.py` に追加。
5. **CSS Scroll-Driven Animations を積極採用する判断ルール** — 本棚ページで `{ hasCustomEasing: false, hasPinOrScrub: false }` のとき CSS 側で書く。`@supports not` フォールバックは自動で添える。
6. **View Transitions のゲート** — `next.config.ts` `experimental.viewTransition: true` はプル子 bootstrap 時にデフォルト有効化。使わないプロジェクトは unset すれば無害。
7. **VRT baseline との整合** — 本再現でアニメ中のフレームが VRT に乗ると毎回 diff が出る。既存 `baseline.mjs` の `reducedMotion: 'reduce'` と CSS の `@media (prefers-reduced-motion)` で止める想定を維持。CAPTURE 側と違って REPLAY の VRT は reduce のままで OK。

実装は別タスクとして TP で扱う。このページは「どの道具で / どう書くか」の根拠を固定する。

## RSRC-WEBANIM-REPLAY.出典 — 出典

- Motion — [React scroll animations — scroll-linked & parallax](https://motion.dev/docs/react-scroll-animations) (参照: 2026-04-13)
- Motion — [useScroll](https://motion.dev/docs/react-use-scroll) (参照: 2026-04-13)
- GSAP — [React & GSAP (useGSAP)](https://gsap.com/resources/React/) (参照: 2026-04-13)
- `@gsap/react` — [npm](https://www.npmjs.com/package/@gsap/react) (参照: 2026-04-13)
- Lenis — [GitHub darkroomengineering/lenis](https://github.com/darkroomengineering/lenis) (参照: 2026-04-13)
- Lenis — [Official docs](https://www.lenis.dev/) (参照: 2026-04-13)
- MDN — [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations) (参照: 2026-04-13)
- MDN — [View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) (参照: 2026-04-13)
- Next.js — [Guides: View transitions](https://nextjs.org/docs/app/guides/view-transitions) (参照: 2026-04-13)
- Next.js — [Next.js 15.2 Release Notes](https://nextjs.org/blog/next-15-2) (参照: 2026-04-13)
- React Three Fiber — [公式ドキュメント](https://r3f.docs.pmnd.rs/) (参照: 2026-04-13)
- GSAP Forums — [Patterns for synchronizing ScrollTrigger and Lenis in React/Next](https://gsap.com/community/forums/topic/40426-patterns-for-synchronizing-scrolltrigger-and-lenis-in-reactnext/) (参照: 2026-04-13)
