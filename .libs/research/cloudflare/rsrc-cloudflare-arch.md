# RSRC-CLOUDFLARE-ARCH — Cloudflare Workers 大規模プロジェクトのランタイム・構成・ストレージ

関連: RSRC-CLOUDFLARE-QUALITY, RSRC-NEXTJS-ARCH, RSRC-PYTHON-ARCH
タグ: cloudflare, cloudflare-workers, workers, wrangler, wrangler-v4, wrangler-jsonc, compatibility-date, compatibility-flags, nodejs-compat, typescript, hono, bindings, kv, r2, d1, durable-objects, queues, workflows, hyperdrive, static-assets, sqlite-storage, block-concurrency-while, alarms, websocket-hibernation, v8-isolates, 大規模プロジェクト, ベストプラクティス, architecture

## RSRC-CLOUDFLARE-ARCH.概要 — 概要

Cloudflare Workers + TypeScript で大規模サーバーサイドアプリを組むときのランタイム理解・構成・ストレージ選択を公式情報ベースで整理したページ。観点は 3 つ: (1) Workers ランタイムと `wrangler.jsonc` 設定、(2) Hono フレームワーク、(3) Durable Objects / D1 / KV / R2 / Queues / Workflows の使い分け。参照日は 2026-04-11。

**前提バージョン:**
- **Wrangler 4.x 以降** (`wrangler.jsonc` 推奨、旧 `wrangler.toml` も後方互換)
- **`compatibility_date: "2024-09-23"` 以降** (`nodejs_compat` 有効化の最低条件)
- **`@cloudflare/workers-types` 最新**
- Python Workers / Hono / Durable Objects SQLite storage に対応した最新ランタイム

## RSRC-CLOUDFLARE-ARCH.ランタイム — Workers ランタイムの理解

### V8 isolates モデル

Cloudflare Workers は **V8 isolate** の上で動く。Lambda や VM とは違い:

- **コールドスタート実質ゼロ** (< 5ms)
- **リクエストごとに isolate は破棄されない** — 同じ isolate で複数リクエストを連続処理
- **グローバル変数はリクエスト間で共有される可能性がある** — ステートレス設計必須
- **CPU time 制限** (無料: 10ms, 有料: 30s default、Paid で延長可) / **wall clock 制限**は基本なし
- **メモリ 128MB 制限**

### リクエストモデル

```ts
// src/index.ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    return new Response("Hello")
  }
} satisfies ExportedHandler<Env>
```

- `env` にすべての Bindings (KV / R2 / D1 / DO / Queues / Workflows / Secrets / vars) が入る
- `ctx.waitUntil(promise)` でレスポンス送信後の非同期処理を continue
- `ctx.passThroughOnException()` で例外時にオリジンへ流す

### Node.js 互換

`compatibility_flags` に `nodejs_compat` を入れると `node:*` の一部が使える:

```jsonc
{
  "compatibility_date": "2024-09-23",
  "compatibility_flags": ["nodejs_compat"]
}
```

**併用で `@types/node` を devDependencies に入れる** (型が欲しいため)。2024-09-23 以降で built-in API は fs/path/crypto/stream/buffer 等が揃う。

## RSRC-CLOUDFLARE-ARCH.wrangler設定 — `wrangler.jsonc` の書き方

### 最小構成

```jsonc
// wrangler.jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-12-01",
  "compatibility_flags": ["nodejs_compat"],

  // Observability (有料プラン)
  "observability": {
    "enabled": true,
    "head_sampling_rate": 1
  }
}
```

### Bindings の書き方

```jsonc
{
  // プレーン環境変数 (非秘密)
  "vars": {
    "APP_ENV": "production",
    "API_BASE_URL": "https://api.example.com"
  },

  // Secrets (宣言のみ、値は wrangler secret put で設定)
  "secrets": {
    "required": ["STRIPE_API_KEY", "OPENAI_API_KEY"]
  },

  // KV namespace
  "kv_namespaces": [
    { "binding": "SESSION_KV", "id": "abc123def456..." }
  ],

  // R2 bucket
  "r2_buckets": [
    { "binding": "ASSETS_BUCKET", "bucket_name": "my-assets" }
  ],

  // D1 database
  "d1_databases": [
    { "binding": "DB", "database_name": "app-db", "database_id": "..." }
  ],

  // Durable Objects
  "durable_objects": {
    "bindings": [
      { "name": "ROOM", "class_name": "Room" }
    ]
  },
  "migrations": [
    { "tag": "v1", "new_sqlite_classes": ["Room"] }
  ],

  // Queues
  "queues": {
    "producers": [{ "queue": "jobs", "binding": "JOBS_QUEUE" }],
    "consumers": [{ "queue": "jobs", "max_batch_size": 10, "max_batch_timeout": 5 }]
  },

  // Workflows
  "workflows": [
    { "name": "image-processing", "binding": "IMAGE_WF", "class_name": "ImageProcessingWorkflow" }
  ],

  // Static Assets
  "assets": { "directory": "./public", "binding": "ASSETS" }
}
```

### 環境ごとの設定 (`env`)

```jsonc
{
  "name": "my-worker",
  "main": "src/index.ts",
  "vars": { "APP_ENV": "production" },

  "env": {
    "staging": {
      "name": "my-worker-staging",
      "vars": { "APP_ENV": "staging" }
    },
    "dev": {
      "vars": { "APP_ENV": "dev" }
    }
  }
}
```

```bash
wrangler deploy --env staging
```

### `wrangler types` による自動型生成

```bash
wrangler types
```

これで `worker-configuration.d.ts` が自動生成され、`env` 型が完全に型付けされる。`tsconfig.json` の `types` に含める。

## RSRC-CLOUDFLARE-ARCH.hono — Hono フレームワーク

### なぜ Hono か

- **Web 標準ベース** (`Request` / `Response` をそのまま扱う)
- **ファーストクラスの TypeScript サポート** — Bindings 型が `c.env` に反映
- **RPC 型クライアント** (`hc<AppType>()`) — tRPC 風に型付きクライアント自動生成
- **バンドルサイズ極小** — Workers のサイズ制限に優しい
- **Cloudflare 公式がフレームワーク選択肢として正式推奨**

### 基本構成

```ts
// src/index.ts
import { Hono } from 'hono'

type Bindings = {
  DB: D1Database
  SESSION_KV: KVNamespace
  ASSETS_BUCKET: R2Bucket
  STRIPE_API_KEY: string
}

const app = new Hono<{ Bindings: Bindings }>()

app.get('/', (c) => c.text('Hello'))
app.get('/users/:id', async (c) => {
  const user = await c.env.DB.prepare('SELECT * FROM users WHERE id = ?')
    .bind(c.req.param('id'))
    .first()
  return c.json(user)
})

export default app
```

### アプリ分割 (大規模)

```ts
// src/routes/users.ts
const users = new Hono<{ Bindings: Bindings }>()
  .get('/', (c) => c.json([]))
  .get('/:id', (c) => c.json({ id: c.req.param('id') }))
  .post('/', async (c) => c.json({ ok: true }, 201))

export default users
```

```ts
// src/index.ts
import users from './routes/users'
import books from './routes/books'

const app = new Hono<{ Bindings: Bindings }>()
  .route('/users', users)
  .route('/books', books)

export type AppType = typeof app      // RPC クライアント用
export default app
```

### Middleware と `createFactory`

```ts
import { createFactory } from 'hono/factory'
const factory = createFactory<{ Bindings: Bindings }>()

const authMiddleware = factory.createMiddleware(async (c, next) => {
  const token = c.req.header('Authorization')
  if (!token) return c.json({ error: 'unauthorized' }, 401)
  c.set('userId', await verify(token, c.env.JWT_SECRET))
  await next()
})

const handlers = factory.createHandlers(
  authMiddleware,
  (c) => c.json({ userId: c.var.userId })
)

app.get('/me', ...handlers)
```

### Zod Validator

```ts
import { zValidator } from '@hono/zod-validator'
import { z } from 'zod'

const createUserSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
})

app.post('/users', zValidator('json', createUserSchema), async (c) => {
  const data = c.req.valid('json')  // 型付き
  // ...
})
```

### RPC クライアント (hc)

```ts
// client.ts (別プロジェクトまたは同一プロジェクトの Client 側)
import { hc } from 'hono/client'
import type { AppType } from './server'

const client = hc<AppType>('https://api.example.com')
const res = await client.users[':id'].$get({ param: { id: '123' } })
const user = await res.json()   // 型推論
```

## RSRC-CLOUDFLARE-ARCH.ストレージ — ストレージ選択

### 用途別の選び方

| ストレージ | 用途 | 一貫性 | 備考 |
|---|---|---|---|
| **Workers KV** | セッション、設定、読取多数・書込少数 | Eventual (global propagation 60s 前後) | 1 value 25MB 上限、無制限 reads |
| **R2** | 画像・動画・ファイル配信、大容量 | Strong | S3 互換 API、egress 無料 |
| **D1** | SQL 状態、リレーショナル | Strong (single-region) | SQLite ベース、bindings 経由で遅延小 |
| **Durable Objects** | per-user state、WebSocket room、カウンタ、強整合が必要な coordination | Strict Serializability | 1 DO = 1 SQLite DB (new)、グローバル配置 |
| **Queues** | fan-out、バッファリング、非同期 mutation | - | 簡易メッセージキュー |
| **Workflows** | 多段階・永続化を伴う実行フロー | - | ステート永続化・リトライ自動、日をまたぐ実行 OK |
| **Hyperdrive** | 外部 PostgreSQL 高速化 | - | Connection pooling + cache |

**原則:**
- **バインディング (env.XXX) で呼ぶ** — REST API 経由は使わない (ネットワークホップなし、認証オーバーヘッドなし)
- **設定・セッション → KV**、**リレーショナル → D1**、**per-entity coordination → DO**、**ファイル → R2**

### Durable Objects の SQLite ストレージ (新)

旧 key-value ストレージは置き換え対象。**新規プロジェクトは SQLite**:

```ts
import { DurableObject } from 'cloudflare:workers'

export class Room extends DurableObject {
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env)
    ctx.blockConcurrencyWhile(async () => {
      ctx.storage.sql.exec(`
        CREATE TABLE IF NOT EXISTS messages (
          id INTEGER PRIMARY KEY,
          text TEXT NOT NULL,
          created_at INTEGER NOT NULL
        )
      `)
    })
  }

  async postMessage(text: string) {
    this.ctx.storage.sql.exec(
      'INSERT INTO messages (text, created_at) VALUES (?, ?)',
      text, Date.now()
    )
  }

  async getMessages() {
    return [...this.ctx.storage.sql.exec('SELECT * FROM messages ORDER BY id DESC LIMIT 100')]
  }
}
```

### Durable Objects 原則

- **`getByName()` で決定論ルーティング** — 同じ name → 同じ instance:

```ts
const stub = env.ROOM.getByName(`room-${roomId}`)
await stub.postMessage('hello')
```

- **`blockConcurrencyWhile()` は初期化専用** — I/O を含めない (外部 fetch/KV/R2 呼出中は全リクエストが止まる)
- **`alarm()` API で遅延処理・定期処理・TTL** を実装

```ts
async alarm() {
  // 定期実行される
  await this.cleanupOldMessages()
  await this.ctx.storage.setAlarm(Date.now() + 60_000)  // 1 分後に再実行
}
```

- **Input Gates / Output Gates** は自動 — read-modify-write の競合は心配しなくてよい
- **WebSocket Hibernation** — 長時間接続でも isolate がイビクトできるようにする公式 API (`state.acceptWebSocket`)

### Workflows (多段階・永続ステップ)

長時間・多段階のフローを **step 単位で永続化** するランタイム:

```ts
import { WorkflowEntrypoint, WorkflowEvent, WorkflowStep } from 'cloudflare:workers'

export class ImageProcessingWorkflow extends WorkflowEntrypoint<Env, Params> {
  async run(event: WorkflowEvent<Params>, step: WorkflowStep) {
    const imageData = await step.do('fetch image', async () => {
      const obj = await this.env.BUCKET.get(event.payload.imageKey)
      return obj ? await obj.arrayBuffer() : null
    })

    await step.sleep('wait 1 hour', '1 hour')

    const approval = await step.waitForEvent('approval', {
      event: 'approved',
      timeout: '24 hours'
    })

    await step.do('publish', async () => {
      // ...
    })
  }
}
```

- **`step.do`** — 関数を 1 step として記録。失敗時は自動リトライ。成功時は結果が永続化される
- **`step.sleep` / `step.sleepUntil`** — 秒〜日単位で眠る。CPU は消費しない
- **`step.waitForEvent`** — 外部イベント待ち

**Queues vs Workflows:**
- **Queues** — 単純な非同期処理、バッチ処理、fan-out
- **Workflows** — 多段階・長時間・人間の承認待ち・複雑なリトライ

## RSRC-CLOUDFLARE-ARCH.推奨パターン — 推奨パターン

1. **`wrangler.jsonc` で設定 (旧 `wrangler.toml` 非推奨)、`compatibility_date` は新規 deploy のたびに更新**
2. **`nodejs_compat` を有効化し、`@types/node` も入れる**
3. **`wrangler types` を CI/pre-commit で自動実行し、`env` の型を維持**
4. **Hono を採用し、`Hono<{ Bindings: Env }>` で env を型付け**
5. **`app.route('/users', users)` でルート分割、`export type AppType` で RPC 型クライアント可能化**
6. **`zValidator` + zod で入力検証を middleware 層に集約**
7. **`hc<AppType>()` で型付きクライアントを作り、フロント (Next.js 等) から型安全に呼ぶ**
8. **ストレージ選択はこの原則で: 設定=KV / リレーショナル=D1 / per-entity=DO (SQLite) / ファイル=R2**
9. **Durable Objects は `getByName()` で決定論ルーティング、`blockConcurrencyWhile` は初期化のみ、alarm で定期処理**
10. **長時間・多段階のビジネスフローは Workflows、単純非同期は Queues**
11. **`vars` はプレーン変数、`secrets` は `wrangler secret put` で注入、`.dev.vars` はローカル開発用**

## RSRC-CLOUDFLARE-ARCH.アンチパターン — アンチパターン

1. **`wrangler.toml` をそのまま使い続ける** — `wrangler.jsonc` に移行 (コメント書けて保守性が上がる)
2. **Node.js の前提 (`fs.readFileSync` 同期 I/O・`process` 直接参照) で書く** — Workers は `ctx.waitUntil` やバインディング経由
3. **Workers のグローバル変数に状態を保存する** — isolate は reuse されるが保証はない。`ctx.waitUntil` で KV/DO に書く
4. **`wrangler secret put` せず `vars` に API key を書く** — git に漏れる
5. **`blockConcurrencyWhile` の中で fetch / KV / R2** — 全リクエストが長時間止まる
6. **`setAlarm` を constructor で呼ぶ** — TTL が継続的に延長されて alarm が発火しない
7. **Durable Objects を `idFromName()` で毎回ランダムに生成** — 同一 entity が別インスタンスに散る。`getByName` で決定論的に
8. **全部の状態を 1 つの Durable Object に詰める** — スケールしない。entity (ユーザー/部屋/セッション) 単位に分ける
9. **Workflows を単発処理に使う** — Queues で十分
10. **REST API (`fetch('https://api.cloudflare.com/client/v4/...')`) でバインディング先を呼ぶ** — バインディング経由で呼べばネットワークホップなし

## RSRC-CLOUDFLARE-ARCH.出典 — 出典

参照日: 2026-04-11

- [Cloudflare Workers docs | developers.cloudflare.com](https://developers.cloudflare.com/workers/)
- [Wrangler Configuration | developers.cloudflare.com](https://developers.cloudflare.com/workers/wrangler/configuration/)
- [Compatibility flags | developers.cloudflare.com](https://developers.cloudflare.com/workers/configuration/compatibility-flags/)
- [Node.js compatibility | developers.cloudflare.com](https://developers.cloudflare.com/workers/runtime-apis/nodejs/)
- [Write Cloudflare Workers in TypeScript | developers.cloudflare.com](https://developers.cloudflare.com/workers/languages/typescript/)
- [Workers Best Practices | developers.cloudflare.com](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/)
- [Bindings (env) | developers.cloudflare.com](https://developers.cloudflare.com/workers/runtime-apis/bindings/)
- [Durable Objects Overview | developers.cloudflare.com](https://developers.cloudflare.com/durable-objects/)
- [Rules of Durable Objects | developers.cloudflare.com](https://developers.cloudflare.com/durable-objects/best-practices/rules-of-durable-objects/)
- [Access Durable Objects Storage | developers.cloudflare.com](https://developers.cloudflare.com/durable-objects/best-practices/access-durable-objects-storage/)
- [Durable Objects Limits | developers.cloudflare.com](https://developers.cloudflare.com/durable-objects/platform/limits/)
- [Choosing a data or storage product | developers.cloudflare.com](https://developers.cloudflare.com/workers/platform/storage-options/)
- [Cloudflare Workflows | developers.cloudflare.com](https://developers.cloudflare.com/workflows/)
- [Cloudflare Queues | developers.cloudflare.com](https://developers.cloudflare.com/queues/)
- [D1 docs | developers.cloudflare.com](https://developers.cloudflare.com/d1/)
- [Hono: Cloudflare Workers | hono.dev](https://hono.dev/docs/getting-started/cloudflare-workers)
- [Hono: Best Practices | hono.dev](https://hono.dev/docs/guides/best-practices)
- [Hono: RPC | hono.dev](https://hono.dev/docs/guides/rpc)
- [Hono: Middleware | hono.dev](https://hono.dev/docs/guides/middleware)
