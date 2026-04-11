# RSRC-CLOUDFLARE-QUALITY — Cloudflare Workers 大規模プロジェクトの開発・テスト・本番化

関連: RSRC-CLOUDFLARE-ARCH, RSRC-NEXTJS-QUALITY, RSRC-PYTHON-QUALITY
タグ: cloudflare, cloudflare-workers, wrangler-cli, wrangler-dev, wrangler-deploy, wrangler-tail, wrangler-types, wrangler-secret, miniflare, vitest-pool-workers, cloudflare-test, unit-test, integration-test, secrets, dotenv, dev-vars, observability, workers-logs, tail-workers, analytics-engine, logpush, traces, ci-cd, 大規模プロジェクト, ベストプラクティス, quality, testing, deployment

## RSRC-CLOUDFLARE-QUALITY.概要 — 概要

Cloudflare Workers プロジェクトで品質を担保するための開発・テスト・Secrets 管理・Observability・CI/CD を公式情報ベースで整理したページ。観点は 4 つ: (1) テスト (`@cloudflare/vitest-pool-workers`)、(2) Wrangler CLI と Secrets 管理、(3) Observability、(4) CI/CD と本番化。参照日は 2026-04-11。

前提: RSRC-CLOUDFLARE-ARCH (ランタイム・構成・Bindings) と併読。

## RSRC-CLOUDFLARE-QUALITY.テスト — vitest-pool-workers

### 原則

Cloudflare 公式のテストソリューションは **`@cloudflare/vitest-pool-workers`**。Vitest のテストを **workerd ランタイムの中** で実行するため、Bindings (KV / R2 / D1 / DO) に本物のローカル実装 (Miniflare ベース) でアクセスできる。

- **Unit テスト** — 関数・クラスを直接 import して叩く
- **Integration テスト** — `exports.default.fetch(req)` で Worker 全体にリクエストを流す
- **要件:** Vitest **4.1 以降** + `@cloudflare/vitest-pool-workers` 最新

### セットアップ

```bash
npm install -D vitest @cloudflare/vitest-pool-workers
```

```ts
// vitest.config.ts
import { cloudflareTest } from '@cloudflare/vitest-pool-workers'
import { defineConfig } from 'vitest/config'

export default defineConfig({
  plugins: [
    cloudflareTest({
      wrangler: { configPath: './wrangler.jsonc' },
      miniflare: {
        // wrangler の設定に追加・上書きしたい場合のみ
        compatibilityFlags: ['nodejs_compat'],
        d1Databases: ['DB'],
        kvNamespaces: ['SESSION_KV'],
      }
    })
  ],
})
```

`wrangler.jsonc` の設定が **自動で読まれる** ので、bindings を二重に書く必要はない。

### Unit テストの例

```ts
// src/lib/hash.ts
export function hash(input: string): string {
  return Array.from(input).reduce((a, c) => a + c.charCodeAt(0), 0).toString(16)
}
```

```ts
// src/lib/hash.test.ts
import { describe, it, expect } from 'vitest'
import { hash } from './hash'

describe('hash', () => {
  it.each([
    ['', '0'],
    ['a', '61'],
    ['ab', 'c3'],
  ])('hash(%s) === %s', (input, expected) => {
    expect(hash(input)).toBe(expected)
  })
})
```

### Integration テストの例

```ts
// tests/integration/users.test.ts
import { env, createExecutionContext, waitOnExecutionContext } from 'cloudflare:test'
import { describe, it, expect } from 'vitest'
import worker from '../../src/index'

describe('GET /users/:id', () => {
  it('returns user from D1', async () => {
    await env.DB.prepare('INSERT INTO users (id, name) VALUES (?, ?)').bind(1, 'Alice').run()

    const req = new Request('http://example.com/users/1')
    const ctx = createExecutionContext()
    const res = await worker.fetch(req, env, ctx)
    await waitOnExecutionContext(ctx)

    expect(res.status).toBe(200)
    expect(await res.json()).toEqual({ id: 1, name: 'Alice' })
  })
})
```

`cloudflare:test` モジュールから `env` / `createExecutionContext` / `waitOnExecutionContext` / `SELF` / `runInDurableObject` などのヘルパが入手できる。

### Durable Objects テスト

```ts
import { env, runInDurableObject } from 'cloudflare:test'

it('posts messages', async () => {
  const id = env.ROOM.idFromName('test-room')
  const stub = env.ROOM.get(id)

  await runInDurableObject(stub, async (instance) => {
    // instance の中に入って直接メソッドを叩ける
    await instance.postMessage('hello')
    const messages = await instance.getMessages()
    expect(messages).toHaveLength(1)
  })
})
```

### Migrations テスト (D1)

`readD1Migrations` ヘルパで `migrations/` の SQL を一括適用できる:

```ts
import { readD1Migrations } from '@cloudflare/vitest-pool-workers/config'

export default defineConfig({
  plugins: [
    cloudflareTest({
      miniflare: {
        d1Databases: ['DB'],
      }
    })
  ],
  test: {
    setupFiles: ['./tests/setup.ts'],
  }
})
```

## RSRC-CLOUDFLARE-QUALITY.wrangler — Wrangler CLI

### 主要コマンド

| コマンド | 役割 |
|---|---|
| `wrangler dev` | ローカル開発サーバー (Miniflare 上で) |
| `wrangler dev --remote` | Cloudflare のエッジで実行 (本物のバインディング利用) |
| `wrangler deploy` | 本番環境へデプロイ |
| `wrangler deploy --env staging` | 特定環境へデプロイ |
| `wrangler versions upload` | 新バージョンをアップロード (即時ルーティング切替なし) |
| `wrangler versions deploy` | アップロード済みバージョンに段階的ルーティング (gradual rollout) |
| `wrangler rollback` | 1 つ前のバージョンに戻す |
| `wrangler tail` | 本番の リアルタイムログストリーム |
| `wrangler types` | `env` の型定義を自動生成 (`worker-configuration.d.ts`) |
| `wrangler secret put KEY` | 秘密値を対話式で設定 |
| `wrangler secret bulk secrets.json` | 複数秘密を一括設定 |
| `wrangler secret list` | 登録済み秘密名の一覧 |
| `wrangler d1 migrations apply <DB>` | D1 マイグレーション適用 |
| `wrangler kv namespace create` | KV namespace 作成 |
| `wrangler r2 bucket create` | R2 bucket 作成 |
| `wrangler queues create <NAME>` | Queue 作成 |

### `package.json` scripts

```json
{
  "scripts": {
    "dev": "wrangler dev",
    "deploy": "wrangler deploy",
    "deploy:staging": "wrangler deploy --env staging",
    "tail": "wrangler tail",
    "types": "wrangler types",
    "test": "vitest",
    "test:ci": "vitest run",
    "typecheck": "tsc --noEmit",
    "lint": "eslint",
    "db:migrate": "wrangler d1 migrations apply DB --remote"
  }
}
```

## RSRC-CLOUDFLARE-QUALITY.secrets — Secrets と環境変数の管理

### 分類

| 種類 | 用途 | 書き込み先 | 例 |
|---|---|---|---|
| **`vars`** | 非秘密の設定値 | `wrangler.jsonc` の `"vars": {}` | `APP_ENV`, `API_BASE_URL` |
| **`secrets`** | API キー・トークン | `wrangler secret put` で管理コンソール | `STRIPE_KEY`, `JWT_SECRET` |
| **`.dev.vars`** | ローカル開発用 | リポジトリ外 (`.gitignore` 必須) | テスト用キー |

### `wrangler.jsonc` での宣言

```jsonc
{
  "vars": {
    "APP_ENV": "production",
    "API_BASE_URL": "https://api.example.com"
  },
  "secrets": {
    "required": ["STRIPE_API_KEY", "OPENAI_API_KEY", "JWT_SECRET"]
  }
}
```

`secrets.required` を宣言すると:
- 起動時に欠落している場合に **警告**
- `.dev.vars` / `.env` からは **リストされたキーだけ** をロード (誤って他の値が混入しない)

### ローカル開発用 `.dev.vars`

```bash
# .dev.vars (gitignore)
STRIPE_API_KEY=sk_test_xxx
OPENAI_API_KEY=sk-xxx
JWT_SECRET=dev-secret-32-chars-long
```

`.env` でも OK だが **両方同時には使わない** — `.dev.vars` があると `.env` は無視される。

### 本番への秘密投入

```bash
wrangler secret put STRIPE_API_KEY
# 対話的に値を入力

# 一括 (CI 向け)
wrangler secret bulk secrets.json
# secrets.json: { "STRIPE_API_KEY": "sk_live_xxx", "JWT_SECRET": "..." }
```

**注意:** `wrangler secret put` は毎回 **新バージョンを作ってデプロイ** する。`wrangler versions secret put` は次回 `wrangler versions deploy` まで反映されない。

## RSRC-CLOUDFLARE-QUALITY.observability — Observability

### Workers Logs (自動収集)

`wrangler.jsonc` で `observability.enabled: true` にすると、**全ログが Cloudflare ダッシュボードで検索・集計可能** になる:

```jsonc
{
  "observability": {
    "enabled": true,
    "head_sampling_rate": 1    // 1 = 100%、0.1 = 10% サンプル
  }
}
```

含まれるもの:
- Invocation logs (リクエスト・レスポンスメタデータ)
- `console.log` などユーザーログ
- 例外 / stack trace

### Real-time logs (`wrangler tail`)

```bash
wrangler tail                          # 全ログ
wrangler tail --format json            # JSON 出力
wrangler tail --status error           # エラーのみ
wrangler tail --sampling-rate 0.1      # 10% サンプル
```

### Tail Workers (高度なパイプライン)

通常の Workers とは別に **"Tail Worker"** を登録すると、他 Worker のログ・テレメトリデータを受けて任意のフィルタ・変換・外部送信できる:

```jsonc
// 監視対象 Worker
{
  "tail_consumers": [{ "service": "my-tail-worker" }]
}
```

```ts
// src/tail-worker.ts
export default {
  async tail(events: TraceItem[], env: Env, ctx: ExecutionContext) {
    for (const event of events) {
      if (event.outcome === 'exception') {
        await env.ERROR_QUEUE.send(event)
      }
    }
  }
}
```

**課金:** Workers Paid / Enterprise プランで利用可。CPU 時間で課金。

### Analytics Engine (時系列集計)

高カーディナリティな時系列データを SQL で集計:

```ts
app.get('/api/*', async (c) => {
  c.env.ANALYTICS.writeDataPoint({
    blobs: [c.req.path, c.req.method],
    doubles: [Date.now()],
    indexes: [c.req.header('cf-connecting-ip') ?? '']
  })
  return handleRequest(c)
})
```

- **書き込みはノンブロッキング** — リクエスト応答のレイテンシに影響しない
- **SQL で後から集計** — `/analytics_engine/sql` API エンドポイント経由

### Logpush (外部送信)

Workers ログを Datadog / Splunk / S3 / R2 に定期送信。エンタープライズ向け。

### Traces (OpenTelemetry 風分散トレース)

Workers Observability Dashboard で request 単位の trace が見られる。2026 年 3 月以降、全プランで課金対象。

## RSRC-CLOUDFLARE-QUALITY.ci-cd — CI/CD と本番化

### GitHub Actions の典型例

```yaml
name: deploy
on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: pnpm/action-setup@v4
        with: { version: 9 }
      - uses: actions/setup-node@v4
        with: { node-version: 22, cache: pnpm }
      - run: pnpm install --frozen-lockfile
      - run: pnpm wrangler types
      - run: pnpm typecheck
      - run: pnpm lint
      - run: pnpm test:ci

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: cloudflare/wrangler-action@v3
        with:
          apiToken: ${{ secrets.CLOUDFLARE_API_TOKEN }}
          command: deploy
```

### Gradual Rollouts (段階的リリース)

```bash
wrangler versions upload              # v2 をアップロード (ルーティングされない)
wrangler versions deploy --percentage 10  # 10% のトラフィックを v2 に
# 監視 + 問題なければ
wrangler versions deploy --percentage 100
# 問題あれば
wrangler rollback <v1-id>
```

### 環境分離

- **本番** — `wrangler deploy`
- **staging** — `wrangler deploy --env staging` (`wrangler.jsonc` の `env.staging` で別名デプロイ)
- **dev (ローカル)** — `wrangler dev`
- **preview** — PR ごとに `wrangler versions upload` でプレビュー URL 発行

### `wrangler types` を CI の最初に走らせる

Bindings の型を最新化する (PR が bindings を追加していた場合に型エラーを捕まえる):

```bash
wrangler types && tsc --noEmit
```

## RSRC-CLOUDFLARE-QUALITY.推奨パターン — 推奨パターン

1. **`@cloudflare/vitest-pool-workers` を標準テストフレームワークに**。直 Miniflare は特殊ケースだけ
2. **`wrangler.jsonc` 1 箇所に bindings を書き、`cloudflareTest` がそれを読む構造**
3. **Integration テストで `exports.default.fetch` を叩き、本物の Request/Response を検証**
4. **Durable Objects は `runInDurableObject` ヘルパでインスタンス内から直接テスト**
5. **D1 migrations は `readD1Migrations` で setup 時に一括適用**
6. **Secrets は `wrangler.jsonc` で `secrets.required` を宣言し、`.dev.vars` + `wrangler secret put` で投入**
7. **ローカルは `.dev.vars` を `.gitignore` して管理、**両方同時に `.env` と `.dev.vars` を置かない
8. **`observability.enabled: true` を本番で有効化**
9. **例外監視・集計は Tail Worker + Analytics Engine or Logpush**
10. **デプロイは Gradual Rollout (`wrangler versions deploy --percentage`) で段階的に**
11. **CI の第 1 ステップは `wrangler types && tsc --noEmit` で型を担保**
12. **`pnpm wrangler dev` をローカル開発で使い、実機エッジは `--remote` を明示**

## RSRC-CLOUDFLARE-QUALITY.アンチパターン — アンチパターン

1. **Miniflare を直接インストールしてテストする** — `vitest-pool-workers` に寄せる (公式推奨)
2. **`wrangler secret put` を手動で叩いて本番を直接デプロイ** — CI 経由 or `wrangler versions secret put` で履歴を残す
3. **`.env` と `.dev.vars` 両方に同じ値を書く** — `.dev.vars` があれば `.env` は無視される、混乱の元
4. **`console.log` しかせず、Workers Logs や Tail Worker を使わない** — 本番調査が困難
5. **`observability.enabled: false` のまま本番運用** — インシデント調査が手探りになる
6. **型生成 (`wrangler types`) を CI で走らせない** — bindings 追加時の型エラーを見逃す
7. **`wrangler deploy` を直接叩くデプロイフロー** — Gradual Rollout を使わないと本番障害時のロールバックが遅い
8. **D1 マイグレーションを本番で直に実行** — テストが migrations を通してないため、本番で初めて壊れることがある
9. **Durable Objects のテストで `fetch` 経由でしか叩かない** — `runInDurableObject` でインスタンス状態を直接検証する方が早い
10. **`wrangler.toml` と `wrangler.jsonc` を両方置く** — どちらか 1 つに (`wrangler.jsonc` 推奨)

## RSRC-CLOUDFLARE-QUALITY.出典 — 出典

参照日: 2026-04-11

- [Workers: Testing | developers.cloudflare.com](https://developers.cloudflare.com/workers/testing/)
- [Workers: Vitest integration | developers.cloudflare.com](https://developers.cloudflare.com/workers/testing/vitest-integration/)
- [Workers: Vitest configuration | developers.cloudflare.com](https://developers.cloudflare.com/workers/testing/vitest-integration/configuration/)
- [Workers: Write your first test | developers.cloudflare.com](https://developers.cloudflare.com/workers/testing/vitest-integration/write-your-first-test/)
- [Workers: Test APIs | developers.cloudflare.com](https://developers.cloudflare.com/workers/testing/vitest-integration/test-apis/)
- [Workers: Recipes and examples | developers.cloudflare.com](https://developers.cloudflare.com/workers/testing/vitest-integration/recipes/)
- [Wrangler commands | developers.cloudflare.com](https://developers.cloudflare.com/workers/wrangler/commands/)
- [Wrangler environments | developers.cloudflare.com](https://developers.cloudflare.com/workers/wrangler/environments/)
- [Workers: Secrets | developers.cloudflare.com](https://developers.cloudflare.com/workers/configuration/secrets/)
- [Workers: Environment variables | developers.cloudflare.com](https://developers.cloudflare.com/workers/configuration/environment-variables/)
- [Workers: Environment variables and secrets (development) | developers.cloudflare.com](https://developers.cloudflare.com/workers/development-testing/environment-variables/)
- [Workers: Observability | developers.cloudflare.com](https://developers.cloudflare.com/workers/observability/)
- [Workers Logs | developers.cloudflare.com](https://developers.cloudflare.com/workers/observability/logs/workers-logs/)
- [Tail Workers | developers.cloudflare.com](https://developers.cloudflare.com/workers/observability/logs/tail-workers/)
- [Real-time logs | developers.cloudflare.com](https://developers.cloudflare.com/workers/observability/logs/real-time-logs/)
- [Metrics and analytics | developers.cloudflare.com](https://developers.cloudflare.com/workers/observability/metrics-and-analytics/)
- [Workers Observability launch | blog.cloudflare.com](https://blog.cloudflare.com/introducing-workers-observability-logs-metrics-and-queries-all-in-one-place/)
- [Gradual Deployments / Versions | developers.cloudflare.com](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/)
