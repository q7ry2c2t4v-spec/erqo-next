# RSRC-NEXTJS-QUALITY — Next.js 15+ 大規模プロジェクトの型安全・パフォーマンス・テスト・本番化

関連: RSRC-NEXTJS-ARCH, RSRC-WEBCLONE-RULES
タグ: nextjs, next15, next16, typescript, tsconfig, next-config-ts, eslint, eslint-flat-config, eslint-config-next, core-web-vitals, typedRoutes, turbopack, partial-prerendering, ppr, next-image, next-font, streaming, suspense, dynamic-import, vitest, playwright, testing, production-checklist, security-headers, csp, data-access-layer, taint-api, server-actions, route-segment-config, 大規模プロジェクト, ベストプラクティス, quality

## RSRC-NEXTJS-QUALITY.概要 — 概要

Next.js 15+ 大規模プロジェクトの「品質保証と本番出荷に直結するコーディング方法」を公式情報ベースで整理したページ。観点は 3 つ: (4) 型安全・Lint・規約、(5) パフォーマンス・ビルド最適化、(6) テスト戦略。セキュリティ/本番化は主に (4)(6) に関連するため同ページに含める。Pages Router・Next.js 14 以前の情報は除外。参照日は 2026-04-11。

前提: RSRC-NEXTJS-ARCH (アーキテクチャ・境界・データ取得) と併読。

## RSRC-NEXTJS-QUALITY.型安全-Lint — 型安全・Lint・規約

### `next.config.ts` で設定も型安全に

Next.js 15 から TypeScript の `next.config.ts` をサポート。`NextConfig` 型を import して補完付きで書ける:

```ts
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  typedRoutes: true,              // 15.5 で stable。next/link の href を型チェック
  experimental: {
    ppr: 'incremental',           // Partial Prerendering
    cacheComponents: true,        // use cache / cacheLife / cacheTag 有効化
    staleTimes: {                 // Router Cache の保持時間
      dynamic: 0,
      static: 180,
    },
  },
  images: {
    remotePatterns: [{ protocol: 'https', hostname: 'cdn.example.com' }],
  },
  logging: { fetches: { fullUrl: true } },
}

export default nextConfig
```

### TypeScript 設定

- **最低バージョン:** TypeScript 5.1 以上
- **`tsconfig.json`:** `create-next-app` 生成のデフォルトに `"strict": true` を必ず追加
- **`next-env.d.ts`:** 自動生成。git 管理しない
- **`PageProps<'/blog/[slug]'>` / `LayoutProps<'/dashboard'>`:** Next.js 15.5 以降のグローバル型ヘルパ。`next dev` / `next build` / `next typegen` で生成され、`params` / `searchParams` / `children` / parallel route slot を自動で型付ける

```tsx
// app/blog/[slug]/page.tsx
export default async function Page(props: PageProps<'/blog/[slug]'>) {
  const { slug } = await props.params
  return <h1>{slug}</h1>
}
```

- **`typedRoutes`:** `next/link` の `href` を文字列リテラル型でチェック。大規模ではリンク切れをビルド時に捕捉できる

### ESLint Flat Config (`eslint.config.mjs`)

Next.js 16 から `next lint` コマンドが削除され、ESLint を `package.json` の scripts 経由で直接呼ぶ前提。**Flat Config 必須**。

```js
// eslint.config.mjs
import { defineConfig, globalIgnores } from 'eslint/config'
import nextVitals from 'eslint-config-next/core-web-vitals'
import nextTs from 'eslint-config-next/typescript'

export default defineConfig([
  ...nextVitals,
  ...nextTs,
  globalIgnores(['.next/**', 'out/**', 'build/**', 'next-env.d.ts']),
])
```

- **`eslint-config-next/core-web-vitals`:** Next.js 推奨の基本ルールセット (`@next/eslint-plugin-next` の rule 群)。Core Web Vitals を壊しやすい書き方を検出 (`next/image` 非使用、`<a>` での内部遷移、`@next/next/no-img-element` など)
- **`eslint-config-next/typescript`:** `typescript-eslint` 由来の TypeScript 固有ルールを追加。`core-web-vitals` と併用する
- **Prettier との併用:** `eslint-config-prettier` を最後に並べて競合を消す
- **移行:** 旧 `.eslintrc.json` から Flat Config への codemod は `npx @next/codemod@canary migrate-eslint-flat-config`

### `package.json` scripts

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint",
    "lint:fix": "eslint --fix",
    "typecheck": "tsc --noEmit"
  }
}
```

Next.js 16 以降 `next build` は lint を自動実行しないため、CI では `typecheck` + `lint` + `build` を別ステップで回す。

### パスエイリアス

`tsconfig.json` で `@/*` を `src/*` にマップし、Next.js 側が自動追従する (設定不要):

```json
{ "compilerOptions": { "baseUrl": ".", "paths": { "@/*": ["src/*"] } } }
```

### セキュリティ規約 (型レベルで閉じる)

- **`server-only` import を DAL に強制** — 認証・DB アクセスは全て `lib/dal/` に閉じ、ファイル先頭に `import 'server-only'`
- **環境変数は `env.ts` で 1 回だけパースする** (zod などで検証)。`process.env` を生のまま散らさない
- **`NEXT_PUBLIC_` prefix 以外はクライアントに漏れない** (ビルド時に検証)
- **taint API** (`experimental_taintObjectReference` / `experimental_taintUniqueValue`): DAL を抜けたオブジェクトが Client にまで到達したときの最終防衛線。DAL での DTO 変換を主、taint API は副

## RSRC-NEXTJS-QUALITY.パフォーマンス — パフォーマンス・ビルド最適化

### Turbopack (16 でデフォルト化)

Next.js 16 から `next dev` / `next build` のデフォルトバンドラが Turbopack。Rust 製で CPU 並列を活用し、大規模プロジェクトの build/dev 速度が大幅改善。

```bash
next dev            # Turbopack (default)
next build          # Turbopack (default)
next dev --webpack  # opt-out (過渡期向け)
```

`next.config.ts` の `turbopack` オプションで loader / resolveAlias / resolveExtensions を設定可能。

### Partial Prerendering (PPR)

静的シェル + 動的ホール (Suspense 境界の中) を **1 HTTP レスポンス** で配信する新レンダリング戦略。14 まで「全ページ静的 or 全ページ動的」の 2 択だったのを、1 ルート内で混在できる。

**有効化 (段階的導入モード):**

```ts
// next.config.ts
const nextConfig: NextConfig = {
  experimental: { ppr: 'incremental' }
}
```

**ルート単位で opt-in:**

```tsx
// app/blog/[slug]/page.tsx
export const experimental_ppr = true

export default function Page() {
  return (
    <>
      <StaticHeader />                     {/* 静的シェルに入る */}
      <Suspense fallback={<Skeleton />}>
        <DynamicComments />                {/* 動的ホールとしてストリーミング */}
      </Suspense>
    </>
  )
}
```

**現状:** 15/16 時点で experimental。production で安定待ち。`'incremental'` で既存ルートを壊さず試せる。

### `next/image`

- `<img>` の代わりに `<Image>` を使うだけで自動で WebP/AVIF 変換・レスポンシブ・lazy loading・layout shift 防止
- ESLint ルール `@next/next/no-img-element` が `core-web-vitals` に含まれており違反を検出
- 外部 CDN を使う場合は `images.remotePatterns` を `next.config.ts` で明示

### `next/font`

```tsx
import { Inter } from 'next/font/google'
const inter = Inter({ subsets: ['latin'], display: 'swap' })

export default function RootLayout({ children }) {
  return <html className={inter.className}><body>{children}</body></html>
}
```

- ビルド時にフォントを取得して self-host 化 (外部リクエスト 0)
- CLS (Cumulative Layout Shift) を自動計測・調整
- Google Fonts / local fonts 両対応

### Dynamic Import + Suspense

- **Client 側の重い Component:** `next/dynamic` で code-split

```tsx
const Chart = dynamic(() => import('@/components/chart'), {
  loading: () => <Skeleton />,
  ssr: false, // 必要なら SSR 無効化
})
```

- **Server 側のデータ取得:** Suspense boundary で段階的ストリーミング

### `staleTimes` で Router Cache を制御

```ts
experimental: {
  staleTimes: { static: 180, dynamic: 0 }  // 秒
}
```

15 からデフォルトで dynamic=0 になったため、ダッシュボード系では明示的に数値を入れて Client 側キャッシュを活用する。

### その他の最適化

- **`loading.tsx`:** route 全体の streaming fallback
- **`<Link prefetch>`:** デフォルトで自動 prefetch (viewport 入ったとき)。広告・フッターなど使わないリンクは `prefetch={false}`
- **`generateStaticParams`:** 動的ルートを build 時に事前生成
- **Route Segment Config (`export const dynamic`, `revalidate`, `runtime`):** route 単位で動的/静的/Edge runtime を制御

## RSRC-NEXTJS-QUALITY.テスト — テスト戦略

### 基本方針 (公式推奨)

- **Unit / Component test:** Vitest (+ React Testing Library)
- **E2E test:** Playwright
- **async Server Component:** **Vitest では未対応**。E2E (Playwright) で検証する
- **同期 Server Component / Client Component:** Vitest で単体テスト可

### Vitest セットアップ

```bash
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react vite-tsconfig-paths
```

```ts
// vitest.config.mts
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
import tsconfigPaths from 'vite-tsconfig-paths'

export default defineConfig({
  plugins: [tsconfigPaths(), react()],
  test: { environment: 'jsdom' },
})
```

`create-next-app` の公式例 `with-vitest` を参照するとフル構成が手に入る。

### テストファイルの配置

- **`__tests__/` 集約** — `src/app/__tests__/blog.test.tsx` のように並列フォルダ。規模が大きいほど集約の方がナビゲート容易
- **Colocated** — `app/blog/page.test.tsx` のように並べる。`page.tsx` / `route.ts` 以外はルーティングされないので安全
- **大規模プロジェクトの実践:** features 単位で `__tests__/` を切り、共通 util は `src/test-utils/` に寄せる

### Playwright セットアップ

```bash
npm init playwright
```

```ts
// playwright.config.ts
import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './e2e',
  webServer: {
    command: 'npm run dev',           // または 'npm run build && npm run start'
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI,
    timeout: 120 * 1000,
  },
  use: { baseURL: 'http://localhost:3000' },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
  ],
})
```

- **`webServer`:** Playwright が自動で dev/build server を起動・待機
- **`reuseExistingServer: !process.env.CI`:** ローカルは再利用、CI は毎回クリーン起動
- **CI では `npm run build && npm run start`** の方が本番と挙動が近い (キャッシュ挙動も再現)

### テストの階層 (大規模)

```
e2e/                          ← Playwright (user flow)
├── auth.spec.ts
├── checkout.spec.ts
└── fixtures/

src/
├── app/...
├── components/
│   └── button.test.tsx       ← Vitest (component unit)
├── lib/
│   └── dal/
│       └── user.test.ts      ← Vitest (server unit、mock DB)
└── test-utils/
    ├── render.tsx
    └── factories.ts
```

## RSRC-NEXTJS-QUALITY.本番化 — セキュリティ・本番化

### Data Access Layer (DAL) 最優先

公式 Data Security Guide の中核:

- **全ての DB アクセス・外部 API 呼び出しを `lib/dal/` に集約**
- **`import 'server-only'` を先頭に**
- **DAL 内部で認可チェックを実施** (Server Action や page/layout の中ではなく DAL)
- **DTO (Data Transfer Object) に変換してから返す** — raw な ORM オブジェクトを Server Component に返さない
- **DAL 以外からは DB パッケージを import しない** (ESLint ルールで縛る)

### Server Actions

- POST 限定 + Origin/Host 比較 + SameSite cookie で CSRF は基本ガード
- それでも **Action 内部で認証 + 認可 + ownership check を再確認** (client-side restriction は防御にならない)
- **引数は必ず validate** (zod など)
- **Rate limit が必要な高コスト操作** (決済・メール送信) は明示的に制限

### 環境変数

- `.env.*` を `.gitignore` に入れる
- `NEXT_PUBLIC_` prefix の付いたものだけが Client に渡る
- 起動時に zod で `env.ts` として 1 箇所でバリデーション

### セキュリティヘッダ (CSP 含む)

- CSP は **middleware で nonce を発行** して動的に付ける (page 単位で新しい nonce)
- `next.config.ts` の `headers` で `Strict-Transport-Security` / `X-Frame-Options` / `Referrer-Policy` / `Permissions-Policy` を静的配布
- production では `unsafe-eval` 不要 (React/Next.js は production で eval を使わない)
- Vercel の [Security Headers ドキュメント](https://vercel.com/docs/headers/security-headers) にテンプレあり

### Route Segment Config

route 単位で強制する宣言:

```tsx
// force static (build 時生成、request 時は配信のみ)
export const dynamic = 'force-static'

// force dynamic (Data Cache / Full Route Cache を無効化、no-store を fetch に設定)
export const dynamic = 'force-dynamic'

// revalidate 時間 (ISR)
export const revalidate = 3600

// runtime
export const runtime = 'nodejs' | 'edge'
```

**注意:** `force-dynamic` は `no-store` を fetch cache のデフォルトに設定する (15 からの挙動)。広く効くので必要な route に限定する。

## RSRC-NEXTJS-QUALITY.推奨パターン — 推奨パターン

1. **`next.config.ts` + `NextConfig` 型 + `experimental` フラグを明示管理**
2. **`eslint.config.mjs` の Flat Config + `eslint-config-next/core-web-vitals` + `/typescript` を併用**
3. **`tsc --noEmit` を CI の独立ステップで回す** (`next build` は lint/type を必ずしも回さない)
4. **Turbopack をデフォルトに。`--webpack` は過渡期のみ**
5. **PPR を `'incremental'` で段階導入 → ルート単位 opt-in**
6. **画像は `<Image>`、フォントは `next/font`、動画/重い Chart は `next/dynamic`**
7. **Vitest (unit) + Playwright (E2E)。async Server Component は E2E で検証**
8. **Playwright の CI は `webServer` で `npm run build && npm run start`**
9. **`lib/dal/` + `import 'server-only'` + DTO 変換 + 認可チェック を徹底**
10. **CSP は middleware で nonce 付き動的発行**

## RSRC-NEXTJS-QUALITY.アンチパターン — アンチパターン

1. **`.eslintrc.json` を 15/16 以降も使い続ける** — Flat Config 前提の移行を進める
2. **`tsconfig.json` を `strict: false` のまま放置** — 型安全の土台が崩れる
3. **`next lint` を CI で使う** — 16 で削除。`eslint` を直接呼ぶ
4. **全ページ `force-dynamic`** — 高コスト。ルート単位で判断
5. **`useEffect` でデータ取得** — Server Component + Suspense に移す
6. **`<img>` / `<link rel="stylesheet">` / Google Fonts 直 link** — `core-web-vitals` ルールで違反
7. **Vitest で async Server Component を無理に単体テスト** — E2E に寄せる
8. **Playwright dev server を手動で立てる** — `webServer` で自動化
9. **DAL を省いて page/layout から直接 DB アクセス** — 認可漏れ・秘匿情報漏洩の温床
10. **`process.env.XXX` をあちこちで直接参照** — `env.ts` で 1 度だけ検証

## RSRC-NEXTJS-QUALITY.出典 — 出典

参照日: 2026-04-11

- [Configuration: TypeScript | Next.js](https://nextjs.org/docs/app/api-reference/config/typescript)
- [Configuration: next.config.js | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js)
- [Configuration: ESLint | Next.js](https://nextjs.org/docs/app/api-reference/config/eslint)
- [next.config.js: typedRoutes | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/typedRoutes)
- [next.config.js: staleTimes | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/staleTimes)
- [next.config.js: cacheComponents | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
- [API Reference: Turbopack | Next.js](https://nextjs.org/docs/app/api-reference/turbopack)
- [Getting Started: Partial Prerendering | Next.js](https://nextjs.org/docs/15/app/getting-started/partial-prerendering)
- [next.config.js: ppr | Next.js](https://nextjs.org/docs/15/app/api-reference/config/next-config-js/ppr)
- [Testing: Vitest | Next.js](https://nextjs.org/docs/app/guides/testing/vitest)
- [Testing: Playwright | Next.js](https://nextjs.org/docs/app/guides/testing/playwright)
- [Guides: Testing | Next.js](https://nextjs.org/docs/app/guides/testing)
- [Guides: Production | Next.js](https://nextjs.org/docs/app/guides/production-checklist)
- [Guides: Data Security | Next.js](https://nextjs.org/docs/app/guides/data-security)
- [Guides: Content Security Policy | Next.js](https://nextjs.org/docs/app/guides/content-security-policy)
- [How to Think About Security in Next.js | Next.js Blog](https://nextjs.org/blog/security-nextjs-server-components-actions)
- [Next.js 15 (release blog) | Next.js](https://nextjs.org/blog/next-15)
- [Next.js 15.5 | Next.js](https://nextjs.org/blog/next-15-5)
- [Next.js 16 (release blog) | Next.js](https://nextjs.org/blog/next-16)
- [Upgrading: Version 16 | Next.js](https://nextjs.org/docs/app/guides/upgrading/version-16)
- [Web server | Playwright](https://playwright.dev/docs/test-webserver)
- [next.js/examples/with-playwright | GitHub](https://github.com/vercel/next.js/tree/canary/examples/with-playwright)
- [next.js/examples/with-vitest | GitHub](https://github.com/vercel/next.js/tree/canary/examples/with-vitest)
