# RSRC-PYTHON-QUALITY — Python 3.12+ 大規模プロジェクトの品質保証・テスト

関連: RSRC-PYTHON-ARCH, RSRC-CLOUDFLARE-QUALITY
タグ: python, python312, python313, ruff, ruff-lint, ruff-format, pyright, mypy, strict-typing, pytest, pytest-asyncio, pytest-fixtures, pytest-parametrize, pre-commit, coverage, coverage-py, logging, structlog, 大規模プロジェクト, ベストプラクティス, quality, lint, format, testing

## RSRC-PYTHON-QUALITY.概要 — 概要

Python 3.12+ の大規模プロジェクトで品質を担保するためのツール・規約を公式情報ベースで整理したページ。観点は 3 つ: (1) Lint / Format (Ruff)、(2) 型チェック (pyright / mypy)、(3) テスト (pytest + pytest-asyncio + coverage)。Python 3.11 以前の情報は除外。参照日は 2026-04-11。

前提: RSRC-PYTHON-ARCH (パッケージ構成・型・非同期) と併読。

## RSRC-PYTHON-QUALITY.ruff — Ruff (Lint + Format)

### 原則

**Black + flake8 + isort + pyupgrade + pylint の大半 + autoflake を 1 ツールに統合**。Rust 実装で 10〜100 倍速。2026 年時点では **Python 大規模の標準**。

### `pyproject.toml` 設定 (推奨ベース)

```toml
[tool.ruff]
target-version = "py312"
line-length = 100
src = ["src", "tests"]
extend-exclude = [".venv", "build", "dist"]

[tool.ruff.lint]
select = [
    "E", "W",   # pycodestyle
    "F",        # pyflakes
    "I",        # isort
    "N",        # pep8-naming
    "UP",       # pyupgrade (古い構文を自動近代化)
    "B",        # flake8-bugbear (バグになりがちな書き方)
    "A",        # builtins shadowing 禁止
    "C4",       # comprehensions 最適化
    "DTZ",      # datetime にタイムゾーンを強制
    "T20",      # print 禁止
    "PT",       # pytest 慣習
    "SIM",      # simplify
    "TCH",      # type-checking imports 整理
    "RUF",      # Ruff 独自
    "ANN",      # 型注釈必須 (引数・戻り値)
    "S",        # Bandit セキュリティ
    "ARG",      # 未使用引数
    "PL",       # pylint のルール一部
    "PERF",     # perflint
]
ignore = [
    "E501",     # line too long (formatter が扱う)
    "ANN401",   # Any を禁じすぎると辛いケースがある
]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101", "PLR2004", "ANN"]   # テストは assert と magic number OK
"__init__.py" = ["F401"]                        # re-export を許容

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
line-ending = "lf"
docstring-code-format = true
```

### 実行

```bash
uv run ruff check .              # lint
uv run ruff check . --fix        # auto-fix できるものは自動修正
uv run ruff format .             # format
uv run ruff format . --check     # CI 用 (差分があれば非 0 終了)
```

### pyright との共存

Ruff でカバーする領域 (import 整理・スタイル・簡易バグ検出) と pyright の型チェックは役割分担する。pyright 側は Ruff がやる import 整理を無効化: `"disableOrganizeImports": true` を `pyrightconfig.json` で設定。

## RSRC-PYTHON-QUALITY.pyright — pyright (Strict 型チェック)

### なぜ pyright を第一選択にするか

- **速度:** mypy 比 3〜10 倍速 (大規模で差が効く)
- **VSCode Pylance の基盤** — エディタ上での型エラーがそのまま CI で再現
- **Strict モードが洗練** — mypy の `--strict` より厳しい追加チェックあり

mypy を使いたいプロジェクトは下記設定を mypy に読み替える。

### `pyrightconfig.json`

```json
{
  "include": ["src", "tests"],
  "exclude": ["**/__pycache__", ".venv", "dist"],
  "venvPath": ".",
  "venv": ".venv",
  "pythonVersion": "3.12",
  "typeCheckingMode": "strict",
  "reportMissingTypeStubs": "warning",
  "reportUnknownMemberType": "warning",
  "disableOrganizeImports": true,
  "useLibraryCodeForTypes": true
}
```

`typeCheckingMode: "strict"` で以下が有効になる:

- `reportGeneralTypeIssues: error`
- `reportMissingParameterType: error`
- `reportMissingReturnType: error`
- `reportUnknownArgumentType: error`
- `reportImplicitStringConcatenation: warning`
- その他 40 項目以上

### 実行

```bash
uv run pyright
```

### 段階的導入

既存の型なしコードに strict を適用すると大量のエラーが出る。段階的に:

1. **まず basic モード** (`typeCheckingMode: "basic"`) で全体を通す
2. **ファイルごとに strict 化** — `# pyright: strict` を先頭行に書く
3. **全体 strict 化** — 最後に pyrightconfig.json を `"strict"` に

### CI 統合

```bash
# GitHub Actions 例
- run: uv sync --frozen
- run: uv run ruff check .
- run: uv run ruff format . --check
- run: uv run pyright
- run: uv run pytest
```

各ステップは並列化できる。

## RSRC-PYTHON-QUALITY.pytest — pytest (テスト戦略)

### なぜ pytest か

- **事実上の標準** (unittest より柔軟、シンプルな assert 文、豊富なプラグインエコシステム)
- Python 公式ドキュメントも pytest を推奨
- `conftest.py` による fixture 共有が大規模で有効

### ディレクトリ構成

```
myproject/
├── src/myproject/
└── tests/
    ├── conftest.py         ← プロジェクト全体の fixture
    ├── unit/
    │   ├── conftest.py     ← unit 用 fixture
    │   ├── test_core.py
    │   └── test_dal.py
    └── integration/
        ├── conftest.py     ← DB コンテナ等重めの fixture
        └── test_api.py
```

### `pyproject.toml` の pytest 設定

```toml
[tool.pytest.ini_options]
minversion = "8.0"
addopts = [
    "-ra",                      # 失敗の理由を要約
    "--strict-markers",         # 未定義 marker でエラー
    "--strict-config",
    "--cov=src/myproject",
    "--cov-report=term-missing",
    "--cov-report=xml",
    "-x",                       # 最初の失敗で停止 (dev 時のみ、CI では外す)
]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
asyncio_mode = "auto"          # async def test_* を自動で async 扱い
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: integration tests (needs DB)",
]
```

### Fixture ベストプラクティス

```python
# tests/conftest.py
import pytest
from pathlib import Path
from myproject.dal import UserRepo

@pytest.fixture(scope="session")
def repo_fixture_data() -> Path:
    return Path(__file__).parent / "fixtures"

@pytest.fixture
def user_repo(tmp_path):                 # function scope がデフォルト
    repo = UserRepo(db=tmp_path / "test.db")
    yield repo                            # yield 前が setup、後が teardown
    repo.close()

@pytest.fixture(scope="module")
async def http_client():
    async with AsyncClient(base_url="http://test") as c:
        yield c
```

**scope の使い分け:**

- `function` (default) — 副作用が漏れないユニットテスト
- `module` — 同一モジュール内で共有できるもの (HTTP client など)
- `session` — 全テスト共通 (静的データ、コストの高いセットアップ)

### Parametrize

```python
import pytest

@pytest.mark.parametrize("input,expected", [
    ("a", 1),
    ("bb", 2),
    ("ccc", 3),
])
def test_length(input: str, expected: int) -> None:
    assert len(input) == expected
```

複数引数を積み重ねれば直積に:

```python
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_mul(x: int, y: int) -> None:
    assert x * y > 0   # 4 通り実行される
```

### Async テスト (pytest-asyncio)

```toml
[tool.pytest.ini_options]
asyncio_mode = "auto"
```

```python
async def test_fetch() -> None:
    result = await fetch_user(1)
    assert result.name == "Alice"
```

**event loop scope:** `asyncio_mode = "auto"` で自動。カスタマイズは `pytest.mark.asyncio(loop_scope="session")` のように mark で指定。

### `tmp_path` / `monkeypatch` / `capsys`

- **`tmp_path`** — テスト用の一時ディレクトリ (自動クリーンアップ)
- **`monkeypatch.setenv("KEY", "value")`** — 環境変数の一時書き換え
- **`monkeypatch.setattr("myproject.foo.bar", new_value)`** — モンキーパッチ
- **`capsys.readouterr()`** — stdout/stderr のキャプチャ

### Coverage

```bash
uv run pytest --cov=src/myproject --cov-report=html
open htmlcov/index.html
```

**大規模の目安:** ユニット 80% 以上、critical path は 95% 以上。網羅率より「意味のあるアサーション」を優先する。

## RSRC-PYTHON-QUALITY.pre-commit — pre-commit hooks

### 設定例 `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.7.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/RobertCraigie/pyright-python
    rev: v1.1.380
    hooks:
      - id: pyright

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-toml
      - id: check-added-large-files
```

### インストール

```bash
uv tool install pre-commit
pre-commit install
```

以降、`git commit` のたびに自動で Ruff + pyright + 基本チェックが走る。

## RSRC-PYTHON-QUALITY.logging — ロギング

### 標準 `logging` モジュール + structlog

```python
import logging
import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
)

log = structlog.get_logger()
log.info("user.created", user_id=123, email="x@example.com")
```

**原則:**
- 本番は JSON ログ出力 (Cloudflare Workers / Datadog / CloudWatch で索引化)
- `print()` 禁止 (Ruff `T20` で検出)
- 構造化ログ (キー付き) で検索性を確保

## RSRC-PYTHON-QUALITY.推奨パターン — 推奨パターン

1. **Ruff を唯一の lint/format ツールにする** (Black + flake8 + isort + pyupgrade を全部置き換え)
2. **target-version を 3.12 以上、`select` は広めに、`ignore` は最小限**
3. **pyright を strict モードで通す**。pyright → mypy への移行は必要時のみ
4. **pytest は `asyncio_mode = "auto"` + `--strict-markers` + `--strict-config`**
5. **fixture scope は function が default。コストの高いものだけ module/session に上げる**
6. **parametrize を重ねて直積テスト**
7. **`tmp_path` / `monkeypatch` を使い、テスト間副作用ゼロを担保**
8. **pre-commit hooks で Ruff + pyright を走らせ、PR で壊れたコードを push させない**
9. **structlog で構造化ログ、本番は JSON Renderer**
10. **CI は `uv sync --frozen → ruff check → ruff format --check → pyright → pytest` の 4 ステップを並列化**

## RSRC-PYTHON-QUALITY.アンチパターン — アンチパターン

1. **Ruff 入れる前提で pylint / flake8 / isort を残す** — 責務が重複してノイズが増える
2. **`# noqa` を理由コメントなしで書く** — `# noqa: E501 (auto-generated SQL)` のように理由を添える
3. **`typeCheckingMode: off` で型を書かない** — basic から入り、段階的に strict へ
4. **テストで `assert result == True`** — `assert result` でよい (Ruff `E712` で検出)
5. **グローバル変数でテスト状態を共有** — fixture に閉じる
6. **`mock.patch` を多用** — fixture で依存を注入できるなら注入する
7. **sleep() でタイミングを取る非同期テスト** — event を使う、もしくは fake clock
8. **coverage を盲信して 100% を目標にする** — 分岐網羅より意味のあるアサーションを優先
9. **`try: except:` の中で logger 書いて握りつぶす** — `logger.exception()` で stacktrace を残す
10. **`print()` でデバッグ** — `structlog` / `logger.debug()` に置き換える

## RSRC-PYTHON-QUALITY.出典 — 出典

参照日: 2026-04-11

- [Ruff: Configuring Ruff | docs.astral.sh](https://docs.astral.sh/ruff/configuration/)
- [Ruff: Settings | docs.astral.sh](https://docs.astral.sh/ruff/settings/)
- [Ruff: Linter | docs.astral.sh](https://docs.astral.sh/ruff/linter/)
- [Ruff: Formatter | docs.astral.sh](https://docs.astral.sh/ruff/formatter/)
- [Ruff: Rules | docs.astral.sh](https://docs.astral.sh/ruff/rules/)
- [pyright docs | microsoft.github.io](https://microsoft.github.io/pyright/)
- [pyright: Configuration | microsoft.github.io](https://microsoft.github.io/pyright/#/configuration)
- [pytest documentation | docs.pytest.org](https://docs.pytest.org/en/stable/)
- [pytest: How to use fixtures | docs.pytest.org](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest: How to parametrize | docs.pytest.org](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [pytest-asyncio documentation | pytest-asyncio.readthedocs.io](https://pytest-asyncio.readthedocs.io/en/stable/)
- [coverage.py documentation | coverage.readthedocs.io](https://coverage.readthedocs.io/)
- [structlog documentation | www.structlog.org](https://www.structlog.org/en/stable/)
- [pre-commit | pre-commit.com](https://pre-commit.com/)
