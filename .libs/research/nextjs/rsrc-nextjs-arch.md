# RSRC-NEXTJS-ARCH — Next.js 15+ 大規模プロジェクトのアーキテクチャ・境界・データ取得

関連: RSRC-NEXTJS-QUALITY, RSRC-WEBCLONE-RULES, RSRC-WEBCLONE-PIPELINE
タグ: nextjs, next15, next16, app-router, project-structure, server-components, rsc, client-components, use-client, server-only, data-fetching, caching, revalidate, revalidateTag, use-cache, cacheLife, cacheTag, cacheComponents, unstable_cache, server-actions, 大規模プロジェクト, ベストプラクティス, architecture, directory-structure, route-groups, private-folders, colocation, interleaving

## RSRC-NEXTJS-ARCH.概要 — 概要

Next.js 15+ の App Router 前提で「大規模プロジェクトで破綻しないコーディング方法」を公式情報ベースで整理したページ。観点は 3 つ: (1) ディレクトリ構成、(2) Server / Client 境界設計、(3) データ取得とキャッシュ戦略。各節は公式ドキュメントの確定情報を引用する。Pages Router・Next.js 14 以前の情報は除外。参照日は 2026-04-11。

前提バージョン:
- **Next.js 15.x** (App Router 安定版) 〜 **16.x** (Turbopack デフォルト) の範囲
- React 19 (Server Components / Server Actions / `use` hook 安定)
- TypeScript 5.1 以上

## RSRC-NEXTJS-ARCH.ディレクトリ構成 — ディレクトリ構成

### トップレベル

| フォルダ | 役割 |
|---|---|
| `app/` | App Router のルーティング本体 |
| `public/` | 静的アセット |
| `src/` | アプリコード全体 (任意だが大規模では必須) |

**`src/` 採用の判断基準:** プロジェクトルートに設定ファイル (`next.config.ts`, `tsconfig.json`, `eslint.config.mjs`, `package.json`) が増えるため、大規模では `src/app/` に寄せてアプリコードと設定を明確に分離する。公式も「application code from project configuration files」の分離目的で `src/` をサポート。

### ルーティング規約

1. **Route Segments = フォルダ** — `app/foo/bar/page.tsx` → `/foo/bar`
2. **ルート公開条件** — フォルダに `page.tsx` または `route.ts` が入った時点で公開される。逆に入れなければ非公開のまま
3. **Route Groups** — `(group)` で囲むと URL には出ず、レイアウトや論理グループ分け専用になる。`app/(marketing)/about/page.tsx` → `/about`。大規模では `(marketing)` `(app)` `(admin)` のような区切りで複数 Root Layout を使う
4. **Private Folders** — `_lib` のようにアンダースコア始まりにすると、そのフォルダ以下はルーティングから完全に除外される。UI・ルーティングのロジック分離に使う
5. **Dynamic Segments** — `[slug]`、`[...slug]` (catch-all)、`[[...slug]]` (optional catch-all)
6. **Parallel Routes / Intercepting Routes** — `@slot` / `(.)foo` で UI 差し込み・モーダル挿入

### Colocation ルール

App Router では `page.ts` / `route.ts` がないフォルダはルートとして公開されないため、**テスト・コンポーネント・ユーティリティを同じフォルダに置いても事故が起きない**。公式:

> "This means that **project files** can be **safely colocated** inside route segments in the `app` directory without accidentally being routable."

### 大規模での推奨レイアウト例

```
src/
├── app/
│   ├── (marketing)/
│   │   ├── layout.tsx          ← マーケ用 Root Layout
│   │   └── about/page.tsx
│   ├── (app)/
│   │   ├── layout.tsx          ← 認証済みユーザー用
│   │   ├── dashboard/
│   │   │   ├── _components/    ← private folder (route 化されない)
│   │   │   ├── _lib/
│   │   │   └── page.tsx
│   │   └── settings/page.tsx
│   ├── api/                    ← Route Handlers
│   └── layout.tsx              ← 共通 Root Layout
├── lib/                        ← 共通ユーティリティ (db, auth, utils)
│   ├── dal/                    ← Data Access Layer (server-only 強制)
│   └── env.ts
├── components/                 ← 共通 UI (ui/, icons/, forms/)
├── hooks/                      ← Client-only カスタムフック
└── types/                      ← 共通型
```

### `tsconfig.json` でのパスエイリアス

```json
{
  "compilerOptions": {
    "baseUrl": "src/",
    "paths": {
      "@/app/*": ["app/*"],
      "@/components/*": ["components/*"],
      "@/lib/*": ["lib/*"]
    }
  }
}
```

Next.js は `paths` / `baseUrl` をネイティブでサポート。相対パスの `../../../` を避けるため大規模では必須。

## RSRC-NEXTJS-ARCH.server-client境界 — Server / Client 境界設計

### 原則: デフォルトは Server Component

App Router の `page.tsx` / `layout.tsx` / `components/*` はデフォルトで **Server Component**。Client 化は必要最小限にとどめる。

**Server Component が向いている処理:**
- DB・API・ファイルシステムからのデータ取得
- API キー・トークンを扱う処理
- 大きな依存ライブラリを含むロジック (クライアントバンドルに載せたくないもの)
- SEO 用の静的コンテンツ

**Client Component が必要な処理:**
- `useState` / `useEffect` / `useRef` など React hooks
- `onClick` / `onChange` などのイベントハンドラ
- `window` / `localStorage` / `Navigator` などブラウザ API
- カスタムフック (サードパーティ含む)

### `"use client"` の配置ルール

ファイル先頭に `'use client'` を書くと、**そのファイルと、そのファイルがインポートするすべてのモジュールがクライアントバンドル側の module graph に入る**。子コンポーネントに個別に `'use client'` を書く必要はない。

```tsx
// app/ui/counter.tsx
'use client'
import { useState } from 'react'
export default function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
```

### Interleaving: Client の中に Server を差し込む

Client Component が Server Component を直接 import することはできない (Client 側の graph に巻き込まれるため)。**`children` / props として渡すことで Server Component を Client の中に「穴埋め」**できる。

```tsx
// app/ui/modal.tsx
'use client'
export default function Modal({ children }: { children: React.ReactNode }) {
  return <div>{children}</div>
}

// app/page.tsx (Server Component)
import Modal from './ui/modal'
import Cart from './ui/cart'  // これは Server Component のまま
export default function Page() {
  return <Modal><Cart /></Modal>
}
```

Cart は Server 側で先に評価され、RSC Payload として Client に送られる。Modal は Client で hydrate される。

### Context Provider は `children` を受け取る薄い Client Component で

React Context は Server Component で使えない。Provider は Client Component として作り、Root Layout から `{children}` を包む最小構造にする。**深いところに置くほど Static 最適化が効く**:

> "Render providers as deep as possible in the tree."

### `server-only` / `client-only` パッケージ

環境間違いによる事故 (API キー漏洩など) を **ビルド時に** 止めるためのガード:

```ts
// lib/dal/getUser.ts
import 'server-only'   // Client から import すればビルドエラー
export async function getUser() {
  return fetch('https://api', { headers: { authorization: process.env.API_KEY } })
}
```

`client-only` は逆方向 (window 前提のコードを Server から使う事故を防ぐ)。

### props はシリアライザブル必須

Server → Client に渡す props は React がシリアライズ可能なもの (文字列/数値/配列/プレーンオブジェクト/Date/Map/Set) に限られる。関数・Symbol・クラスインスタンスは不可。

## RSRC-NEXTJS-ARCH.データ取得 — データ取得とキャッシュ戦略

### 原則: 取得は Server Component で async/await

```tsx
export default async function Page() {
  const posts = await fetch('https://api.example.com/posts').then(r => r.json())
  return <ul>{posts.map(p => <li key={p.id}>{p.title}</li>)}</ul>
}
```

DB の場合は ORM (Drizzle / Prisma) を直接 import して同様に `await` する。

### デフォルトの `fetch` は **キャッシュされない** (Next.js 15+ の破壊的変更)

14 以前と違い、15 からは `fetch` は `no-store` がデフォルト。明示的にキャッシュしたい場合は `use cache` ディレクティブか Route Segment Config で制御する:

```tsx
// 方法 A: use cache ディレクティブ (新 API、cacheComponents 必須)
async function getPosts() {
  'use cache'
  return fetch('https://api.example.com/posts').then(r => r.json())
}

// 方法 B: Route Segment Config
export const dynamic = 'force-static'
```

### Request Memoization

同じ component tree 内で同一 URL への `fetch` は React 側で自動メモ化される (二重リクエストは 1 回に集約)。複数コンポーネントで同じデータが欲しいとき prop drilling せず直接 fetch してよい。

### 並列 vs 逐次

**並列 (推奨):**

```tsx
const artistPromise = getArtist(id)
const albumsPromise = getAlbums(id)
const [artist, albums] = await Promise.all([artistPromise, albumsPromise])
```

**逐次依存があるときは Suspense で待機中の後続をストリーム:**

```tsx
<Suspense fallback={<Spinner />}>
  <Playlists artistId={artist.id} />
</Suspense>
```

### `use cache` ディレクティブ + `cacheLife` / `cacheTag`

Next.js 15 で導入された新しいキャッシュ API。`next.config.ts` で `cacheComponents: true` を有効化してから使う:

```tsx
import { cacheLife, cacheTag } from 'next/cache'

async function getPosts() {
  'use cache'
  cacheLife('hours')        // 組み込みプロファイル: minutes/hours/days/biweekly
  cacheTag('posts')         // 複数可: cacheTag('posts', 'user-123')
  return db.select().from(posts)
}
```

`unstable_cache` は既存プロジェクトの移行パスとして残るが、新規は `use cache` に寄せる。

### 無効化: `revalidateTag` / `revalidatePath` / `updateTag`

```ts
'use server'
import { revalidateTag, revalidatePath, updateTag } from 'next/cache'

export async function createPost(data: FormData) {
  await db.insert(posts).values(...)
  revalidateTag('posts')          // 該当タグ付きキャッシュを次回アクセス時に破棄
  revalidatePath('/blog')         // パス単位の破棄
  // updateTag('posts')            // Server Action 内でのみ使用可。即時破棄 (read-your-own-writes)
}
```

### 非同期 Request API (15+ 破壊的変更)

`cookies()` / `headers()` / `draftMode()` / `params` / `searchParams` は **15 から非同期**。

```tsx
// 旧: const token = cookies().get('token')
const cookieStore = await cookies()
const token = cookieStore.get('token')

// page.tsx では
export default async function Page({ params, searchParams }: {
  params: Promise<{ slug: string }>
  searchParams: Promise<{ [k: string]: string | string[] | undefined }>
}) {
  const { slug } = await params
}
```

16 以降は同期アクセスを完全削除。codemod (`npx @next/codemod@canary next-async-request-api`) で一括移行可。

### Client Component でのデータ取得

原則 Server で取得するが、どうしても Client で必要なら:
- **`use` hook でサーバー由来の Promise を受け取る** (streaming 可)
- **SWR / TanStack Query** のライブラリを使う
- **Server Actions を呼ぶ** (mutations は基本こちら)

## RSRC-NEXTJS-ARCH.推奨パターン — 推奨パターン

1. **`(app)` / `(marketing)` / `(admin)` で Route Groups を切り、Root Layout を複数持つ**
2. **Private Folder `_components` / `_lib` / `_hooks` でルートフォルダ内の非ルーティング資産を分離する**
3. **`lib/dal/` に Data Access Layer を作り、`import 'server-only'` で強制する** (認可・DTO 変換・DB アクセスを集約)
4. **`'use client'` は葉に近い対話要素だけに付ける。layout / page はなるべく Server のまま**
5. **Client Component が Server Component を欲しいときは `children` 経由で interleave**
6. **キャッシュしたい fetch は `use cache` + `cacheTag` で宣言し、書き込み時に `revalidateTag` で破棄**
7. **`params` / `searchParams` / `cookies()` / `headers()` は必ず `await`**
8. **Context Provider は Root Layout の深い位置 (`{children}` だけを包む) に置く**

## RSRC-NEXTJS-ARCH.アンチパターン — アンチパターン

1. **`'use client'` を Root Layout に書く** — 全ページが Client 化してしまい、RSC の恩恵が消える
2. **Client Component から直接 Server Component を import する** — Client graph に取り込まれるので Server として実行されない
3. **Secret を Client Component の props で渡す** — シリアライズされてバンドルに埋め込まれる。`server-only` + DAL に閉じる
4. **`cookies()` / `params` を同期アクセス** — 15 で warning、16 で削除
5. **データ取得を `useEffect` で行う** — App Router では Server Component + Suspense で書き直す
6. **同じ `fetch` を prop drilling で引き回す** — Request Memoization が効くので直接呼んでよい
7. **「念のため」全部 `force-dynamic`** — Full Route Cache と Data Cache を両方捨てるためパフォーマンスが落ちる。必要なルートに限定する
8. **`revalidatePath('/')`** — 広すぎる invalidation。タグベースで絞る

## RSRC-NEXTJS-ARCH.出典 — 出典

参照日: 2026-04-11

- [Getting Started: Project Structure | Next.js](https://nextjs.org/docs/app/getting-started/project-structure)
- [Getting Started: Server and Client Components | Next.js](https://nextjs.org/docs/app/getting-started/server-and-client-components)
- [Directives: use client | Next.js](https://nextjs.org/docs/app/api-reference/directives/use-client)
- [Directives: use cache | Next.js](https://nextjs.org/docs/app/api-reference/directives/use-cache)
- [Getting Started: Caching and Revalidating | Next.js](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)
- [Functions: revalidateTag | Next.js](https://nextjs.org/docs/app/api-reference/functions/revalidateTag)
- [Functions: cacheLife | Next.js](https://nextjs.org/docs/app/api-reference/functions/cacheLife)
- [Functions: cacheTag | Next.js](https://nextjs.org/docs/app/api-reference/functions/cacheTag)
- [Functions: unstable_cache | Next.js](https://nextjs.org/docs/app/api-reference/functions/unstable_cache)
- [next.config.js: cacheComponents | Next.js](https://nextjs.org/docs/app/api-reference/config/next-config-js/cacheComponents)
- [Dynamic APIs are Asynchronous | Next.js](https://nextjs.org/docs/messages/sync-dynamic-apis)
- [Next.js 15 (release blog) | Next.js](https://nextjs.org/blog/next-15)
- [Upgrading: Version 15 | Next.js](https://nextjs.org/docs/app/guides/upgrading/version-15)
- [Upgrading: Version 16 | Next.js](https://nextjs.org/docs/app/guides/upgrading/version-16)
- [How to Think About Security in Next.js | Next.js Blog](https://nextjs.org/blog/security-nextjs-server-components-actions)
