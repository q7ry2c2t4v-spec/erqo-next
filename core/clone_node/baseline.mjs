#!/usr/bin/env node
// baseline.mjs — Storybook ストーリーの VRT 基準スクショを自動取得する。
//
// Python 側 (core/clone.py cmd_baseline) から subprocess で呼ばれる。
// Storybook が未起動なら自動起動 → ストーリー iframe でスクショ → 停止。
//
// 使い方:
//   node core/clone_node/baseline.mjs <story-id> <output-dir> \
//     [--viewport name:WxH] [--port PORT]
//
// 出力:
//   <output-dir>/baseline-<viewport-name>.png
//
// 依存: プロジェクトルートの node_modules/playwright + @storybook/react
// プロジェクトルートで実行する想定 (cwd をそこに設定して呼ぶ)。

import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';
import { resolve, join } from 'node:path';
import { spawn } from 'node:child_process';

// --- 引数パース ---

function parseArgs(argv) {
  const args = argv.slice(2);
  if (args.length < 2) {
    throw new Error(
      'usage: node baseline.mjs <story-id> <output-dir> ' +
        '[--viewport name:WxH ...] [--port PORT]'
    );
  }

  const storyId = args[0];
  const outputDir = resolve(args[1]);
  const viewports = [];
  let port = 6099;

  for (let i = 2; i < args.length; i++) {
    if (args[i] === '--viewport' && i + 1 < args.length) {
      const spec = args[++i];
      const match = spec.match(/^([\w-]+):(\d+)x(\d+)$/);
      if (!match) throw new Error(`invalid --viewport spec: ${spec}`);
      viewports.push({
        name: match[1],
        width: parseInt(match[2], 10),
        height: parseInt(match[3], 10),
      });
    } else if (args[i] === '--port' && i + 1 < args.length) {
      port = parseInt(args[++i], 10);
    }
  }

  if (viewports.length === 0) {
    viewports.push({ name: 'desktop', width: 1440, height: 900 });
  }

  return { storyId, outputDir, viewports, port };
}

// --- Storybook サーバー管理 ---

async function isServerReady(url) {
  try {
    const res = await fetch(url, { signal: AbortSignal.timeout(3000) });
    return res.ok;
  } catch {
    return false;
  }
}

async function waitForServer(url, timeoutMs = 90000) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    if (await isServerReady(url)) return true;
    await new Promise((r) => setTimeout(r, 1500));
  }
  return false;
}

function startStorybook(port) {
  const isWindows = process.platform === 'win32';

  const child = spawn(
    'npx',
    ['storybook', 'dev', '--port', String(port), '--ci', '--no-open'],
    {
      stdio: ['ignore', 'pipe', 'pipe'],
      shell: isWindows,
      env: { ...process.env, CI: 'true', STORYBOOK_DISABLE_TELEMETRY: '1' },
      ...(isWindows ? {} : { detached: true }),
    }
  );

  // Storybook の stderr/stdout はログに流さない (ノイズが多い)
  child.stdout.resume();
  child.stderr.resume();

  return child;
}

function stopStorybook(child) {
  if (!child || child.exitCode !== null) return;
  if (process.platform === 'win32') {
    spawn('taskkill', ['/pid', String(child.pid), '/T', '/F'], {
      stdio: 'ignore',
    });
  } else {
    try {
      process.kill(-child.pid, 'SIGTERM');
    } catch {
      /* already exited */
    }
  }
}

// --- メイン ---

async function main() {
  const { storyId, outputDir, viewports, port } = parseArgs(process.argv);
  await mkdir(outputDir, { recursive: true });

  const baseUrl = `http://localhost:${port}`;
  let storybookChild = null;
  let weStarted = false;

  // Storybook 起動チェック
  if (await isServerReady(baseUrl)) {
    console.log(`baseline: Storybook already running at ${baseUrl}`);
  } else {
    console.log(`baseline: Starting Storybook on port ${port}...`);
    storybookChild = startStorybook(port);
    weStarted = true;

    const ready = await waitForServer(baseUrl);
    if (!ready) {
      stopStorybook(storybookChild);
      throw new Error(
        `Storybook did not start within 90 seconds at ${baseUrl}`
      );
    }
    console.log('baseline: Storybook is ready');
  }

  const iframeUrl = `${baseUrl}/iframe.html?id=${storyId}&viewMode=story`;

  const browser = await chromium.launch({ headless: true });
  try {
    for (const vp of viewports) {
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        reducedMotion: 'reduce',
      });
      const page = await context.newPage();

      try {
        await page.goto(iframeUrl, {
          waitUntil: 'networkidle',
          timeout: 30000,
        });
      } catch {
        // networkidle に行かない場合は load で妥協
        await page.goto(iframeUrl, { waitUntil: 'load', timeout: 30000 });
      }

      // レンダリング安定を待つ
      await page.waitForTimeout(1500);

      const screenshotPath = join(outputDir, `baseline-${vp.name}.png`);
      await page.screenshot({ path: screenshotPath, fullPage: true });

      console.log(
        `baseline-ok viewport=${vp.name} width=${vp.width} height=${vp.height} ` +
          `screenshot=${screenshotPath}`
      );

      await context.close();
    }
  } finally {
    await browser.close();

    if (weStarted && storybookChild) {
      console.log('baseline: Stopping Storybook...');
      stopStorybook(storybookChild);
    }
  }
}

main().catch((err) => {
  console.error(`baseline-error ${err.message}`);
  if (err.stack) console.error(err.stack);
  process.exit(1);
});
