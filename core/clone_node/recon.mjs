#!/usr/bin/env node
// recon.mjs — 参考サイトから 6 項目取材 + スクショを 1 回のブラウザ起動で取得する。
//
// Python 側 (core/clone.py cmd_recon) から subprocess で呼ばれる。
// 参考 URL を chromium で開き、ビューポートごとにスクショとメタ情報を保存する。
//
// 使い方:
//   node core/clone_node/recon.mjs <url> <output-dir> \
//     [--viewport name:WxH] [--viewport name:WxH] ... \
//     [--scroll-steps N] [--scroll-selectors sel1,sel2,...] \
//     [--assets-dir PATH] \
//     [--deterministic] [--deterministic-step MS] [--deterministic-warmup FRAMES] \
//     [--no-rrweb]
//
// 出力:
//   <output-dir>/screenshot-<name>.png
//   <output-dir>/recon-<name>.json
//   <output-dir>/scroll-samples.json                (desktop viewport のみ)
//   <output-dir>/rrweb.json                         (desktop viewport のみ、段階 4)
//   <assets-dir>/lottie-*.json / rive-*.riv         (Lottie/Rive 検出時)
//   <assets-dir>/video-*.mp4 / .webm / .ogg         (背景動画 検出時、段階 3)
//
// 取材項目 (page.evaluate 内で収集):
//   1. DOM  — セマンティックツリーの概要 (tagName / role / id / class / テキスト)
//   2. CSS  — 計算済みスタイルのサマリ (フォント / 色 / 寸法 / 表示プロパティ)
//   3. 色   — 出現色の重複排除リスト
//   4. フォント — font-family ごとの出現数 + weight / size サマリ
//   5. アセット — 画像 / 背景画像 / アイコン / 動画
//   6. アニメ  — element.getAnimations() からの keyframes / timing
//   7. ライブラリ — anim_lib_patterns.json の script/global 照合 (RSRC-WEBANIM-CAPTURE)
//   8. スクロール連動 — ページ高さを N 分割して transform/opacity/filter を実測
// (補助: インタラクション — focusable 要素 / リンク / ボタン / フォーム)
// (補助: Lottie/Rive は Node 側の response 監視で自動 DL)
//
// 依存: プロジェクトルートの node_modules/playwright
// プロジェクトルートで実行する想定 (cwd をそこに設定して呼ぶ)。

import { chromium } from 'playwright';
import { mkdir, writeFile, readFile } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { captureWebGLShaders, installWebGLProgramTracking } from './spector.mjs';
import { installTimeVirtualization, warmupVirtualTime } from './time-virtualize.mjs';
import { installRrwebRecording, startRrwebRecording, collectRrwebEvents } from './rrweb-record.mjs';

// 段階 3 の時間偽装デフォルト値。core/constants.py の DETERMINISTIC_STEP_MS /
// DETERMINISTIC_WARMUP_FRAMES と同期させること (SSOT は constants.py)。
// 現時点は recon.mjs 単独起動時のフォールバック用。将来 clone.py から CLI 引数で
// 上書きする仕様を足したら削除する。
const DETERMINISTIC_STEP_MS_DEFAULT = 16;
const DETERMINISTIC_WARMUP_FRAMES_DEFAULT = 60;

// --- 引数パース ---

function parseArgs(argv) {
  const args = argv.slice(2);
  if (args.length < 2) {
    throw new Error(
      'usage: node core/clone_node/recon.mjs <url> <output-dir> ' +
        '[--viewport name:WxH ...] [--scroll-steps N] ' +
        '[--scroll-selectors sel1,sel2,...] [--assets-dir PATH]'
    );
  }

  const url = args[0];
  const outputDir = resolve(args[1]);
  const viewports = [];
  let scrollSteps = 0;
  let scrollSelectors = [];
  let assetsDir = null;
  let deterministic = false;
  let deterministicStepMs = DETERMINISTIC_STEP_MS_DEFAULT;
  let deterministicWarmupFrames = DETERMINISTIC_WARMUP_FRAMES_DEFAULT;
  let rrwebEnabled = true;  // 段階 4: デフォルト ON、--no-rrweb でオフ

  for (let i = 2; i < args.length; i++) {
    if (args[i] === '--viewport' && i + 1 < args.length) {
      const spec = args[++i];
      const match = spec.match(/^([\w-]+):(\d+)x(\d+)$/);
      if (!match) {
        throw new Error(`invalid --viewport spec: ${spec}`);
      }
      viewports.push({
        name: match[1],
        width: parseInt(match[2], 10),
        height: parseInt(match[3], 10),
      });
    } else if (args[i] === '--scroll-steps' && i + 1 < args.length) {
      scrollSteps = parseInt(args[++i], 10);
      if (Number.isNaN(scrollSteps) || scrollSteps < 0) scrollSteps = 0;
    } else if (args[i] === '--scroll-selectors' && i + 1 < args.length) {
      scrollSelectors = args[++i].split(',').map(s => s.trim()).filter(Boolean);
    } else if (args[i] === '--assets-dir' && i + 1 < args.length) {
      assetsDir = resolve(args[++i]);
    } else if (args[i] === '--deterministic') {
      deterministic = true;
    } else if (args[i] === '--deterministic-step' && i + 1 < args.length) {
      const v = parseInt(args[++i], 10);
      if (!Number.isNaN(v) && v > 0) deterministicStepMs = v;
    } else if (args[i] === '--deterministic-warmup' && i + 1 < args.length) {
      const v = parseInt(args[++i], 10);
      if (!Number.isNaN(v) && v >= 0) deterministicWarmupFrames = v;
    } else if (args[i] === '--no-rrweb') {
      rrwebEnabled = false;
    } else if (args[i] === '--rrweb') {
      rrwebEnabled = true;
    }
  }

  if (viewports.length === 0) {
    // デフォルト: desktop のみ
    viewports.push({ name: 'desktop', width: 1440, height: 900 });
  }

  return {
    url, outputDir, viewports, scrollSteps, scrollSelectors, assetsDir,
    deterministic, deterministicStepMs, deterministicWarmupFrames,
    rrwebEnabled,
  };
}

// --- 取材本体 (page.evaluate の中で走る) ---
//
// evaluate に関数を渡すと page 側で実行される (Node スコープは使えない)。
// 結果を JSON シリアライズ可能な形で返す。

function collectReport(patterns) {
  /* eslint-env browser */

  const MAX_DOM_NODES = 400;
  const MAX_COLOR_ENTRIES = 80;

  // --- 7. ライブラリ検出 (RSRC-WEBANIM-CAPTURE §技術詳細 1) ---
  // patterns は anim_lib_patterns.json を JSON でそのまま受け取る
  const scriptSrcs = [...document.scripts]
    .map(s => s.src || '')
    .filter(Boolean);
  const detected = {};
  const globalsHit = {};
  const scriptsHit = {};
  if (patterns && Array.isArray(patterns.patterns)) {
    for (const p of patterns.patterns) {
      const re = new RegExp(p.scriptSrcRegex);
      const matchedScripts = scriptSrcs.filter(u => re.test(u));
      const matchedGlobals = (p.globals || []).filter(
        g => typeof window[g] !== 'undefined'
      );
      if (matchedScripts.length > 0 || matchedGlobals.length > 0) {
        detected[p.name] = true;
        scriptsHit[p.name] = matchedScripts.slice(0, 5);
        globalsHit[p.name] = matchedGlobals;
      }
    }
  }
  const libraries = {
    scripts: scriptSrcs.slice(0, 80),
    detected,
    scriptsHit,
    globalsHit,
  };

  // --- 1. DOM セマンティックツリー ---
  const domNodes = [];
  const walker = document.createTreeWalker(
    document.body || document.documentElement,
    NodeFilter.SHOW_ELEMENT
  );
  while (walker.nextNode() && domNodes.length < MAX_DOM_NODES) {
    const el = walker.currentNode;
    const rect = el.getBoundingClientRect();
    // 見えない要素はスキップ (サイズ 0 x 0)
    if (rect.width === 0 && rect.height === 0) continue;
    domNodes.push({
      tag: el.tagName.toLowerCase(),
      id: el.id || null,
      class: el.className && typeof el.className === 'string'
        ? el.className.slice(0, 200)
        : null,
      role: el.getAttribute('role') || null,
      text: (el.textContent || '').trim().slice(0, 80) || null,
      rect: {
        x: Math.round(rect.x),
        y: Math.round(rect.y),
        w: Math.round(rect.width),
        h: Math.round(rect.height),
      },
    });
  }

  // --- 2. CSS / 色 / フォントの集計 ---
  const colorCounts = new Map();
  const fontCounts = new Map();
  const fontSizes = new Set();
  const fontWeights = new Set();
  const allElements = document.querySelectorAll('*');

  function bumpMap(map, key) {
    if (!key) return;
    map.set(key, (map.get(key) || 0) + 1);
  }

  allElements.forEach((el) => {
    const cs = window.getComputedStyle(el);
    bumpMap(colorCounts, cs.color);
    bumpMap(colorCounts, cs.backgroundColor);
    bumpMap(colorCounts, cs.borderTopColor);
    bumpMap(fontCounts, cs.fontFamily);
    if (cs.fontSize) fontSizes.add(cs.fontSize);
    if (cs.fontWeight) fontWeights.add(cs.fontWeight);
  });

  const sortedColors = [...colorCounts.entries()]
    .filter(([c]) => c && c !== 'rgba(0, 0, 0, 0)' && c !== 'transparent')
    .sort((a, b) => b[1] - a[1])
    .slice(0, MAX_COLOR_ENTRIES)
    .map(([value, count]) => ({ value, count }));

  const sortedFonts = [...fontCounts.entries()]
    .sort((a, b) => b[1] - a[1])
    .slice(0, 20)
    .map(([value, count]) => ({ value, count }));

  // --- 5. アセット ---
  const imgs = [...document.images].slice(0, 80).map((img) => ({
    src: img.currentSrc || img.src || null,
    alt: img.alt || null,
    w: img.naturalWidth || img.width || null,
    h: img.naturalHeight || img.height || null,
  }));

  const bgImages = [];
  allElements.forEach((el) => {
    if (bgImages.length >= 40) return;
    const bg = window.getComputedStyle(el).backgroundImage;
    if (bg && bg !== 'none') {
      bgImages.push({
        tag: el.tagName.toLowerCase(),
        id: el.id || null,
        image: bg.slice(0, 200),
      });
    }
  });

  const videos = [...document.querySelectorAll('video')].map((v) => ({
    src: v.currentSrc || v.src || null,
    poster: v.poster || null,
  }));

  // --- 6. アニメーション ---
  const animations = [];
  try {
    const docAnims = document.getAnimations ? document.getAnimations() : [];
    docAnims.slice(0, 50).forEach((anim) => {
      const effect = anim.effect;
      if (!effect) return;
      const timing = effect.getTiming ? effect.getTiming() : {};
      let keyframes = [];
      try {
        keyframes = effect.getKeyframes ? effect.getKeyframes() : [];
      } catch {
        keyframes = [];
      }
      const target = effect.target;
      animations.push({
        target: target
          ? {
              tag: target.tagName ? target.tagName.toLowerCase() : null,
              id: target.id || null,
              class: (target.className && typeof target.className === 'string')
                ? target.className.slice(0, 100)
                : null,
            }
          : null,
        playState: anim.playState,
        duration: timing.duration || null,
        iterations: timing.iterations || null,
        easing: timing.easing || null,
        keyframes: keyframes.slice(0, 20),
      });
    });
  } catch (e) {
    /* no-op: getAnimations 未対応ブラウザ */
  }

  // --- 補助: インタラクション ---
  const interactions = {
    links: document.querySelectorAll('a[href]').length,
    buttons: document.querySelectorAll('button, [role="button"]').length,
    inputs: document.querySelectorAll('input, select, textarea').length,
    focusables: document.querySelectorAll(
      'a[href], button, input, select, textarea, [tabindex]:not([tabindex="-1"])'
    ).length,
  };

  // --- トポロジー ---
  const topology = {
    header: !!document.querySelector('header'),
    nav: !!document.querySelector('nav'),
    main: !!document.querySelector('main'),
    aside: !!document.querySelector('aside'),
    footer: !!document.querySelector('footer'),
    sectionCount: document.querySelectorAll('section').length,
    articleCount: document.querySelectorAll('article').length,
  };

  // --- WebGL 検出 (段階 2: RSRC-WEBANIM-HARDCASE §1) ---
  // canvas が WebGL/WebGL2 コンテキストを保有しているかを確認する。
  // getContext は同一種別なら既存コンテキストを返すだけで副作用なし。
  const canvasElements = [...document.querySelectorAll('canvas')];
  let hasWebGL = false;
  for (const c of canvasElements) {
    try {
      if (c.getContext('webgl2') || c.getContext('webgl')) {
        hasWebGL = true;
        break;
      }
    } catch {
      /* 取得失敗は無視 */
    }
  }
  const webgl = { hasWebGL, canvasCount: canvasElements.length };

  return {
    url: window.location.href,
    title: document.title || null,
    viewport: { w: window.innerWidth, h: window.innerHeight },
    dom: domNodes,
    css: {
      colors: sortedColors,
      fonts: sortedFonts,
      fontSizes: [...fontSizes].slice(0, 40),
      fontWeights: [...fontWeights].slice(0, 10),
      totalElements: allElements.length,
    },
    assets: {
      images: imgs,
      backgroundImages: bgImages,
      videos,
    },
    animations,
    libraries,
    interactions,
    topology,
    webgl,
  };
}

// --- スクロール連動サンプリング (ページ側で実行) ---
// RSRC-WEBANIM-CAPTURE §技術詳細 6 "スクロール連動マッピングの抽出"。
// ページ高さを steps 分割し、各段階で観察対象の transform/opacity/filter を記録する。
// target の最大個数は 12 に制限 (1 サンプルあたりの上限)。ログ全体サイズを抑える。

async function collectScrollSamples({ steps, selectors }) {
  /* eslint-env browser */
  const MAX_TARGETS_PER_FRAME = 12;
  const uniqueSel = selectors.join(', ');
  const targets = [...document.querySelectorAll(uniqueSel)]
    .slice(0, MAX_TARGETS_PER_FRAME);

  const describe = el => {
    const cls = typeof el.className === 'string'
      ? el.className.slice(0, 80)
      : '';
    return `${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}${cls ? '.' + cls.split(/\s+/).filter(Boolean).slice(0, 2).join('.') : ''}`;
  };

  const docHeight = Math.max(
    document.documentElement.scrollHeight,
    document.body ? document.body.scrollHeight : 0
  );
  const stepHeight = steps > 0 ? docHeight / steps : docHeight;
  const samples = [];
  const rafTwice = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));

  for (let i = 0; i <= steps; i++) {
    const y = Math.round(stepHeight * i);
    window.scrollTo(0, y);
    await rafTwice();
    const frame = targets.map(el => {
      const cs = window.getComputedStyle(el);
      return {
        sel: describe(el),
        transform: cs.transform,
        opacity: cs.opacity,
        filter: cs.filter,
      };
    });
    samples.push({ y, frame });
  }

  window.scrollTo(0, 0);
  return {
    steps,
    docHeight,
    selectors,
    targetCount: targets.length,
    samples,
  };
}

// --- Lottie / Rive 検出 (Node 側で response 監視) ---
// RSRC-WEBANIM-CAPTURE §技術詳細 1 の補助 + §RSRC-WEBANIM-HARDCASE §5 "Lottie/Rive 検出"。

// 段階 1: json / lottie / riv  ← Lottie/Rive DL
// 段階 3: mp4 / webm / ogg      ← 背景動画 DL (core/constants.py VIDEO_EXTENSIONS と同期)
const RECON_ASSET_URL_REGEX = /\.(json|lottie|riv|mp4|webm|ogg)(\?|$)/i;
const VIDEO_EXT_REGEX = /\.(mp4|webm|ogg)(\?|$)/i;
const LOTTIE_JSON_MARKER_RE = /"v"\s*:\s*"[\d.]+"[\s\S]*?"layers"\s*:/;
const RIVE_MAGIC = Buffer.from('RIVE');

function classifyAsset(url, buf) {
  if (VIDEO_EXT_REGEX.test(url)) return 'video';
  if (/\.riv(\?|$)/i.test(url)) return 'rive';
  if (buf.length >= 4 && buf.slice(0, 4).equals(RIVE_MAGIC)) return 'rive';
  if (/\.lottie(\?|$)/i.test(url)) return 'lottie';
  if (/\.json(\?|$)/i.test(url)) {
    const head = buf.slice(0, 1024).toString('utf-8');
    if (LOTTIE_JSON_MARKER_RE.test(head)) return 'lottie';
  }
  return null;
}

// --- メイン ---

async function main() {
  const {
    url, outputDir, viewports,
    scrollSteps, scrollSelectors, assetsDir,
    deterministic, deterministicStepMs, deterministicWarmupFrames,
    rrwebEnabled,
  } = parseArgs(process.argv);

  await mkdir(outputDir, { recursive: true });
  if (assetsDir) await mkdir(assetsDir, { recursive: true });

  // --- anim_lib_patterns.json を SSOT から読み込む ---
  const thisDir = dirname(fileURLToPath(import.meta.url));
  const patternsPath = join(thisDir, 'anim_lib_patterns.json');
  let patterns = { patterns: [], selectPriority: [] };
  try {
    patterns = JSON.parse(await readFile(patternsPath, 'utf-8'));
  } catch (e) {
    console.error(`recon-warn anim_lib_patterns.json の読み込み失敗: ${e.message}`);
  }

  const browser = await chromium.launch({ headless: true });
  try {
    const savedAssets = [];
    for (let vpIdx = 0; vpIdx < viewports.length; vpIdx++) {
      const vp = viewports[vpIdx];
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
      });
      const page = await context.newPage();

      // --- WebGL program 履歴追跡 (段階 4: RSRC-WEBANIM-HARDCASE §1 拡張) ---
      // WebGLRenderingContext / WebGL2RenderingContext の useProgram を addInitScript で
      // hook し、サイトが bind した全 program への参照を追跡する。
      // capture 時 (screenshot 後) に getAttachedShaders + getShaderSource で GLSL を抽出。
      // 失敗しても recon 全体は止めない (HARDCASE §1「9 割再現」方針)。
      if (vpIdx === 0) {
        try {
          await installWebGLProgramTracking(page);
          console.log('recon-webgl tracking installed (useProgram hook)');
        } catch (e) {
          console.error(`recon-warn WebGL hook install 失敗: ${e.message}`);
        }
      }

      // --- 仮想時計注入 (段階 3: RSRC-WEBANIM-HARDCASE §2) ---
      // deterministic=true なら page.addInitScript で仮想時計を入れる。
      // Web Worker / OffscreenCanvas の時計は patch 外 (time-virtualize.mjs の制約参照)。
      if (deterministic) {
        try {
          await installTimeVirtualization(page);
          console.log(
            `recon-deterministic install step=${deterministicStepMs}ms ` +
              `warmup=${deterministicWarmupFrames}frames`
          );
        } catch (e) {
          console.error(`recon-warn 仮想時計注入失敗: ${e.message}`);
        }
      }

      // --- rrweb 録画開始 (段階 4: RSRC-WEBANIM-HARDCASE §3) ---
      // desktop viewport のみ。UMD を addInitScript で注入し record を起動。
      // rrweb パッケージが node_modules に無ければスキップする (警告のみ、取材は止めない)。
      let rrwebInstalled = false;
      if (rrwebEnabled && vpIdx === 0) {
        try {
          const bundlePath = await installRrwebRecording(page);
          rrwebInstalled = true;
          console.log(`recon-rrweb install bundle=${bundlePath}`);
        } catch (e) {
          console.error(`recon-warn rrweb install スキップ: ${e.message}`);
        }
      }

      // --- Lottie / Rive / 背景動画 の response 監視 (最初の viewport だけで十分) ---
      const seenAssetUrls = new Set();
      if (assetsDir && vpIdx === 0) {
        page.on('response', async (res) => {
          const resUrl = res.url();
          if (!RECON_ASSET_URL_REGEX.test(resUrl)) return;
          if (seenAssetUrls.has(resUrl)) return;
          seenAssetUrls.add(resUrl);
          try {
            const buf = await res.body();
            const kind = classifyAsset(resUrl, buf);
            if (!kind) return;
            const extMatch = resUrl.match(RECON_ASSET_URL_REGEX);
            const ext = extMatch ? extMatch[1].toLowerCase() : 'bin';
            const hash = Math.abs([...resUrl].reduce((a, c) => (a * 31 + c.charCodeAt(0)) | 0, 0))
              .toString(36).slice(0, 8);
            const fileName = `${kind}-${hash}.${ext}`;
            const filePath = join(assetsDir, fileName);
            await writeFile(filePath, buf);
            savedAssets.push({
              url: resUrl, kind, fileName, size: buf.length,
            });
            console.log(`recon-asset kind=${kind} file=${filePath} size=${buf.length}`);
          } catch {
            /* 取得失敗は無視 (ストリーミング等で body が取れないケース) */
          }
        });
      }

      // deterministic モードは全ての setTimeout を仮想時計に差し替えるため、
      // 'networkidle' を待つと遅延ロードが発火せずタイムアウトする。
      // DOM 構築完了 (domcontentloaded) → warmupVirtualTime で初期化を進める、の 2 段構え。
      const gotoWaitUntil = deterministic ? 'domcontentloaded' : 'networkidle';
      try {
        await page.goto(url, { waitUntil: gotoWaitUntil, timeout: 45000 });
      } catch (e) {
        // networkidle に行かないサイトもあるので load で妥協リトライ
        await page.goto(url, { waitUntil: 'load', timeout: 45000 });
      }

      // 仮想時計ウォームアップ (段階 3): 初期 setTimeout / rAF チェーンを進めて
      // 「60 フレーム経過相当」の DOM 状態にしてから取材する。
      if (deterministic && vpIdx === 0) {
        try {
          await warmupVirtualTime(page, deterministicWarmupFrames, deterministicStepMs);
          console.log(
            `recon-deterministic warmup-done ` +
              `frames=${deterministicWarmupFrames} stepMs=${deterministicStepMs}`
          );
        } catch (e) {
          console.error(`recon-warn 仮想時計 warmup 失敗: ${e.message}`);
        }
      }

      // アニメ開始直後も取れるよう少し待つ。
      // 通常モードは 1 秒 / deterministic モードは warmup 済みなので 200ms に短縮。
      await page.waitForTimeout(deterministic ? 200 : 1000);

      const screenshotPath = join(outputDir, `screenshot-${vp.name}.png`);
      await page.screenshot({ path: screenshotPath, fullPage: true });

      const report = await page.evaluate(collectReport, patterns);
      report._meta = {
        reconViewport: vp,
        capturedAt: new Date().toISOString(),
        screenshotFile: `screenshot-${vp.name}.png`,
      };

      // --- スクロール連動サンプリング (desktop viewport のみ実行してコスト抑制) ---
      if (scrollSteps > 0 && scrollSelectors.length > 0 && vpIdx === 0) {
        // 段階 4: deterministic モードだと collectScrollSamples 内の rafTwice() が
        // 仮想 rAF キューに積まれて外部 __step__ を待つため resolve しない。
        // scroll-samples は実時計での scrollTo + rAF 待ちを前提としているので、
        // 実行中だけ仮想時計を一時停止する。
        if (deterministic) {
          try {
            const paused = await page.evaluate(() =>
              typeof window.__pause__ === 'function' ? window.__pause__() : false
            );
            if (paused) {
              console.log('recon-deterministic scroll-samples paused virtual clock');
            }
          } catch (e) {
            console.error(`recon-warn 仮想時計 pause 失敗: ${e.message}`);
          }
        }
        // 段階 4: rrweb 録画は scroll-samples 区間だけ起動する (goto 直後に起動すると
        // MutationObserver 発火で fullPage screenshot が timeout するため)。
        if (rrwebInstalled) {
          try {
            const r = await startRrwebRecording(page);
            if (r.started) {
              console.log('recon-rrweb record started (scroll-samples window)');
            } else {
              console.error(`recon-warn rrweb 起動スキップ: ${r.reason}`);
            }
          } catch (e) {
            console.error(`recon-warn rrweb 起動失敗: ${e.message}`);
          }
        }
        try {
          const scrollData = await page.evaluate(
            collectScrollSamples,
            { steps: scrollSteps, selectors: scrollSelectors },
          );
          report.scrollSamples = scrollData;
          // scroll-samples.json を別ファイルでも出す (全量参照用)
          const scrollPath = join(outputDir, 'scroll-samples.json');
          await writeFile(
            scrollPath,
            JSON.stringify(scrollData, null, 2),
            'utf-8',
          );
          console.log(
            `recon-scroll steps=${scrollSteps} targets=${scrollData.targetCount} ` +
              `file=${scrollPath}`
          );
        } catch (e) {
          console.error(`recon-warn スクロールサンプリング失敗: ${e.message}`);
        }
        if (deterministic) {
          try {
            await page.evaluate(() => {
              if (typeof window.__resume__ === 'function') window.__resume__();
            });
            console.log('recon-deterministic scroll-samples resumed virtual clock');
          } catch (e) {
            console.error(`recon-warn 仮想時計 resume 失敗: ${e.message}`);
          }
        }
      }

      // --- WebGL シェーダ取材 (段階 2: RSRC-WEBANIM-HARDCASE §1) ---
      // hasWebGL=true のときだけ Spector.js を注入してシェーダを取得。
      // 失敗しても recon 全体は止めない (HARDCASE §1「9 割再現」方針)。
      // capture が成功したら programs 0 件でも shaders.json に残す (デバッグ + 後段参照用)。
      if (vpIdx === 0 && report.webgl?.hasWebGL) {
        try {
          const shaders = await captureWebGLShaders(page);
          if (shaders) {
            const webglDir = join(outputDir, 'webgl');
            await mkdir(webglDir, { recursive: true });
            const shadersPath = join(webglDir, 'shaders.json');
            await writeFile(
              shadersPath,
              JSON.stringify(shaders, null, 2),
              'utf-8',
            );
            const programCount = Array.isArray(shaders.programs) ? shaders.programs.length : 0;
            console.log(
              `recon-webgl programs=${programCount} ` +
                `commands=${shaders.commandCount} file=${shadersPath}`
            );
          } else {
            console.log('recon-webgl capture null (タイムアウト or canvas 未検出)');
          }
        } catch (e) {
          console.error(`recon-warn WebGL capture 失敗: ${e.message}`);
        }
      }

      // --- rrweb 録画回収 (段階 4: RSRC-WEBANIM-HARDCASE §3) ---
      // record を停止して events を取り出し、rrweb.json に保存。
      // scroll-samples 区間で起動した record を回収する。events が 0 件なら
      // JSON は書かず report にも載せない (未起動 / scroll-samples 非実行時)。
      if (rrwebInstalled) {
        try {
          const result = await collectRrwebEvents(page);
          if (result.eventCount > 0) {
            const rrwebPath = join(outputDir, 'rrweb.json');
            await writeFile(
              rrwebPath,
              JSON.stringify({
                eventCount: result.eventCount,
                capturedAt: new Date().toISOString(),
                url: report.url,
                sampling: { mousemove: 20, scroll: 100, input: 'all' },
                events: result.events,
              }, null, 2),
              'utf-8',
            );
            report.rrweb = {
              eventCount: result.eventCount,
              file: 'rrweb.json',
            };
            console.log(`recon-rrweb events=${result.eventCount} file=${rrwebPath}`);
          } else {
            console.log('recon-rrweb events=0 (record 未起動 or scroll-samples 非実行)');
          }
        } catch (e) {
          console.error(`recon-warn rrweb 回収失敗: ${e.message}`);
        }
      }

      const jsonPath = join(outputDir, `recon-${vp.name}.json`);
      await writeFile(jsonPath, JSON.stringify(report, null, 2), 'utf-8');

      // Node 側 stdout は進捗行のみ。Python がパースしやすいよう key=value で出す。
      console.log(
        `recon-ok viewport=${vp.name} width=${vp.width} height=${vp.height} ` +
          `screenshot=${screenshotPath} json=${jsonPath}`
      );

      await context.close();
    }

    if (assetsDir && savedAssets.length > 0) {
      const manifestPath = join(assetsDir, 'manifest.json');
      await writeFile(
        manifestPath,
        JSON.stringify({ assets: savedAssets }, null, 2),
        'utf-8',
      );
      console.log(`recon-assets-manifest file=${manifestPath} count=${savedAssets.length}`);
    }
  } finally {
    await browser.close();
  }
}

// collectReport / collectScrollSamples は page.evaluate の第 1 引数 fn として渡されるため、
// Node 側から直接参照されるが、関数本体は page 側で実行される。
// page.evaluate はクロージャを追えないので、collectScrollSamples は collectReport とは別の
// evaluate で呼ぶ (上の main() が対応済み)。関数本体はシリアライズできるように
// モジュールスコープのトップレベル関数として宣言している。

main().catch((err) => {
  console.error(`recon-error ${err.message}`);
  if (err.stack) {
    console.error(err.stack);
  }
  process.exit(1);
});
