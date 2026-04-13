#!/usr/bin/env node
// spector.mjs — WebGL の現在 bind されている program から shader source を抽出する。
//
// RSRC-WEBANIM-HARDCASE §1 "WebGL 完全取材" の実装。
// Spector.js の capture は 1 フレーム分の描画 call しか含まず、初期化フェーズの
// compileShader / shaderSource / linkProgram は既に終わっているため取れない。
// そこで WebGL 標準 API (getAttachedShaders + getShaderSource) を使い、
// 各 canvas の CURRENT_PROGRAM から shader 本文を直接取り出す。
//
// recon.mjs から `captureWebGLShaders(page)` として呼ばれる。
//
// 返却値:
//   成功: {
//     capturedAt, url, canvases: [...], programs: [{id, canvasIndex, vertexShader, fragmentShader}],
//     commandCount: 0,  // Spector 経由ではないため常に 0
//   }
//   未検出: { ..., programs: [] }
//   例外:   recon.mjs 側で catch される (null ではなく throw 流儀)

/**
 * ページ内の全 canvas から CURRENT_PROGRAM の shader source を取得する。
 * @param {import('playwright').Page} page
 * @returns {Promise<object | null>}
 */
export async function captureWebGLShaders(page) {
  return await page.evaluate(() => {
    /* eslint-env browser */

    const canvases = [...document.querySelectorAll('canvas')];
    const canvasesSeen = [];
    const programs = [];

    canvases.forEach((c, ci) => {
      let gl = null;
      try {
        gl = c.getContext('webgl2') || c.getContext('webgl');
      } catch {
        return;
      }
      if (!gl) return;

      const rect = c.getBoundingClientRect();
      canvasesSeen.push({
        index: ci,
        width: c.width || Math.round(rect.width),
        height: c.height || Math.round(rect.height),
        tagId: c.id || null,
        className: typeof c.className === 'string' ? c.className.slice(0, 120) : '',
      });

      const currentProgram = gl.getParameter(gl.CURRENT_PROGRAM);
      if (!currentProgram) return;

      const attached = gl.getAttachedShaders(currentProgram) || [];
      let vertex = null;
      let fragment = null;
      for (const shader of attached) {
        const type = gl.getShaderParameter(shader, gl.SHADER_TYPE);
        const source = gl.getShaderSource(shader);
        if (!source) continue;
        // VERTEX_SHADER = 0x8B31 (35633), FRAGMENT_SHADER = 0x8B30 (35632)
        if (type === gl.VERTEX_SHADER) vertex = source;
        else if (type === gl.FRAGMENT_SHADER) fragment = source;
      }

      if (vertex || fragment) {
        programs.push({
          id: `canvas-${ci}-current`,
          canvasIndex: ci,
          vertexShader: vertex,
          fragmentShader: fragment,
        });
      }
    });

    return {
      capturedAt: new Date().toISOString(),
      url: window.location.href,
      canvases: canvasesSeen,
      programs,
      commandCount: 0,
      note:
        'CURRENT_PROGRAM based extraction (WebGL standard API). ' +
        '全 program 履歴は取らないため、描画ループで bind されている最終 program のみが対象。',
    };
  });
}
