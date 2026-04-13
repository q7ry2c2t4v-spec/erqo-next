#!/usr/bin/env node
// spector.mjs — WebGL の program から shader source を抽出する。
//
// RSRC-WEBANIM-HARDCASE §1 "WebGL 完全取材" の実装。
// Spector.js の capture は 1 フレーム分の描画 call しか含まず、初期化フェーズの
// compileShader / shaderSource / linkProgram は既に終わっているため取れない。
// そこで WebGL 標準 API (getAttachedShaders + getShaderSource) を使い、
// shader 本文を直接取り出す。
//
// 段階 2 では CURRENT_PROGRAM (描画ループで最後に bind された program) のみを対象とし、
// 段階 4 では useProgram を addInitScript で hook して全 program 履歴を追跡するように拡張。
// capture 時に window.__webglTrackedPrograms__ があれば全履歴を対象にし、無ければ
// 従来通り CURRENT_PROGRAM へフォールバックする。
//
// recon.mjs から呼ばれる 2 関数:
//   - installWebGLProgramTracking(page): page 生成直後に addInitScript で hook 仕込み (段階 4)
//   - captureWebGLShaders(page):         取材時に全 program から shader source を抽出
//
// 返却値 (captureWebGLShaders):
//   成功: {
//     capturedAt, url, canvases: [...],
//     programs: [{id, canvasIndex, contextType, vertexShader, fragmentShader}],
//     commandCount: 0,  // Spector 経由ではないため常に 0
//     note: ...
//   }
//   program 未検出: { ..., programs: [] }
//   例外:   recon.mjs 側で catch される

/**
 * page 生成直後に WebGL コンテキストの useProgram / attachShader / linkProgram を hook する。
 * 取材中にサイトが bind した全 program への参照を window.__webglTrackedPrograms__ に蓄積する。
 * @param {import('playwright').Page} page
 */
export async function installWebGLProgramTracking(page) {
  await page.addInitScript(() => {
    /* eslint-env browser */

    // canvas → getContext で得た gl ごとに program のリストを保持する。
    // evaluate 時に gl から getAttachedShaders → getShaderSource で GLSL を抽出するため、
    // program 単体ではなく {gl, program} のペアで持つ必要がある。
    const entries = [];
    // 重複排除用 (同一 program を二度 push しない)
    const seen = new WeakSet();

    const hookProto = (proto, contextType) => {
      if (!proto || typeof proto.useProgram !== 'function') return;
      const origUseProgram = proto.useProgram;
      proto.useProgram = function patchedUseProgram(program) {
        try {
          if (program && !seen.has(program)) {
            seen.add(program);
            entries.push({ gl: this, program, contextType });
          }
        } catch {
          /* 取材は止めない */
        }
        return origUseProgram.call(this, program);
      };
    };

    if (typeof window.WebGLRenderingContext !== 'undefined') {
      hookProto(window.WebGLRenderingContext.prototype, 'webgl');
    }
    if (typeof window.WebGL2RenderingContext !== 'undefined') {
      hookProto(window.WebGL2RenderingContext.prototype, 'webgl2');
    }

    // evaluate 側からはシリアライズ不可な WebGLProgram を返せないため、
    // ここで GLSL 抽出を完結させるコレクタを置く (capture 時に呼ばれる)。
    window.__webglCollectTrackedPrograms__ = () => {
      const canvases = [...document.querySelectorAll('canvas')];
      const canvasIndex = (node) => {
        const idx = canvases.indexOf(node);
        return idx < 0 ? -1 : idx;
      };
      const out = [];
      for (let i = 0; i < entries.length; i++) {
        const { gl, program, contextType } = entries[i];
        try {
          const attached = gl.getAttachedShaders(program) || [];
          let vertex = null;
          let fragment = null;
          for (const shader of attached) {
            const type = gl.getShaderParameter(shader, gl.SHADER_TYPE);
            const source = gl.getShaderSource(shader);
            if (!source) continue;
            if (type === gl.VERTEX_SHADER) vertex = source;
            else if (type === gl.FRAGMENT_SHADER) fragment = source;
          }
          if (vertex || fragment) {
            out.push({
              id: `program-${i}`,
              canvasIndex: canvasIndex(gl.canvas),
              contextType,
              vertexShader: vertex,
              fragmentShader: fragment,
            });
          }
        } catch {
          /* 破棄済み program 等は無視 */
        }
      }
      return out;
    };

    // 取材後に「何件 useProgram を検出したか」を確認できるマーカー
    window.__webglTrackedPrograms__ = entries;  // 参照共有 (count 取得用)
  });
}

/**
 * 全 program の shader source を取得する。
 * __webglTrackedPrograms__ があれば全履歴、無ければ CURRENT_PROGRAM の 1 つだけ返す。
 * @param {import('playwright').Page} page
 * @returns {Promise<object | null>}
 */
export async function captureWebGLShaders(page) {
  return await page.evaluate(() => {
    /* eslint-env browser */

    const canvasElements = [...document.querySelectorAll('canvas')];
    const canvasesSeen = canvasElements.map((c, ci) => {
      const rect = c.getBoundingClientRect();
      return {
        index: ci,
        width: c.width || Math.round(rect.width),
        height: c.height || Math.round(rect.height),
        tagId: c.id || null,
        className: typeof c.className === 'string' ? c.className.slice(0, 120) : '',
      };
    });

    // 段階 4: 事前 hook が install されていれば全 program 履歴を取る
    const trackedCount = Array.isArray(window.__webglTrackedPrograms__)
      ? window.__webglTrackedPrograms__.length
      : 0;
    if (typeof window.__webglCollectTrackedPrograms__ === 'function' && trackedCount > 0) {
      const programs = window.__webglCollectTrackedPrograms__();
      return {
        capturedAt: new Date().toISOString(),
        url: window.location.href,
        canvases: canvasesSeen,
        programs,
        commandCount: 0,
        note:
          `useProgram hook 経由で ${trackedCount} 件の program を記録 ` +
          '(段階 4: 全履歴取材)。',
      };
    }

    // 段階 2 フォールバック: CURRENT_PROGRAM のみ
    const programs = [];
    for (let ci = 0; ci < canvasElements.length; ci++) {
      const c = canvasElements[ci];
      let gl = null;
      try {
        gl = c.getContext('webgl2') || c.getContext('webgl');
      } catch {
        continue;
      }
      if (!gl) continue;

      const currentProgram = gl.getParameter(gl.CURRENT_PROGRAM);
      if (!currentProgram) continue;

      const attached = gl.getAttachedShaders(currentProgram) || [];
      let vertex = null;
      let fragment = null;
      for (const shader of attached) {
        const type = gl.getShaderParameter(shader, gl.SHADER_TYPE);
        const source = gl.getShaderSource(shader);
        if (!source) continue;
        if (type === gl.VERTEX_SHADER) vertex = source;
        else if (type === gl.FRAGMENT_SHADER) fragment = source;
      }

      if (vertex || fragment) {
        programs.push({
          id: `canvas-${ci}-current`,
          canvasIndex: ci,
          contextType: gl instanceof WebGL2RenderingContext ? 'webgl2' : 'webgl',
          vertexShader: vertex,
          fragmentShader: fragment,
        });
      }
    }

    return {
      capturedAt: new Date().toISOString(),
      url: window.location.href,
      canvases: canvasesSeen,
      programs,
      commandCount: 0,
      note:
        'CURRENT_PROGRAM based extraction (WebGL standard API, フォールバック)。' +
        '全 program 履歴が欲しければ installWebGLProgramTracking を事前に呼ぶ。',
    };
  });
}
