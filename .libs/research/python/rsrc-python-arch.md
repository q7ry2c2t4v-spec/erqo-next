# RSRC-PYTHON-ARCH — Python 3.12+ 大規模プロジェクトの構成・型・並行

関連: RSRC-PYTHON-QUALITY, RSRC-CLOUDFLARE-ARCH
タグ: python, python312, python313, python314, pyproject, uv, src-layout, packaging, type-hints, pep-695, pep-696, pep-702, pep-705, generics, typed-dict, protocol, self-type, asyncio, task-group, except-star, exception-group, pydantic, dataclass, structural-typing, 大規模プロジェクト, ベストプラクティス, architecture, free-threading, jit, gil

## RSRC-PYTHON-ARCH.概要 — 概要

Python 3.12+ の大規模プロジェクト向けコーディング方法を公式情報ベースで整理したページ。観点は 3 つ: (1) パッケージ構成とツーリング、(2) 型システム、(3) 非同期・エラー処理。Python 3.11 以前の情報は除外。参照日は 2026-04-11。

**前提バージョン:**
- **Python 3.12 以上** (3.13 をメイン、3.14 の新機能に触れる)
- **uv 0.5 以上** (pyproject.toml ベース、PEP 621 準拠)
- **pyright 1.1.380+** または **mypy 1.11+** で strict 型チェック

## RSRC-PYTHON-ARCH.バージョン — バージョン前提と新機能

### Python 3.12 (最低ライン)

- **PEP 695** `type` 文と generic syntax 導入: `def first[T](xs: list[T]) -> T`
- **`typing.override` デコレータ** — サブクラスの override を型チェックで強制
- **`typing.TypeAliasType`** — `type` 文で生成される型エイリアスオブジェクト
- **f-string の任意の式** — `f'{obj.value!r}'` の制限緩和
- **`sys.monitoring`** — 軽量プロファイリング API

### Python 3.13

- **PEP 696** — 型パラメータのデフォルト値: `class Container[T = int]: ...`
- **PEP 702** — `@warnings.deprecated("use X instead")` デコレータ (実行時警告 + 型チェッカー対応)
- **PEP 705** — `typing.ReadOnly` で `TypedDict` のキーを読み取り専用化
- **PEP 703 (experimental)** — Free-Threaded CPython (no GIL)。`python3.13t` バイナリで有効化。単スレッド性能は低下、マルチスレッド並列で効果
- **JIT コンパイラ (experimental)** — `--enable-experimental-jit` ビルド + `PYTHON_JIT=1` 環境変数
- **REPL 改善** (multi-line 編集、colored output)

### Python 3.14

- Free-threading の experimental 卒業 (PEP 779)
- さらなる型システム拡張 (`TypeVarTuple` のデフォルト値など)
- **基本方針: 本番プロジェクトは 3.13 を target、ライブラリは 3.12 以上を宣言する**

## RSRC-PYTHON-ARCH.パッケージ構成 — パッケージ構成とツーリング

### `src-layout` 必須

**ライブラリ・アプリ問わず `src/` 配下に置く** のが現代標準:

```
myproject/
├── pyproject.toml
├── .python-version        ← uv が生成
├── .venv/                 ← uv sync で自動生成
├── uv.lock                ← 必ず commit
├── src/
│   └── myproject/
│       ├── __init__.py
│       ├── core.py
│       └── lib/
├── tests/
│   └── test_core.py
└── README.md
```

**理由:** カレントディレクトリからの偶発 import を防ぎ、installed 状態に近い挙動でテスト・開発ができる。

### `pyproject.toml` (PEP 621 + uv)

```toml
[project]
name = "myproject"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "httpx>=0.27",
    "pydantic>=2.8",
]

[project.optional-dependencies]
test = ["pytest>=8", "pytest-asyncio>=0.24"]

[build-system]
requires = ["uv_build>=0.11.6,<0.12"]
build-backend = "uv_build"

[tool.uv]
dev-dependencies = ["ruff>=0.7", "pyright>=1.1.380"]

[tool.uv.sources]
# モノレポの相対パス参照など
```

### uv コマンド (大規模で覚えるべきもの)

| コマンド | 役割 |
|---|---|
| `uv init` / `uv init --lib` | プロジェクト初期化 (app or library テンプレ) |
| `uv add <pkg>` | 依存を `pyproject.toml` に追加 + lock + 同期 |
| `uv add --dev <pkg>` | dev 依存として追加 |
| `uv add --group test <pkg>` | 任意の dependency group に追加 |
| `uv sync` | `uv.lock` に従って `.venv/` を同期 |
| `uv sync --frozen` | lock を更新せず同期 (CI で使う) |
| `uv run <cmd>` | 同期を確認した上でコマンド実行 |
| `uv lock --upgrade-package <pkg>` | 指定パッケージだけ upgrade |
| `uv build` | sdist + wheel を `dist/` に生成 |
| `uv python install 3.13` | Python 自体のインストール |
| `uv tool install ruff` | global な開発ツール導入 |

`.venv/` は pyproject.toml の隣に置かれる。`uv run` が毎回 lock 整合性をチェックするため、`source .venv/bin/activate` を省略しても良い。

### Workspaces (monorepo)

```toml
[tool.uv.workspace]
members = ["packages/*"]
```

packages/ 配下の各 pyproject.toml が独立パッケージとして扱われ、同一 venv を共有する。

### 本元リポジトリとの関係

本元 erqo-next の `core/` は **Python 標準ライブラリのみ** を原則とする (giget 配布でプロジェクトに届く前提)。pyproject.toml や uv は使わず、直接 `python core/...` で呼ぶ。外部ライブラリが必要な機能は `core/<feature>_node/` のような隔離サブディレクトリに置く (前例: `core/clone_node/`)。

## RSRC-PYTHON-ARCH.型システム — 型システム

### PEP 695 `type` 文

```python
# エイリアス
type Vector = list[float]
type UserId = int

# Generic 関数 (TypeVar 宣言不要)
def first[T](xs: list[T]) -> T:
    return xs[0]

# Generic クラス
class Container[T]:
    def __init__(self, item: T) -> None:
        self.item = item
```

**利点:** `TypeVar("T")` の事前宣言が不要。スコープが構文で閉じる。

### PEP 696 型パラメータのデフォルト

```python
class APIClient[T = dict[str, object]]:
    def fetch(self) -> T: ...

client: APIClient = APIClient()        # T は dict[str, object]
typed: APIClient[MyModel] = APIClient()  # T は MyModel
```

### Protocol (構造的サブタイピング)

継承なしで「こういう shape を持つもの」を型にする:

```python
from typing import Protocol

class SupportsClose(Protocol):
    def close(self) -> None: ...

def cleanup(r: SupportsClose) -> None:
    r.close()
```

**使いどき:** 外部ライブラリの型に依存せず、必要な機能だけを契約として書きたいとき。

### `TypedDict` と `ReadOnly` (PEP 705)

```python
from typing import TypedDict, ReadOnly

class UserDTO(TypedDict):
    id: ReadOnly[int]      # 書き換え不可
    name: str              # 通常キー
    age: int
```

dict だが型が効く。DAL から API に渡す DTO などに便利。

### `Self` 型 (3.11+)

```python
class Builder:
    def chain(self) -> "Self":
        return self
```

サブクラスでも自動的に正しい Self 型になる。Fluent API で必須。

### `@override` デコレータ (3.12+)

```python
from typing import override

class Base:
    def run(self) -> None: ...

class Child(Base):
    @override
    def run(self) -> None: ...   # Base.run が消えたらエラー
```

リファクタ時の安全網。

### `@deprecated` デコレータ (3.13+)

```python
from warnings import deprecated

@deprecated("Use new_api() instead")
def old_api() -> None: ...
```

型チェッカーと実行時警告の両方で検出される。

## RSRC-PYTHON-ARCH.非同期エラー処理 — 非同期・エラー処理

### `asyncio.TaskGroup` (3.11+ / 3.12 で安定)

複数の並行タスクを**キャンセル伝播込み**でまとめる新 API:

```python
import asyncio

async def fetch_all() -> tuple[str, str]:
    async with asyncio.TaskGroup() as tg:
        a = tg.create_task(fetch("https://a"))
        b = tg.create_task(fetch("https://b"))
    return a.result(), b.result()
```

**従来の `asyncio.gather` よりこちらを優先**:
- 子タスクで例外が起きると他の子も cancel される
- `async with` を抜けた時点で全タスク完了が保証される
- 例外は `ExceptionGroup` にまとめられる

### `ExceptionGroup` と `except*` (PEP 654)

複数の例外を同時に扱える:

```python
try:
    async with asyncio.TaskGroup() as tg:
        tg.create_task(task_a())
        tg.create_task(task_b())
except* ValueError as eg:
    # ValueError だけを抜き出してハンドル
    log.warning("value errors: %s", eg.exceptions)
except* ConnectionError as eg:
    log.error("connection errors: %s", eg.exceptions)
```

### `asyncio.timeout` (3.11+)

```python
async with asyncio.timeout(10):
    await long_op()
```

`asyncio.wait_for` より柔軟。ネストして累積制限も可能。

### データクラス vs pydantic v2

| 用途 | 選択 |
|---|---|
| 内部データ構造 (検証不要) | `@dataclass(slots=True)` |
| 外部境界 (API 入力・環境変数・設定) | `pydantic.BaseModel` v2 |
| 型付き辞書 (JSON そのまま扱う) | `TypedDict` |

pydantic v2 はコアが Rust 実装で v1 比 5〜50 倍高速。**境界では必ず検証する** (specs/06-coding-rules.md §1.5 と整合)。

```python
from pydantic import BaseModel, Field

class UserInput(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(ge=0, le=150)

# 使い方
user = UserInput.model_validate(raw_dict)  # ValidationError を投げうる
```

## RSRC-PYTHON-ARCH.推奨パターン — 推奨パターン

1. **`requires-python = ">=3.12"`** を宣言し、新型構文を遠慮なく使う
2. **`src/` layout + `uv` で pyproject.toml を一元管理** (`uv.lock` は必ず commit)
3. **Generic は `class Container[T]:` の PEP 695 構文で書き、`TypeVar` の事前宣言をしない**
4. **非同期並列は `asyncio.gather` ではなく `asyncio.TaskGroup`**
5. **外部境界 (API / env / CLI 引数) は pydantic v2 で validate、内部は dataclass**
6. **ExceptionGroup を `except*` で品目別にハンドル**
7. **override は `@typing.override` で宣言、非推奨化は `@warnings.deprecated` で宣言**
8. **`TypedDict` に `ReadOnly[...]` を付けて不変フィールドを型で固める**
9. **`.venv/` は `.gitignore`、`uv.lock` は commit**
10. **CI では `uv sync --frozen` + `uv run <cmd>`**

## RSRC-PYTHON-ARCH.アンチパターン — アンチパターン

1. **`setup.py` や `setup.cfg` を残す** — PEP 621 pyproject.toml に一本化する
2. **flat layout (`myproject/` 直下にモジュール)** — src layout に移行
3. **`TypeVar("T")` を事前宣言** — PEP 695 の generic 構文に書き換え
4. **`asyncio.gather(..., return_exceptions=True)`** — 例外が握りつぶされ、デバッグが困難。`TaskGroup` を使う
5. **`try: except Exception:`** — 広すぎるキャッチ。型別の `except*` か個別 except に
6. **pydantic を内部データ構造にも使う** — オーバースペック。dataclass で十分
7. **`from typing import List, Dict, Tuple`** — 組み込み `list`, `dict`, `tuple` を直接使う
8. **モジュール top-level で副作用のあるコード** — import 時に DB 接続などしない。`main()` に閉じる
9. **`Any` を戻り値型に書く** — 使うなら `object` か型をちゃんと書く
10. **`print()` でデバッグログ** — `logging` module (or structlog) に置き換える

## RSRC-PYTHON-ARCH.出典 — 出典

参照日: 2026-04-11

- [What's New In Python 3.12 | docs.python.org](https://docs.python.org/3/whatsnew/3.12.html)
- [What's New In Python 3.13 | docs.python.org](https://docs.python.org/3/whatsnew/3.13.html)
- [What's New In Python 3.14 | docs.python.org](https://docs.python.org/3/whatsnew/3.14.html)
- [PEP 695 – Type Parameter Syntax | peps.python.org](https://peps.python.org/pep-0695/)
- [PEP 696 – Type Defaults for Type Parameters | peps.python.org](https://peps.python.org/pep-0696/)
- [PEP 702 – Deprecated Decorator | peps.python.org](https://peps.python.org/pep-0702/)
- [PEP 703 – Making the GIL Optional | peps.python.org](https://peps.python.org/pep-0703/)
- [PEP 705 – TypedDict ReadOnly | peps.python.org](https://peps.python.org/pep-0705/)
- [typing — Support for type hints | docs.python.org](https://docs.python.org/3/library/typing.html)
- [Python support for free threading | docs.python.org](https://docs.python.org/3/howto/free-threading-python.html)
- [Writing your pyproject.toml | Python Packaging User Guide](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [src layout vs flat layout | Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [uv: Working on projects | docs.astral.sh](https://docs.astral.sh/uv/guides/projects/)
- [uv: Structure and files | docs.astral.sh](https://docs.astral.sh/uv/concepts/projects/layout/)
- [uv: Workspaces | docs.astral.sh](https://docs.astral.sh/uv/concepts/projects/workspaces/)
- [uv: The uv build backend | docs.astral.sh](https://docs.astral.sh/uv/concepts/build-backend/)
- [pydantic v2 docs | docs.pydantic.dev](https://docs.pydantic.dev/latest/)
