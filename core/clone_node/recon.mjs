#!/usr/bin/env node
// recon.mjs — 参考サイトから 6 項目取材 + スクショを 1 回のブラウザ起動で取得する。
//
// Python 側 (core/clone.py cmd_recon) から subprocess で呼ばれる。
// 参考 URL を chromium で開き、ビューポートごとにスクショとメタ情報を保存する。
//
// 使い方:
//   node core/clone_node/recon.mjs <url> <output-dir> \
//     [--viewport name:WxH] [--viewport name:WxH] ...
//
// 出力:
//   <output-dir>/screenshot-<name>.png
//   <output-dir>/recon-<name>.json
//
// 取材 6 項目 (page.evaluate 内で収集):
//   1. DOM  — セマンティックツリーの概要 (tagName / role / id / class / テキスト)
//   2. CSS  — 計算済みスタイルのサマリ (フォント / 色 / 寸法 / 表示プロパティ)
//   3. 色   — 出現色の重複排除リスト
//   4. フォント — font-family ごとの出現数 + weight / size サマリ
//   5. アセット — 画像 / 背景画像 / アイコン / 動画
//   6. アニメ  — element.getAnimations() からの keyframes / timing
// (補助: インタラクション — focusable 要素 / リンク / ボタン / フォーム)
//
// 依存: プロジェクトルートの node_modules/playwright
// プロジェクトルートで実行する想定 (cwd をそこに設定して呼ぶ)。

import { chromium } from 'playwright';
import { mkdir, writeFile } from 'node:fs/promises';
import { dirname, join, resolve } from 'node:path';

// --- 引数パース ---

function parseArgs(argv) {
  const args = argv.slice(2);
  if (args.length < 2) {
    throw new Error(
      'usage: node core/clone_node/recon.mjs <url> <output-dir> ' +
        '[--viewport name:WxH ...]'
    );
  }

  const url = args[0];
  const outputDir = resolve(args[1]);
  const viewports = [];

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
    }
  }

  if (viewports.length === 0) {
    // デフォルト: desktop のみ
    viewports.push({ name: 'desktop', width: 1440, height: 900 });
  }

  return { url, outputDir, viewports };
}

// --- 取材本体 (page.evaluate の中で走る) ---
//
// evaluate に関数を渡すと page 側で実行される (Node スコープは使えない)。
// 結果を JSON シリアライズ可能な形で返す。

function collectReport() {
  /* eslint-env browser */

  const MAX_DOM_NODES = 400;
  const MAX_COLOR_ENTRIES = 80;

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
    interactions,
    topology,
  };
}

// --- メイン ---

async function main() {
  const { url, outputDir, viewports } = parseArgs(process.argv);

  await mkdir(outputDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  try {
    for (const vp of viewports) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
      });
      const page = await context.newPage();

      try {
        await page.goto(url, { waitUntil: 'networkidle', timeout: 45000 });
      } catch (e) {
        // networkidle に行かないサイトもあるので load で妥協リトライ
        await page.goto(url, { waitUntil: 'load', timeout: 45000 });
      }

      // アニメ開始直後も取れるよう少し待つ (1 秒)
      await page.waitForTimeout(1000);

      const screenshotPath = join(outputDir, `screenshot-${vp.name}.png`);
      await page.screenshot({ path: screenshotPath, fullPage: true });

      const report = await page.evaluate(collectReport);
      report._meta = {
        reconViewport: vp,
        capturedAt: new Date().toISOString(),
        screenshotFile: `screenshot-${vp.name}.png`,
      };
      const jsonPath = join(outputDir, `recon-${vp.name}.json`);
      await writeFile(jsonPath, JSON.stringify(report, null, 2), 'utf-8');

      // Node 側 stdout は進捗行のみ。Python がパースしやすいよう key=value で出す。
      console.log(
        `recon-ok viewport=${vp.name} width=${vp.width} height=${vp.height} ` +
          `screenshot=${screenshotPath} json=${jsonPath}`
      );

      await context.close();
    }
  } finally {
    await browser.close();
  }
}

main().catch((err) => {
  console.error(`recon-error ${err.message}`);
  if (err.stack) {
    console.error(err.stack);
  }
  process.exit(1);
});
