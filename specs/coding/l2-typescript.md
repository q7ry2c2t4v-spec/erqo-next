# L2 TypeScript コーディングルール

**適用対象:** `.ts` / `.tsx` / `.mts` / `.cts` 拡張子のファイル全般 (Next.js / Cloudflare Workers / その他)
**前提:** 必ず `specs/06-coding-rules.md` (L1 汎用共通) と合わせて適用する
**機械判定:** `python core/coding_rules.py <file.tsx>`

L3 の Next.js / Cloudflare ルールと**合算して**適用される。TS/TSX であればフレームワークに関係なくこのレイヤの規約が必ず効く。

---

## 1. strict TypeScript 必須 **[MUST]**

- **`tsconfig.json` で `"strict": true`**
- **`noUncheckedIndexedAccess: true`** — 配列アクセスの戻り値に `undefined` を含めて安全にする
- **`noImplicitOverride: true`** — `override` キーワードの付け忘れをエラー化
- **`exactOptionalPropertyTypes: true`** — `?:` と `| undefined` を区別して厳密に
- **`any` の使用は例外的** — 必ず `// eslint-disable-next-line @typescript-eslint/no-explicit-any` などで理由付きコメント
- **TypeScript 最低バージョン 5.1** 以上 (Next.js 15+ の要件)

## 2. パスエイリアス **[MUST]**

相対パス `../../../components/button` は書かない。`tsconfig.json` で `@/*` → `src/*` を定義し、絶対パスで書く。

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": { "@/*": ["src/*"] }
  }
}
```

Next.js / Cloudflare Workers / Vite / その他ビルダーはいずれもこの `paths` を尊重する。

## 3. 環境変数の 1 箇所検証 **[MUST]**

`process.env.XXX` / `import.meta.env.XXX` を**直接あちこちで参照しない**。

- **`src/lib/env.ts`** で 1 度だけパース・検証
- **`zod` などで型チェック付きで宣言**
- 他モジュールは `env.ts` から re-export を import

```ts
// src/lib/env.ts
import { z } from 'zod'

const envSchema = z.object({
  DATABASE_URL: z.string().url(),
  JWT_SECRET: z.string().min(32),
  APP_ENV: z.enum(['development', 'staging', 'production']),
})

export const env = envSchema.parse(process.env)
```

**理由:** 未定義変数・型ミスを起動時に即検出するため。L1 §1.2 (DRY / 一元管理) の TypeScript 版実装。`constants.py` / `paths.py` の Python 側ルールと同じ思想。

## 4. 命名とコメント **[SHOULD]**

- 関数は動詞始まり (`fetchUser`, `buildUrl`)、コンポーネントは PascalCase (`UserCard`)
- hook は `use` 始まり (`useLocalStorage`)
- 定数は `UPPER_SNAKE_CASE`
- コメントは「何を」ではなく「なぜ」を書く (L1 §1.3 の延長)
- 自明な型注釈は省略してよい — `const x: number = 1` → `const x = 1`

## 5. import の整理 **[MUST]**

- **相対 import は同一ディレクトリのみ** (`./foo`)。`../` を 2 段以上は禁止 → エイリアスを使う
- **副作用 import (`import './polyfill'`) は最上部にまとめる**
- **type-only import は `import type` を明示** (バンドラが最適化しやすい)

```ts
import type { User } from '@/types/user'
import { fetchUser } from '@/lib/dal/user'
```

## 6. エラー型付け **[SHOULD]**

- **`try { ... } catch (e) { ... }` の `e` はデフォルトで `unknown`** (TypeScript の推奨デフォルト)
- **型ガードで絞ってから使う**

```ts
try {
  await action()
} catch (e) {
  if (e instanceof Error) logger.error(e.message)
  else logger.error(String(e))
}
```

- カスタムエラーは `class MyError extends Error` で定義し、`name` プロパティを明示

## 7. L3 への引き継ぎ

TypeScript 共通のルールはここまで。**フレームワーク固有ルール** (React hook 規約 / Next.js の Server Components / Cloudflare Workers のバインディング) は L3 ファイルに書かれている:

- **Next.js プロジェクト** — `specs/coding/l3-nextjs.md`
- **Cloudflare Workers プロジェクト** — `specs/coding/l3-cloudflare.md`

編集対象のファイルパスに応じて `python core/coding_rules.py <path>` が自動的に該当する L3 ファイルも列挙する。必ず両方を読んでから実装に入る。
