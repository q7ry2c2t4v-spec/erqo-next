# L3 Next.js 15+ 専用コーディングルール

**適用対象:** Next.js プロジェクトの `.ts` / `.tsx` ファイル (プロジェクトルートに `next.config.ts|mjs|js` がある場合に機械判定される)
**前提:** 必ず `specs/06-coding-rules.md` (L1) + `specs/coding/l2-typescript.md` (L2) と合わせて適用する
**前提バージョン:** Next.js **15.x 以降** (App Router 前提。Pages Router・14 以前は対象外)
**詳細リサーチ:** `RSRC-NEXTJS-ARCH` / `RSRC-NEXTJS-QUALITY` (`.libs/research/nextjs/`)
**機械判定:** `python core/coding_rules.py src/app/page.tsx`

---

## 1. デザイン値トークン化 (Tailwind v4 `@theme`) **[MUST]**

ウェブクローンや UI 実装で「最高精度の再現」を保証するため、すべてのデザイン値を Tailwind v4 の `@theme` トークン経由で扱う。

### 禁止される書き方

- 直書き色値: `style={{ color: '#3b82f6' }}` / `className="bg-[#3b82f6]"`
- 直書き寸法: `className="p-[17px]"` / `style={{ padding: '17px' }}`
- 任意値ユーティリティ: `bg-[...]`, `p-[...]` は原則禁止

### 推奨される書き方

- `@theme` トークン経由: `className="bg-extracted-primary p-extracted-17"`
- トークンは `globals.css` の `@theme` ブロックで一元定義 (元サイトの実値や要望値を登録)

### 例外

- **動的な値 (props/state から計算):** 計算結果を `style` に渡す場合は許容 (例: `style={{ width: progress + '%' }}`)
- **過渡期の暫定:** リファクタの過渡期で `@theme` 化が間に合わない部分は `// TODO: tokenize` コメント付きで一時的に許容

### 理由

- ウェブクローン時に「どこに何の値があるか」を一元追跡できる
- 要望の上書きや差し替えが本棚ページから一括で反映できる
- VRT による pixel-perfect 検証が安定する

詳細な実装パイプラインは `.libs/research/webclone/rsrc-webclone-rules.md` を参照。

## 2. ディレクトリ構成 **[SHOULD]**

- **`src/` を有効化**してアプリコードと設定ファイルを分離
- **Route Groups `(marketing)` / `(app)` / `(admin)`** で論理分割し、それぞれに Root Layout を持たせる
- **ルーティング対象外の資産は Private Folder `_components/` / `_lib/` / `_hooks/`** に置く (アンダースコア始まりで route 化されない)
- **テスト・ユーティリティは Colocation 可** (`page.tsx` / `route.ts` がなければ route 化されない)

## 3. Server / Client 境界 **[MUST]**

- **デフォルトは Server Component** — `'use client'` は必要最小限
- `'use client'` は **Root Layout や Layout に書かない**。対話要素が必要な**葉のコンポーネント**にだけ付ける
- Client Component から **Server Component を直接 import しない**。`children` / props 経由で interleave する
- **`server-only` パッケージ** を DB アクセスや API キー扱うモジュールの先頭に `import 'server-only'` で書く (ビルド時にガード)
- **Context Provider** は Client Component で作り、Root Layout の**深い位置** (`{children}` だけを包む) に置く

### Interleaving パターン

```tsx
// app/ui/modal.tsx — Client
'use client'
export default function Modal({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}

// app/page.tsx — Server
import Modal from './ui/modal'
import Cart from './ui/cart'  // Server Component のまま
export default function Page() {
  return <Modal><Cart /></Modal>
}
```

Cart は Server 側で評価され、RSC Payload として Client に送られる。

## 4. データ取得とキャッシュ **[MUST]**

- **データ取得は Server Component で async/await**。`useEffect` でのデータ取得はしない
- **`fetch` のデフォルトは Next.js 15 から無キャッシュ**。キャッシュしたいときは `'use cache'` ディレクティブ + `cacheLife()` + `cacheTag()` を明示
- **キャッシュ無効化は `revalidateTag('<tag>')` をタグ単位で** (`revalidatePath('/')` のような広すぎる invalidation は禁止)
- **非同期 Request API** — `cookies()` / `headers()` / `draftMode()` / `params` / `searchParams` は必ず `await`
- **並列取得は `Promise.all`**、依存のあるものは `<Suspense>` 境界でストリーミング

```tsx
// 正しい書き方
export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params
  const cookieStore = await cookies()
  const token = cookieStore.get('token')
  // ...
}
```

## 5. ESLint Flat Config **[MUST]**

- **Flat Config (`eslint.config.mjs`) 必須** — 旧 `.eslintrc.json` は使わない
- `eslint-config-next/core-web-vitals` + `eslint-config-next/typescript` を併用
- `globalIgnores(['.next/**', 'out/**', 'build/**', 'next-env.d.ts'])` を必ず含める
- **Next.js 16 以降は `next lint` が削除**されるため、`package.json` scripts で `"lint": "eslint"` を直接呼ぶ
- CI では `typecheck` (`tsc --noEmit`) + `lint` + `build` を**別ステップ**で回す

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

## 6. `next.config.ts` + 型ヘルパ **[MUST]**

- **`next.config.ts` (TypeScript) を使う**。`import type { NextConfig } from 'next'` で型付け
- `typedRoutes: true` を有効化し、`next/link` の `href` を型チェック
- **`PageProps<'/blog/[slug]'>` / `LayoutProps<'/dashboard'>`** グローバル型ヘルパを使う (Next.js 15.5 以降で自動生成)

```ts
// next.config.ts
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {
  typedRoutes: true,
  experimental: {
    ppr: 'incremental',
    cacheComponents: true,
  },
}

export default nextConfig
```

## 7. パフォーマンス最適化 **[SHOULD]**

- **画像は必ず `<Image>`** (`next/image`)。`<img>` は `core-web-vitals` ルールで禁止される
- **フォントは必ず `next/font`** (Google Fonts 直 link 禁止)
- **重い Client Component は `next/dynamic`** で code-split
- **Partial Prerendering (PPR)** は `experimental: { ppr: 'incremental' }` で段階導入し、ルート単位で `export const experimental_ppr = true`
- **Route Segment Config** (`dynamic = 'force-dynamic' | 'force-static'`, `revalidate = <秒>`) はルート単位で必要なときだけ使う。**全ページ `force-dynamic` は禁止**

## 8. テスト戦略 **[MUST]**

- **Unit / Component:** Vitest + React Testing Library
- **E2E:** Playwright
- **async Server Component は Vitest で単体テストしない** — E2E (Playwright) でカバーする
- **Playwright は `webServer` + `reuseExistingServer: !process.env.CI`** パターンで自動サーバー管理
- **CI では `npm run build && npm run start`** を Playwright の webServer コマンドに使い、本番ビルドを検証する
- テスト配置は `__tests__/` 集約 or Colocation (どちらも MAY)。プロジェクト内で統一する

## 9. セキュリティと Data Access Layer **[MUST]**

- **Data Access Layer (DAL):** DB アクセスと外部 API 呼び出しは `src/lib/dal/` に集約し、各ファイル先頭に `import 'server-only'`
- **DAL 内部で認可チェック** — Server Action や page/layout ではなく DAL 層で実施
- **DTO 変換** — raw な ORM オブジェクトを Server Component に返さず、DTO に変換してから返す
- **Server Actions** — 引数を zod で validate + 認証 + 認可 + ownership check を毎回実施
- **CSP** — middleware で nonce を動的発行。静的ヘッダ (`Strict-Transport-Security` 等) は `next.config.ts` の `headers()` で配布
- **環境変数** — `NEXT_PUBLIC_` prefix のないものは絶対に Client に渡さない (`env.ts` で静的に分離 — L2 §3 参照)

## 10. アンチパターンまとめ

1. `'use client'` を Root Layout に書く
2. Client Component から Server Component を直接 import する
3. Secret を Client Component の props で渡す
4. `cookies()` / `params` を同期アクセス (15 で warning、16 で削除)
5. `useEffect` でデータ取得
6. 同じ `fetch` を prop drilling (Request Memoization が効くので直接呼んでよい)
7. 全ページ `force-dynamic`
8. `revalidatePath('/')` のような広すぎる invalidation
9. `<img>` / Google Fonts 直 link
10. Vitest で async Server Component を無理に単体テスト
11. DAL を省いて page/layout から直接 DB アクセス
12. 旧 `.eslintrc.json` を残したまま Next.js 16 へアップグレード
