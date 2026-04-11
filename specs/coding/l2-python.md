# L2 Python コーディングルール

**適用対象:** `.py` 拡張子のファイル全般
**前提:** 必ず `specs/06-coding-rules.md` (L1 汎用共通) と合わせて適用する
**詳細リサーチ:** `RSRC-PYTHON-ARCH` / `RSRC-PYTHON-QUALITY` (`.libs/research/python/`)
**機械判定:** `python core/coding_rules.py <file.py>`

---

## 1. 本元 vs プロジェクトの棲み分け

- **本元 erqo-next の `core/` 直下** — **Python 標準ライブラリのみ** を使う (giget 配布先で追加インストール不要にするため)。uv / Ruff / pyright / pytest 等のツールチェーンは本元では採用しない
- **外部ライブラリが必要な機能** — 本元では `core/<feature>_node/` のような隔離サブディレクトリに分離する (前例: `core/clone_node/`)
- **プロジェクト側の `scripts/` や Python アプリ** — §3 以降のツールチェーン (uv / Ruff / pyright / pytest) をフル適用する

## 2. 定数の配置先 **[MUST]**

| 種類 | 配置先 |
|---|---|
| パス・ディレクトリ名 | `core/paths.py` |
| ファイル名・プレフィックス・固定文字列・棚名リスト等 | `core/constants.py` |
| モジュール固有の内部定数 | 該当モジュール冒頭 (他から import されない範囲に限る) |

**迷ったら:** パス由来なら `paths.py`、それ以外は `constants.py`。

### エラー処理と自動フィードバック **[SHOULD]**

- 未処理エラーは `core/feedback.py` の `init_error_handling()` で自動 JSON 保存される前提。キャッチしない例外は捨てない
- 一時的エラーは `with_retry()` デコレータで最大 3 回リトライ
- 明示的エラー報告は `report_error(exc)` を使う

### Windows cp932 対策 **[MUST]**

`core/` の Python スクリプトが stdout/stderr に日本語を書くなら、ファイル冒頭で UTF-8 を強制する:

```python
import io
import sys
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
```

**理由:** Windows 標準の cp932 環境では em-dash `—` などが `UnicodeEncodeError` になる。本元は Windows 環境での開発を想定しているため必須。

## 3. パッケージ構成 (プロジェクト側) **[MUST]**

- **Python 3.12 以上を target** — `pyproject.toml` の `requires-python = ">=3.12"` を宣言
- **`src-layout` を採用** — アプリコードは `src/myproject/` に置き、`tests/` を並列に
- **`pyproject.toml` を PEP 621 準拠で 1 ファイル管理** (`setup.py` / `setup.cfg` は使わない)
- **パッケージマネージャは `uv`** — `uv.lock` を必ず commit、`.venv/` は `.gitignore`

### 推奨ディレクトリ構成

```
myproject/
├── pyproject.toml
├── uv.lock              ← commit
├── .python-version
├── src/
│   └── myproject/
└── tests/
```

### 代表的 uv コマンド

- `uv init` / `uv init --lib` — プロジェクト初期化
- `uv add <pkg>` / `uv add --dev <pkg>` — 依存追加
- `uv sync --frozen` — CI で lockfile に従って同期
- `uv run <cmd>` — lockfile 整合性チェックしてから実行

## 4. 型システム **[MUST]**

- **PEP 695 `type` 構文** で generic を書く: `def first[T](xs: list[T]) -> T:`
- **`TypeVar` の事前宣言は書かない** (PEP 695 構文に書き換える)
- **`from typing import List, Dict`** は使わない — 組み込み `list`, `dict` を直接使う
- **戻り値型を `Any` にしない** — 書くなら `object`
- **サブクラスの override は `@typing.override` で宣言**
- **非推奨化は `@warnings.deprecated("use X")` で宣言** (3.13+)
- **外部境界 (API / env / CLI 入力) は `pydantic.BaseModel` v2 で validate**、内部構造は `@dataclass(slots=True)` で十分

## 5. 非同期・エラー処理 **[MUST]**

- **並列実行は `asyncio.gather` ではなく `asyncio.TaskGroup`** — キャンセル伝播・例外収集が自動
- **複数例外は `except* ValueError as eg:` のように `ExceptionGroup` を品目別ハンドル**
- **タイムアウトは `async with asyncio.timeout(seconds):`**
- **`try: except Exception:` のような広いキャッチは禁止** — 型を絞るか、`except*` を使う
- **`logger.exception(...)` で stacktrace を残す。握りつぶし禁止**

## 6. Lint / Format: Ruff **[MUST]** (プロジェクト側のみ)

**Ruff が唯一の lint / format ツール** — Black / flake8 / isort / pyupgrade / autoflake を全て置き換える。本元 `core/` は対象外 (標準ライブラリ運用のため)。

### `pyproject.toml` 推奨設定

```toml
[tool.ruff]
target-version = "py312"
line-length = 100
src = ["src", "tests"]

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP", "B", "A", "C4", "DTZ",
          "T20", "PT", "SIM", "TCH", "RUF", "ANN", "S", "ARG", "PL", "PERF"]
ignore = ["E501", "ANN401"]

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["S101", "PLR2004", "ANN"]
"__init__.py" = ["F401"]

[tool.ruff.format]
quote-style = "double"
docstring-code-format = true
```

- `uv run ruff check .` / `uv run ruff check . --fix` / `uv run ruff format .`
- **`# noqa` は必ず理由コメント付き** — `# noqa: E501 (auto-generated SQL)`

## 7. 型チェック: pyright **[MUST]** (プロジェクト側のみ)

**pyright を第一選択** — mypy より速く、Pylance と同じエンジンで VSCode 連動。

### `pyrightconfig.json` 推奨設定

```json
{
  "include": ["src", "tests"],
  "pythonVersion": "3.12",
  "typeCheckingMode": "strict",
  "venvPath": ".",
  "venv": ".venv",
  "disableOrganizeImports": true
}
```

- **段階的導入:** まず `"basic"` で全体を通し、ファイル単位で `# pyright: strict` を付けて強化
- 既存コードに strict を一括適用するとエラーが大量発生するため必ず段階的に

## 8. テスト: pytest **[MUST]** (プロジェクト側のみ)

### 原則

- **`pytest` + `pytest-asyncio`** を標準構成
- **`asyncio_mode = "auto"`** で `async def test_*` を自動認識
- **`--strict-markers` + `--strict-config`** で typo / 未登録 marker を検出
- **fixture scope はデフォルト function** — コストの高いものだけ `module` / `session`
- **parametrize を積極利用** — 直積テストで網羅
- **`tmp_path` / `monkeypatch` で副作用を閉じる**
- **テスト間の状態共有禁止** — グローバル変数・クラス変数に状態を貯めない
- **sleep でタイミング取り禁止** — event or fake clock で制御する
- **coverage は目安 80% 以上、critical path は 95% 以上** — 数字より「意味のあるアサーション」優先

### `pyproject.toml` 推奨設定

```toml
[tool.pytest.ini_options]
minversion = "8.0"
addopts = ["-ra", "--strict-markers", "--strict-config",
           "--cov=src/myproject", "--cov-report=term-missing"]
testpaths = ["tests"]
asyncio_mode = "auto"
```

## 9. ロギング **[SHOULD]** (プロジェクト側のみ)

- **`print()` 禁止** (Ruff `T20` で検出)
- **`structlog` で構造化ログ** — 本番は `JSONRenderer` でログ検索可能に
- **`logger.debug()` / `logger.info()` / `logger.exception()` を使い分け**

## 10. pre-commit hooks **[SHOULD]** (プロジェクト側のみ)

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
```

## 11. CI パイプライン **[SHOULD]** (プロジェクト側のみ)

並列で 4 ステップを回す:

```bash
uv sync --frozen
uv run ruff check . && uv run ruff format . --check
uv run pyright
uv run pytest
```
