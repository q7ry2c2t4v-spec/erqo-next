#!/usr/bin/env node
// diff.mjs — 元サイトの recon スクショと再現 (Storybook baseline) スクショを
// pixelmatch で比較し、差分画像と差分率を出力する。
//
// Python 側 (core/clone.py _run_node_diff) から subprocess で呼ばれる。
//
// 使い方:
//   node core/clone_node/diff.mjs \
//     --baseline <path/to/baseline-desktop.png> \
//     --reference <path/to/screenshot-desktop.png> \
//     --output   <path/to/diff-desktop.png> \
//     [--threshold 0.1] [--alpha 0.5]
//
// 出力: diff 画像 (--output) + 最終行に 1 行 JSON で結果サマリ。
//   {"mismatchRatio": 0.0234, "diffPixels": 1234, "width": 1440, "height": 900}
//
// 依存: プロジェクトルートの node_modules/pixelmatch + pngjs
// RSRC-WEBANIM-HARDCASE §7 "VRT 差分自動修正ループ" のレポート部分。

import { readFile, writeFile } from 'node:fs/promises';
import { PNG } from 'pngjs';
import pixelmatch from 'pixelmatch';

function parseArgs(argv) {
  const args = argv.slice(2);
  const out = { threshold: 0.1, alpha: 0.5 };
  for (let i = 0; i < args.length; i++) {
    const key = args[i];
    const val = args[i + 1];
    if (key === '--baseline' && val) { out.baseline = val; i++; }
    else if (key === '--reference' && val) { out.reference = val; i++; }
    else if (key === '--output' && val) { out.output = val; i++; }
    else if (key === '--threshold' && val) { out.threshold = parseFloat(val); i++; }
    else if (key === '--alpha' && val) { out.alpha = parseFloat(val); i++; }
  }
  if (!out.baseline || !out.reference || !out.output) {
    throw new Error(
      'usage: node core/clone_node/diff.mjs --baseline <png> --reference <png> --output <png> [--threshold N] [--alpha N]'
    );
  }
  return out;
}

async function readPng(path) {
  const buf = await readFile(path);
  return PNG.sync.read(buf);
}

// --- サイズを小さい方に合わせてリサイズ (同一寸法化) ---
//
// pixelmatch は寸法一致が前提。参考サイトと再現が同サイズで撮られる保証はない
// (fullPage スクショでページ高さが違う等)。そこで、交差矩形 (min(w1,w2) × min(h1,h2))
// でトリミングしてから比較する。比較範囲を明示した上で、差分は「共通部分の中で」測る。

function cropToCommon(png, commonWidth, commonHeight) {
  if (png.width === commonWidth && png.height === commonHeight) return png;
  const cropped = new PNG({ width: commonWidth, height: commonHeight });
  PNG.bitblt(png, cropped, 0, 0, commonWidth, commonHeight, 0, 0);
  return cropped;
}

async function main() {
  const { baseline, reference, output, threshold, alpha } = parseArgs(process.argv);

  const a = await readPng(baseline);
  const b = await readPng(reference);

  const commonWidth = Math.min(a.width, b.width);
  const commonHeight = Math.min(a.height, b.height);
  if (commonWidth === 0 || commonHeight === 0) {
    throw new Error(
      `画像の共通寸法が 0: baseline=${a.width}x${a.height} reference=${b.width}x${b.height}`
    );
  }

  const aCropped = cropToCommon(a, commonWidth, commonHeight);
  const bCropped = cropToCommon(b, commonWidth, commonHeight);
  const diff = new PNG({ width: commonWidth, height: commonHeight });

  const diffPixels = pixelmatch(
    aCropped.data, bCropped.data, diff.data,
    commonWidth, commonHeight,
    { threshold, alpha, includeAA: false },
  );
  const total = commonWidth * commonHeight;
  const mismatchRatio = total > 0 ? diffPixels / total : 0;

  await writeFile(output, PNG.sync.write(diff));

  // Python 側が拾う最終行の JSON。diff.mjs の契約。
  console.log(JSON.stringify({
    mismatchRatio,
    diffPixels,
    width: commonWidth,
    height: commonHeight,
    baselineWidth: a.width,
    baselineHeight: a.height,
    referenceWidth: b.width,
    referenceHeight: b.height,
    output,
  }));
}

main().catch((err) => {
  console.error(`diff-error ${err.message}`);
  if (err.stack) console.error(err.stack);
  process.exit(1);
});
