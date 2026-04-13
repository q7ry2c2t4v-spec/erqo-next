#!/usr/bin/env node
// time-virtualize.mjs — Playwright ページに仮想時計を注入する (段階 3)
//
// RSRC-WEBANIM-HARDCASE §2 "rAF 時間偽装法 — 決定的フレーム取材" に準拠。
// 外部から呼ばれるのは 2 関数のみ:
//   - installTimeVirtualization(page)   ページ生成直後に呼んで addInitScript する
//   - warmupVirtualTime(page, steps, stepMs)   goto 後にフレームを進めてウォームアップ
//
// 注入後、ページコンテキストには以下が定義される:
//   window.__step__(dtMs)     仮想時計を dtMs 進め、発火可能な timeout / rAF / CSS アニメ /
//                              video.currentTime を全部同期して currentTime を返す
//   window.__virtualTime__()  現在の仮想時計 (ms)
//   window.__pause__()        仮想時計を一時停止し、Date/rAF/setTimeout 等を元の実装に戻す
//                              (段階 4: scroll-samples のような実時計前提の取材中だけ無効化)
//   window.__resume__()       仮想時計を再適用する (保留中の rAF/timeout は保持される)
//   window.__isPaused__()     現在一時停止中か (bool)
//
// 制約 (RSRC-WEBANIM-HARDCASE §2 の注意点):
//   - Web Worker / OffscreenCanvas の内部時計は patch できない
//   - requestIdleCallback は rAF で代替注入 (厳密な idle は模倣しない)
//   - Promise / queueMicrotask は触らない (イベントループ整合性が崩れる)
//   - 仮想時計を入れると setTimeout 依存の初期化が止まるため、
//     必ず goto 後に warmupVirtualTime でステップを進めること
//   - __pause__ 中は仮想時計は進まない。pause→resume 間に実時計で経過した時間は
//     仮想時計には加算されない (想定: scroll-samples のような「実時計で動かしたい
//     ロジック」のためだけの一時退避)
//
// recon.mjs の --deterministic フラグから呼ばれる。通常 recon はこのモジュールを読まない。

export async function installTimeVirtualization(page) {
  await page.addInitScript(() => {
    /* eslint-env browser */
    let vt = 0;
    const rafQueue = [];
    const timeouts = [];
    const clearedIntervals = new Set();
    let nextId = 1;

    // 元の実装を保存 (__pause__ で復帰できるように)。
    // performance.now は環境によっては非 writable なので、try で拾えた範囲で記録する。
    const origs = {
      Date: window.Date,
      performanceNow: performance.now.bind(performance),
      requestAnimationFrame: window.requestAnimationFrame.bind(window),
      cancelAnimationFrame: window.cancelAnimationFrame.bind(window),
      requestIdleCallback: window.requestIdleCallback
        ? window.requestIdleCallback.bind(window)
        : null,
      cancelIdleCallback: window.cancelIdleCallback
        ? window.cancelIdleCallback.bind(window)
        : null,
      setTimeout: window.setTimeout.bind(window),
      clearTimeout: window.clearTimeout.bind(window),
      setInterval: window.setInterval.bind(window),
      clearInterval: window.clearInterval.bind(window),
    };

    const OrigDate = origs.Date;
    class VirtualDate extends OrigDate {
      constructor(...args) {
        if (args.length === 0) {
          super(vt);
        } else {
          super(...args);
        }
      }
    }
    VirtualDate.now = () => vt;
    VirtualDate.UTC = OrigDate.UTC;
    VirtualDate.parse = OrigDate.parse;

    // 仮想時計版の実装 (install / resume でこれをぶら下げる)
    const virt = {};
    virt.Date = VirtualDate;
    virt.performanceNow = () => vt;
    virt.requestAnimationFrame = (cb) => {
      const id = nextId++;
      rafQueue.push({ id, cb });
      return id;
    };
    virt.cancelAnimationFrame = (id) => {
      const idx = rafQueue.findIndex((r) => r.id === id);
      if (idx >= 0) rafQueue.splice(idx, 1);
    };
    // requestIdleCallback は rAF で代替 (厳密な idle は模倣しない)
    virt.requestIdleCallback = (cb) => virt.requestAnimationFrame(() => cb({
      didTimeout: false,
      timeRemaining: () => 50,
    }));
    virt.cancelIdleCallback = virt.cancelAnimationFrame;
    virt.setTimeout = (cb, ms = 0, ...args) => {
      const id = nextId++;
      timeouts.push({ id, fireAt: vt + Math.max(0, Number(ms) || 0), cb, args });
      return id;
    };
    virt.clearTimeout = (id) => {
      const idx = timeouts.findIndex((t) => t.id === id);
      if (idx >= 0) timeouts.splice(idx, 1);
    };
    virt.setInterval = (cb, ms = 0, ...args) => {
      const intervalMs = Math.max(1, Number(ms) || 1);
      const id = nextId++;
      const wrap = () => {
        if (clearedIntervals.has(id)) return;
        try { cb(...args); } catch { /* ハンドラ内例外で取材を止めない */ }
        // まだ clear されていなければ再 push
        if (!clearedIntervals.has(id)) {
          timeouts.push({ id, fireAt: vt + intervalMs, cb: wrap, args: [] });
        }
      };
      timeouts.push({ id, fireAt: vt + intervalMs, cb: wrap, args: [] });
      return id;
    };
    virt.clearInterval = (id) => {
      clearedIntervals.add(id);
      const idx = timeouts.findIndex((t) => t.id === id);
      if (idx >= 0) timeouts.splice(idx, 1);
    };

    // 仮想時計を適用する (install 直後 + __resume__ 時に呼ぶ共通処理)
    const applyVirtual = () => {
      window.Date = virt.Date;
      try { performance.now = virt.performanceNow; }
      catch { /* 非 writable 環境は諦める */ }
      window.requestAnimationFrame = virt.requestAnimationFrame;
      window.cancelAnimationFrame = virt.cancelAnimationFrame;
      window.requestIdleCallback = virt.requestIdleCallback;
      window.cancelIdleCallback = virt.cancelIdleCallback;
      window.setTimeout = virt.setTimeout;
      window.clearTimeout = virt.clearTimeout;
      window.setInterval = virt.setInterval;
      window.clearInterval = virt.clearInterval;
    };

    // 元の実装に戻す (__pause__ 時)
    const applyOriginal = () => {
      window.Date = origs.Date;
      try { performance.now = origs.performanceNow; }
      catch { /* 非 writable 環境は諦める */ }
      window.requestAnimationFrame = origs.requestAnimationFrame;
      window.cancelAnimationFrame = origs.cancelAnimationFrame;
      if (origs.requestIdleCallback) window.requestIdleCallback = origs.requestIdleCallback;
      if (origs.cancelIdleCallback) window.cancelIdleCallback = origs.cancelIdleCallback;
      window.setTimeout = origs.setTimeout;
      window.clearTimeout = origs.clearTimeout;
      window.setInterval = origs.setInterval;
      window.clearInterval = origs.clearInterval;
    };

    // 初期化: 仮想時計を適用する
    let paused = false;
    applyVirtual();

    // 外部から 1 ステップ進める (仮想時計 + 発火のみ、DOM 同期は __sync__ に分離)
    window.__step__ = (dtMs) => {
      const dt = Math.max(0, Number(dtMs) || 0);
      vt += dt;

      // 発火可能な timeout を時刻順に実行 (実行中の cb が新規 timeout を積むことがある)
      // ガード 500 で無限ループを防ぎつつ、通常のアニメ初期化は十分実行できる範囲。
      for (let guard = 0; guard < 500; guard++) {
        const idx = timeouts.findIndex((t) => t.fireAt <= vt);
        if (idx < 0) break;
        const [fired] = timeouts.splice(idx, 1);
        try { fired.cb(...(fired.args || [])); } catch { /* 取材は止めない */ }
      }

      // rAF キューを吐き出す (rAF ハンドラ内で次の rAF を積むケースは次ステップで捕捉)
      const rafs = rafQueue.splice(0);
      for (const { cb } of rafs) {
        try { cb(vt); } catch { /* 取材は止めない */ }
      }

      return vt;
    };

    // 仮想時計と DOM (CSS animations / video) を 1 回だけ同期する。
    // __step__ 内で毎回呼ぶと巨大サイトで数秒かかるので、warmup 最終で 1 回だけ呼ぶ。
    window.__sync__ = () => {
      try {
        if (document.getAnimations) {
          for (const anim of document.getAnimations()) {
            try { anim.currentTime = vt; } catch { /* pending / finished は無視 */ }
          }
        }
      } catch { /* 非対応環境は諦める */ }
      try {
        for (const v of document.querySelectorAll('video')) {
          try { v.currentTime = vt / 1000; } catch { /* seekable でない動画は無視 */ }
        }
      } catch { /* 基本失敗しないが念のため */ }
      return vt;
    };

    window.__virtualTime__ = () => vt;

    // 段階 4: 仮想時計の一時停止/再開 API
    // scroll-samples のような「rAF で実時計を 2 フレーム待つ」ロジックが
    // 仮想時計下だと永久に resolve しないため、取材の該当区間だけ実時計に戻す。
    // 保留中の rafQueue / timeouts は pause 中も保持され、resume 後に引き続き発火可能。
    window.__pause__ = () => {
      if (paused) return false;
      applyOriginal();
      paused = true;
      return true;
    };
    window.__resume__ = () => {
      if (!paused) return false;
      applyVirtual();
      paused = false;
      return true;
    };
    window.__isPaused__ = () => paused;
  });
}

export async function warmupVirtualTime(page, steps, stepMs) {
  const stepCount = Math.max(0, Number(steps) || 0);
  const dt = Math.max(0, Number(stepMs) || 0);
  for (let i = 0; i < stepCount; i++) {
    try {
      await page.evaluate((ms) => {
        if (typeof window.__step__ === 'function') {
          window.__step__(ms);
        }
      }, dt);
    } catch {
      /* 1 フレームの失敗で warmup 全体は止めない */
    }
  }
  // 最終フレームで DOM を 1 回だけ同期 (CSS animations + video.currentTime)
  try {
    await page.evaluate(() => {
      if (typeof window.__sync__ === 'function') {
        window.__sync__();
      }
    });
  } catch {
    /* 同期失敗で warmup 全体は止めない */
  }
}
