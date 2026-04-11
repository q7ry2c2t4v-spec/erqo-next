# L3 Cloudflare Workers 専用コーディングルール

**適用対象:** Cloudflare Workers プロジェクトの `.ts` / `.tsx` ファイル (プロジェクトルートに `wrangler.jsonc|json|toml` があるか、対象ファイルが `workers/` 配下にある場合に機械判定される)
**前提:** 必ず `specs/06-coding-rules.md` (L1) + `specs/coding/l2-typescript.md` (L2) と合わせて適用する
**前提バージョン:** **Wrangler 4.x 以降** / `compatibility_date: "2024-09-23"` 以降
**詳細リサーチ:** `RSRC-CLOUDFLARE-ARCH` / `RSRC-CLOUDFLARE-QUALITY` (`.libs/research/cloudflare/`)
**機械判定:** `python core/coding_rules.py workers/src/index.ts`

---

## 1. V8 isolates モデルに即した書き方 **[MUST]**

- **Workers はリクエストごとに isolate が破棄されない** — グローバル変数に状態を持たせない (reuse は起こるが保証なし)
- **`ctx.waitUntil(promise)`** でレスポンス送信後の非同期処理を継続する
- **`ctx.passThroughOnException()`** で例外時にオリジンへフォールバック
- **Node.js の同期 I/O (`fs.readFileSync` 等) は使わない** — Bindings 経由 or `fetch`
- **`process.*` を直接参照しない** — 環境変数は `env` 引数経由で受け取る

```ts
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    ctx.waitUntil(logRequest(request, env))
    return handleRequest(request, env)
  }
} satisfies ExportedHandler<Env>
```

## 2. `wrangler.jsonc` で設定を管理 **[MUST]**

- **`wrangler.jsonc` を使う** (旧 `wrangler.toml` は新規プロジェクトで採用しない — コメントが書けて保守性が高い)
- **`compatibility_date` を明示** し、大きな機能追加時は更新
- **`compatibility_flags: ["nodejs_compat"]`** を有効化し、`@types/node` を devDependencies に追加
- **`observability.enabled: true`** を本番で有効化

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-12-01",
  "compatibility_flags": ["nodejs_compat"],
  "observability": { "enabled": true, "head_sampling_rate": 1 }
}
```

### `wrangler types` を CI の第 1 ステップに **[MUST]**

```bash
wrangler types && tsc --noEmit
```

`worker-configuration.d.ts` が自動生成されて `env` が完全に型付けされる。bindings 追加時の型エラーを自動的に検出するため CI の最初に必ず実行する。

## 3. Secrets と環境変数の管理 **[MUST]**

| 種類 | 用途 | 書き込み先 |
|---|---|---|
| `vars` | 非秘密の設定値 | `wrangler.jsonc` の `"vars": {}` |
| `secrets` | API キー・トークン | `wrangler secret put` (対話) or `wrangler secret bulk` |
| `.dev.vars` | ローカル開発用 | リポジトリ外 (`.gitignore` 必須) |

- **`secrets.required`** を `wrangler.jsonc` で宣言 — 欠落時に警告、`.dev.vars` / `.env` から想定外の値が混入しない
- **`.env` と `.dev.vars` を両方置かない** — `.dev.vars` があれば `.env` は無視される
- **`vars` に API キーを書かない** — git に漏れる、必ず `secrets` に
- **`wrangler secret put` は毎回新バージョンをデプロイする** — 段階ロールアウトしたければ `wrangler versions secret put` を使う

## 4. Hono フレームワークの採用 **[SHOULD]**

Cloudflare 公式推奨のフレームワーク。Bindings 型と完全連動し、RPC 型クライアントが自動生成できる。

### Bindings 型定義

```ts
import { Hono } from 'hono'

type Bindings = {
  DB: D1Database
  SESSION_KV: KVNamespace
  ASSETS_BUCKET: R2Bucket
  ROOM: DurableObjectNamespace
  STRIPE_API_KEY: string
  JWT_SECRET: string
}

const app = new Hono<{ Bindings: Bindings }>()
```

### アプリ分割 (大規模)

```ts
// src/routes/users.ts
const users = new Hono<{ Bindings: Bindings }>()
  .get('/', (c) => c.json([]))
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

export type AppType = typeof app  // RPC クライアント用
export default app
```

### Zod Validator **[MUST]**

入力検証は必ず middleware 層 (`@hono/zod-validator` + zod) に集約:

```ts
import { zValidator } from '@hono/zod-validator'
import { z } from 'zod'

app.post('/users', zValidator('json', z.object({
  name: z.string().min(1),
  email: z.string().email(),
})), async (c) => {
  const data = c.req.valid('json')
  // ...
})
```

## 5. ストレージ選択 **[MUST]**

**Bindings 経由で呼ぶ** (REST API 経由は禁止 — ネットワークホップなし・認証オーバーヘッドなし)。

| 用途 | ストレージ |
|---|---|
| セッション / 設定 / 読取多・書込少 | **Workers KV** |
| ファイル / 画像 / 動画 / 大容量 | **R2** |
| SQL / リレーショナル | **D1** |
| per-entity (ユーザー/部屋/セッション) state | **Durable Objects** |
| 非同期 fan-out / バッファリング | **Queues** |
| 多段階・長時間の永続フロー | **Workflows** |
| 外部 PostgreSQL 高速化 | **Hyperdrive** |

## 6. Durable Objects **[MUST]**

- **SQLite ストレージを新規プロジェクトで採用** (旧 key-value storage は使わない)
- **`getByName()` で決定論ルーティング** — 同じ name → 同じ instance。`idFromName()` をランダムに使わない
- **`blockConcurrencyWhile()` は初期化専用** — 中で `fetch` / KV / R2 の外部 I/O を呼ばない (全リクエストが止まる)
- **`alarm()` API で遅延処理・定期処理・TTL** を実装
- **Input / Output Gates は自動** — read-modify-write の競合は心配しなくてよい
- **WebSocket Hibernation** — 長時間接続は `state.acceptWebSocket` を使い、isolate がエビクトされてもハンドラが再開できる形にする
- **`setAlarm` を constructor で呼ばない** — TTL が継続延長されて alarm が発火しない

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
}
```

## 7. Workflows vs Queues **[SHOULD]**

- **Queues** — 単純な非同期処理・バッチ・fan-out
- **Workflows** — 多段階・長時間・人間の承認待ち・複雑なリトライ (`step.do` / `step.sleep` / `step.waitForEvent`)

**Workflows を単発処理に使わない** (Queues で十分)。

## 8. テスト: `@cloudflare/vitest-pool-workers` **[MUST]**

Cloudflare 公式のテストフレームワーク。Vitest のテストを **workerd ランタイムの中** で実行し、Bindings (KV / R2 / D1 / DO) に本物のローカル実装でアクセスできる。

- **`@cloudflare/vitest-pool-workers` を標準採用** (Miniflare 直は非推奨)
- Vitest **4.1 以降** が必要
- `wrangler.jsonc` の設定が自動で読まれるため bindings を二重に書かない
- **Integration テストは `exports.default.fetch(req)`** で Worker 全体を叩く
- **Durable Objects は `runInDurableObject(stub, fn)`** でインスタンス内から直接テスト
- **D1 migrations は `readD1Migrations` で setup 時に一括適用**

```ts
// vitest.config.ts
import { cloudflareTest } from '@cloudflare/vitest-pool-workers'
import { defineConfig } from 'vitest/config'

export default defineConfig({
  plugins: [cloudflareTest({ wrangler: { configPath: './wrangler.jsonc' } })],
})
```

## 9. Observability **[MUST]**

- **`observability.enabled: true`** を本番で必ず有効化 (ダッシュボードでログ検索・集計可能)
- **`wrangler tail`** でリアルタイムログストリーム
- **Tail Workers** で高度なログパイプライン (フィルタ / 変換 / 外部送信)
- **Analytics Engine** で時系列集計データを SQL 集計 (書き込みはノンブロッキング)
- **Logpush** でログを Datadog / Splunk / S3 / R2 に送信 (Enterprise)
- **`console.log` しかせず Workers Logs を使わない書き方は禁止** — 本番調査が手探りになる

## 10. CI/CD と本番デプロイ **[MUST]**

- **`wrangler types && tsc --noEmit`** を CI 第 1 ステップで必ず実行
- **Gradual Rollouts** を使う — 新バージョンを `wrangler versions upload` で上げ、`wrangler versions deploy --percentage 10 → 100` で段階的にルーティング
- **問題発生時は `wrangler rollback <v1-id>`** で前バージョンに戻す
- **環境分離** — 本番 `wrangler deploy` / staging `wrangler deploy --env staging` / dev `wrangler dev`
- **D1 migrations は CI で `wrangler d1 migrations apply DB --remote`** (本番で直接実行しない)

## 11. アンチパターンまとめ

1. `wrangler.toml` を新規で書き始める → `wrangler.jsonc` に
2. Node.js 前提 (`fs.readFileSync` 同期 I/O・`process` 直接参照)
3. Workers のグローバル変数に状態を保存
4. `wrangler secret put` せず `vars` に API key を書く
5. `blockConcurrencyWhile` の中で `fetch` / KV / R2
6. `setAlarm` を constructor で呼ぶ
7. Durable Objects を `idFromName()` で毎回ランダムに生成
8. 全部の状態を 1 つの Durable Object に詰める
9. Workflows を単発処理に使う
10. REST API (`fetch('https://api.cloudflare.com/client/v4/...')`) でバインディング先を呼ぶ
11. Miniflare を直接使ってテストを書く (`vitest-pool-workers` に寄せる)
12. `.env` と `.dev.vars` を両方置く
13. `observability.enabled: false` のまま本番運用
14. `wrangler types` を CI で走らせない
15. `wrangler deploy` 直叩きで Gradual Rollouts を使わない
