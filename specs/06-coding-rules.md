# コーディング規約 (ハブ)

エル子がコードを書くときの共通ルール。**3 層モデル**に基づき、対象ファイルに応じて必要な層を合併して適用する。

このファイルは **ハブ (index)** として機能する。L1 汎用共通ルールだけを内包し、L2 / L3 は `specs/coding/` 配下の層別ファイルに分割してある。**実装前にファイルパスから機械判定** して必要な層別ファイルを Read する。

## 0. 概要と適用マトリックス

### 3 層モデル

| 層 | 名前 | 配置 | 内容 |
|---|---|---|---|
| L1 | 汎用共通 | **本ファイル (下記)** | すべてのコードに適用する基礎原則 |
| L2 | 言語カテゴリ | `specs/coding/l2-*.md` | 言語ごとの基礎 (Python / TypeScript) |
| L3 | フレームワーク専用 | `specs/coding/l3-*.md` | 特定フレームワークの規約 (Next.js / Cloudflare) |

### 適用マトリックス (機械判定)

| ファイルパスパターン | 適用層 |
|---|---|
| `**/*.py` | L1 + `l2-python.md` |
| `**/*.ts`, `**/*.tsx` (汎用) | L1 + `l2-typescript.md` |
| Next.js プロジェクト (`next.config.ts|mjs|js` 有) の `.ts` / `.tsx` | L1 + `l2-typescript.md` + `l3-nextjs.md` |
| Cloudflare プロジェクト (`wrangler.jsonc|json|toml` 有、または `workers/` 配下) の `.ts` / `.tsx` | L1 + `l2-typescript.md` + `l3-cloudflare.md` |
| それ以外 | L1 のみ |

### 機械判定の使い方 (必須)

**エル子はコード編集前に必ず** 以下のスクリプトを実行し、返ってきたルールファイルを全て Read してから実装する:

```bash
python core/coding_rules.py <編集対象のファイルパス>
```

**出力例:**

```
specs/06-coding-rules.md                 (L1 汎用 — 常時適用)
specs/coding/l2-typescript.md            (L2 TypeScript)
specs/coding/l3-nextjs.md                (L3 Next.js)
```

この判定は `core/coding_rules.py` の `get_applicable_rules()` 関数で機械的に行われる。**AI の自己判断は一切挟まない** (`specs/08-responsibility.md` の責務分離原則)。

### 語気の凡例

- **MUST** — 違反はバグ扱い。レビューで必ず弾く
- **SHOULD** — 推奨。妥当な理由があれば例外を許容
- **MAY** — 任意。プロジェクトの好みで選ぶ

---

## 1. 汎用共通ルール (L1)

すべてのコードに適用する基礎原則。言語・フレームワークを問わない。

### 1.1 ハードコーディング禁止 **[MUST]**

パスリテラル、ファイル名、固定文字列、マジックナンバーをコード中に直接書かない。

**理由:** 同じ値が複数箇所に散ると、変更時に全箇所の追跡漏れが起きる。定数化すれば意図を名前で示せる。

### 1.2 DRY / 定数の一元管理 **[MUST]**

同じ値・同じロジックが 2 箇所以上で参照されるなら必ず 1 箇所に集約する。

- **値:** 言語に応じた定数の配置先 (L2 参照) に集約
- **ロジック:** ヘルパ関数・共通モジュールに切り出す

### 1.3 命名規則 — 役割を示す **[MUST]**

定数・関数・変数の名前は**意図**を示す。値そのものを名前に入れない。

- NG: `DOT_CLAUDE = ".claude"` / `BG_BLUE = "#3b82f6"`
- OK: `CLAUDE_DIR_NAME = ".claude"` / `PRIMARY_BRAND_COLOR = "#3b82f6"`

### 1.4 例外: リテラルを書いてよいケース

以下に限りリテラルを直接書いてよい:

- **エラーメッセージ・ログ文言のフォーマット文字列** — ただし同じ文言が複数箇所で使われるなら定数化する
- **モジュール内で 1 度しか出現しない内部値** — 他モジュールから参照されないローカル値に限る
- **テストコードの期待値** — テストは意図を明示するためリテラルを使ってよい

### 1.5 責務境界でだけバリデーション **[MUST]**

- **外部からの入力** (ユーザー入力・外部 API・環境変数) は境界で検証する
- **内部呼び出し** (内部モジュール間) は検証しない。呼び出し元の型契約を信頼する
- **曖昧判断禁止** (`specs/08-responsibility.md`): AI が「今回は〜だから省略する」とその場判断するのはルール違反

---

## 2. 層別ファイル (L2 / L3) へのポインタ

以下は `python core/coding_rules.py` で機械的に列挙される。ここでは参考までに一覧を示す:

| 層別ファイル | 内容 |
|---|---|
| `specs/coding/l2-python.md` | Python 共通 (`core/paths.py`/`constants.py` 配置、uv、Ruff、pyright、pytest、pre-commit、structlog) |
| `specs/coding/l2-typescript.md` | TypeScript 共通 (strict、パスエイリアス、`env.ts` 1 箇所検証、import 整理) |
| `specs/coding/l3-nextjs.md` | Next.js 15+ (Tailwind `@theme`、Server/Client 境界、データ取得、ESLint Flat Config、PPR、DAL、DAL) |
| `specs/coding/l3-cloudflare.md` | Cloudflare Workers (wrangler.jsonc、Hono、Durable Objects SQLite、`vitest-pool-workers`、Gradual Rollouts、Observability) |

---

## 3. 違反時の対応

新規コード・既存コード編集時に L1〜L3 の該当ルールに反する箇所を見つけたら、**その場で修正** する。全面リファクタの義務化はしない (該当箇所を編集するときに合わせる)。

迷ったときは `specs/00-identity.md` の承認フロー (対話 → 承認 → 実装) を踏み、AI が自己判断で仕様を曲げない。

---

## 4. 関連リサーチへのポインタ

本規約の根拠になっているリサーチページ:

- **`RSRC-NEXTJS-ARCH`** / **`RSRC-NEXTJS-QUALITY`** (`.libs/research/nextjs/`) — `l3-nextjs.md` の根拠
- **`RSRC-PYTHON-ARCH`** / **`RSRC-PYTHON-QUALITY`** (`.libs/research/python/`) — `l2-python.md` の根拠
- **`RSRC-CLOUDFLARE-ARCH`** / **`RSRC-CLOUDFLARE-QUALITY`** (`.libs/research/cloudflare/`) — `l3-cloudflare.md` の根拠
- **`RSRC-WEBCLONE-RULES`** (`.libs/research/webclone/`) — Tailwind v4 `@theme` トークン運用の詳細 (`l3-nextjs.md` §1 の根拠)
- **`specs/08-responsibility.md`** — 責務分離・AI 自己判断の禁止 (L1.5 + 機械判定の根拠)

新しいルールを追加するときは、**まず `/rsrc` で公式情報を裏取り** → **RSRC ページを作成** → **該当する層別ファイル (`l2-*` / `l3-*`) に追加** → **このハブの §0 適用マトリックスを更新 (新カテゴリの場合のみ)** → **`core/coding_rules.py` の判定ロジック更新 (新カテゴリの場合のみ)** の順で行う。
