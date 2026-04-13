#!/usr/bin/env node
// rrweb-record.mjs — rrweb で DOM 時系列を録画する (段階 4)
//
// RSRC-WEBANIM-HARDCASE §3 "rrweb 型 DOM 時系列記録" に準拠。
// 外部から呼ばれるのは 3 関数:
//   - installRrwebRecording(page)   goto 前に rrweb UMD を addInitScript で注入 (record は未起動)
//   - startRrwebRecording(page)     取材シナリオ直前に record を起動
//   - collectRrwebEvents(page)      record を停止し window.__rrwebEvents__ を回収
//
// 注入後、ページコンテキストには以下が定義される:
//   window.__rrwebEvents__    取材中に蓄積される rrweb イベント配列
//   window.__rrwebStop__()    record を止める (collect 時に自動で呼ぶ)
//   window.__rrwebStarted__   record が既に走っているか (二重起動防止)
//
// 仕組み:
//   1. node_modules/rrweb の UMD バンドルを Playwright の addInitScript({path}) で注入
//      → page の先頭で window.rrweb を定義する
//   2. startRrwebRecording で page.evaluate 経由で rrweb.record(...) を起動
//      (goto 直後に起動すると rrweb の MutationObserver 発火で page.screenshot が
//       timeout するため、scroll-samples 区間だけ録画する設計に分離した)
//   3. 取材終了後に collectRrwebEvents で stop + events を取り出して JSON 保存
//
// 備考:
//   - WebGL/canvas の内容は recordCanvas=true が必要だが、重いため off (段階 4 では非対応)
//     WebGL 取材は spector.mjs 側で別系統
//   - rrweb は MutationObserver で動くため、仮想時計下でも動作する
//     (timestamp は仮想時計の Date.now())
//   - rrweb パッケージが node_modules に無ければ呼び出し側で握りつぶす設計

import { createRequire } from 'node:module';
import { dirname, join } from 'node:path';
import { existsSync } from 'node:fs';

const require = createRequire(import.meta.url);

// 2.x の UMD ファイル名の変遷に備えて候補を複数試す。
// 見つかった最初のものを使う。
const RRWEB_UMD_CANDIDATES = [
  'rrweb.umd.cjs',
  'rrweb.min.js',
  'rrweb.js',
  'rrweb.umd.min.cjs',
];

function resolveRrwebUmd() {
  let entry;
  try {
    entry = require.resolve('rrweb');
  } catch {
    return null;
  }
  const distDir = dirname(entry);
  for (const candidate of RRWEB_UMD_CANDIDATES) {
    const p = join(distDir, candidate);
    if (existsSync(p)) return p;
  }
  // entry がパッケージルート直下の場合は dist/ を追加で探す
  for (const candidate of RRWEB_UMD_CANDIDATES) {
    const p = join(distDir, 'dist', candidate);
    if (existsSync(p)) return p;
  }
  return null;
}

export async function installRrwebRecording(page) {
  const bundlePath = resolveRrwebUmd();
  if (!bundlePath) {
    throw new Error(
      'rrweb の UMD バンドルが見つかりません。' +
      'starter/package.json の "rrweb" 依存を確認してください。'
    );
  }
  // UMD バンドルを page のプリロードに積むだけ (window.rrweb を定義する)。
  // record はここでは起動しない — goto 直後に起動すると rrweb の MutationObserver
  // が fullPage screenshot と干渉して page.screenshot が timeout する。
  // record の起動は startRrwebRecording 側で scroll-samples 直前に行う。
  await page.addInitScript({ path: bundlePath });
  // events バッファだけは先に初期化 (startRrwebRecording 前に collect されても空配列が返る)
  await page.addInitScript(() => {
    /* eslint-env browser */
    window.__rrwebEvents__ = [];
    window.__rrwebStarted__ = false;
  });
  return bundlePath;
}

export async function startRrwebRecording(page) {
  return await page.evaluate(() => {
    if (window.__rrwebStarted__) return { started: false, reason: 'already-started' };
    const api = window.rrweb;
    // rrweb 2.x は record を直接 export する場合と、rrweb.record として持つ場合がある
    const recordFn = (api && typeof api.record === 'function') ? api.record
      : (typeof api === 'function') ? api
      : null;
    if (!recordFn) return { started: false, reason: 'rrweb-not-loaded' };
    try {
      window.__rrwebStop__ = recordFn({
        emit: (ev) => { window.__rrwebEvents__.push(ev); },
        sampling: { mousemove: 20, scroll: 100, input: 'all' },
        slimDOMOptions: 'all',
      });
      window.__rrwebStarted__ = true;
      return { started: true };
    } catch (e) {
      return { started: false, reason: e && e.message ? e.message : 'record-threw' };
    }
  });
}

export async function collectRrwebEvents(page) {
  return await page.evaluate(() => {
    try {
      if (typeof window.__rrwebStop__ === 'function') {
        window.__rrwebStop__();
      }
    } catch {
      /* 停止失敗は無視 (既に停止 or 未開始) */
    }
    const events = Array.isArray(window.__rrwebEvents__) ? window.__rrwebEvents__ : [];
    return {
      eventCount: events.length,
      events,
    };
  });
}
