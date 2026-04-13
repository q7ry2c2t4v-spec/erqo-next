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
//
// 制約 (RSRC-WEBANIM-HARDCASE §2 の注意点):
//   - Web Worker / OffscreenCanvas の内部時計は patch できない
//   - requestIdleCallback は rAF で代替注入 (厳密な idle は模倣しない)
//   - Promise / queueMicrotask は触らない (イベントループ整合性が崩れる)
//   - 仮想時計を入れると setTimeout 依存の初期化が止まるため、
//     必ず goto 後に warmupVirtualTime でステップを進めること
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

    const OrigDate = Date;
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
    window.Date = VirtualDate;

    try {
      performance.now = () => vt;
    } catch {
      /* performance.now が非 writable な環境は諦める */
    }

    window.requestAnimationFrame = (cb) => {
      const id = nextId++;
      rafQueue.push({ id, cb });
      return id;
    };
    window.cancelAnimationFrame = (id) => {
      const idx = rafQueue.findIndex((r) => r.id === id);
      if (idx >= 0) rafQueue.splice(idx, 1);
    };

    // requestIdleCallback は rAF で代替 (厳密な idle は模倣しない)
    window.requestIdleCallback = (cb) => window.requestAnimationFrame(() => cb({
      didTimeout: false,
      timeRemaining: () => 50,
    }));
    window.cancelIdleCallback = window.cancelAnimationFrame;

    window.setTimeout = (cb, ms = 0, ...args) => {
      const id = nextId++;
      timeouts.push({ id, fireAt: vt + Math.max(0, Number(ms) || 0), cb, args });
      return id;
    };
    window.clearTimeout = (id) => {
      const idx = timeouts.findIndex((t) => t.id === id);
      if (idx >= 0) timeouts.splice(idx, 1);
    };

    window.setInterval = (cb, ms = 0, ...args) => {
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
    window.clearInterval = (id) => {
      clearedIntervals.add(id);
      const idx = timeouts.findIndex((t) => t.id === id);
      if (idx >= 0) timeouts.splice(idx, 1);
    };

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
