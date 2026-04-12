"""coding_rules.py — ファイルパスから適用すべきコーディングルールを機械判定する。

エル子 (AI) はコード編集前に必ずこのスクリプトを呼び、返ってきたルールファイルを
すべて Read してから実装する。AI の自己判断は挟まない。

判定ロジック (機械的):
- 常時: specs/06-coding-rules.md (L1 汎用共通ハブ)
- .py: + specs/coding/l2-python.md
- .ts / .tsx / .mts / .cts: + specs/coding/l2-typescript.md
  - かつプロジェクトルートに next.config.ts|mjs|js があれば: + l3-nextjs.md
  - かつプロジェクトルートに wrangler.jsonc|json|toml があるか、
    または対象ファイルのパス部に "workers" が含まれていれば: + l3-cloudflare.md

出力: 該当ルールファイルのパスを 1 行 1 ファイルで stdout に書き出す。
終了コード: 正常 0、引数不正 2、ファイル未発見 3。

使い方 (本元):
    python core/coding_rules.py src/app/page.tsx
    python core/coding_rules.py core/state.py
    python core/coding_rules.py workers/src/index.ts

使い方 (プロジェクト):
    python .nxt-core/core/coding_rules.py src/app/page.tsx

参照: specs/06-coding-rules.md §0 適用マトリックス
     specs/08-responsibility.md (責務分離・AI 自己判断の禁止)
"""

from __future__ import annotations

import io
import sys
from pathlib import Path

# Windows の cp932 環境でも日本語ラベルを出せるように UTF-8 に切り替える
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from constants import (
    CLOUDFLARE_MARKER_FILES,
    NEXTJS_MARKER_FILES,
    PYTHON_FILE_EXTENSIONS,
    TYPESCRIPT_FILE_EXTENSIONS,
    WORKERS_DIR_NAME,
)
from paths import (
    CODING_HUB_FILE,
    CODING_L2_PYTHON_FILE,
    CODING_L2_TYPESCRIPT_FILE,
    CODING_L3_CLOUDFLARE_FILE,
    CODING_L3_NEXTJS_FILE,
    PROJECT_ROOT,
)

# 出力時のラベル
_LABEL_HUB = "L1 汎用 — 常時適用"
_LABEL_PYTHON = "L2 Python"
_LABEL_TYPESCRIPT = "L2 TypeScript"
_LABEL_NEXTJS = "L3 Next.js"
_LABEL_CLOUDFLARE = "L3 Cloudflare"

_USAGE = "usage: python core/coding_rules.py <file_path>"
_EXIT_BAD_ARGS = 2
_EXIT_NO_PROJECT = 3


def _has_any_marker(project_root: Path, markers: tuple[str, ...]) -> bool:
    """プロジェクトルート直下にマーカーファイルが 1 つでも存在するか。"""
    return any((project_root / name).exists() for name in markers)


def _is_in_path_keyword(file_path: Path, project_root: Path, keyword: str) -> bool:
    """対象ファイルの相対パスに `keyword` がディレクトリ部として含まれているか。"""
    try:
        rel = file_path.relative_to(project_root)
    except ValueError:
        return False
    return keyword in rel.parts


# --- L2 / L3 ルール判定テーブル ---
# 新言語を追加するときはこのリストに 1 辞書を足すだけで追従する (拡張容易性)。
# L1 §1.1 ハードコ禁止・§1.2 DRY に準拠し、if/elif 分岐はここには書かない。

_L2_RULES: list[dict] = [
    {
        "extensions": PYTHON_FILE_EXTENSIONS,
        "path": CODING_L2_PYTHON_FILE,
        "label": _LABEL_PYTHON,
        "l3": (),
    },
    {
        "extensions": TYPESCRIPT_FILE_EXTENSIONS,
        "path": CODING_L2_TYPESCRIPT_FILE,
        "label": _LABEL_TYPESCRIPT,
        "l3": (
            {
                "path": CODING_L3_NEXTJS_FILE,
                "label": _LABEL_NEXTJS,
                "markers": NEXTJS_MARKER_FILES,
                "path_keywords": (),
            },
            {
                "path": CODING_L3_CLOUDFLARE_FILE,
                "label": _LABEL_CLOUDFLARE,
                "markers": CLOUDFLARE_MARKER_FILES,
                "path_keywords": (WORKERS_DIR_NAME,),
            },
        ),
    },
]


def get_applicable_rules(file_path: Path, project_root: Path) -> list[tuple[Path, str]]:
    """ファイルパスから適用ルールを (Path, ラベル) のリストで返す。

    L1 ハブは必ず先頭に入る。該当しない拡張子の場合は L1 のみ。
    新言語を追加するときは `_L2_RULES` に 1 辞書を足すだけで追従する。
    """
    rules: list[tuple[Path, str]] = [(CODING_HUB_FILE, _LABEL_HUB)]
    suffix = file_path.suffix

    for l2 in _L2_RULES:
        if suffix not in l2["extensions"]:
            continue
        rules.append((l2["path"], l2["label"]))
        for l3 in l2["l3"]:
            marker_hit = _has_any_marker(project_root, l3["markers"])
            path_hit = any(
                _is_in_path_keyword(file_path, project_root, kw)
                for kw in l3["path_keywords"]
            )
            if marker_hit or path_hit:
                rules.append((l3["path"], l3["label"]))
        break  # 拡張子は 1 グループにしかマッチしない前提

    return rules


def _format_line(rule_path: Path, label: str, project_root: Path) -> str:
    """1 行分の出力を組み立てる。プロジェクト相対パス + ラベル。"""
    try:
        rel = rule_path.relative_to(project_root)
        display = str(rel).replace("\\", "/")
    except ValueError:
        display = str(rule_path)
    return f"{display:40s} ({label})"


def main() -> int:
    if len(sys.argv) != 2:
        print(_USAGE, file=sys.stderr)
        return _EXIT_BAD_ARGS

    if PROJECT_ROOT is None:
        print("error: project root not found (CLAUDE.md missing)", file=sys.stderr)
        return _EXIT_NO_PROJECT

    file_path = Path(sys.argv[1])
    if not file_path.is_absolute():
        file_path = (PROJECT_ROOT / file_path).resolve()
    else:
        file_path = file_path.resolve()

    rules = get_applicable_rules(file_path, PROJECT_ROOT)
    for rule_path, label in rules:
        print(_format_line(rule_path, label, PROJECT_ROOT))

    return 0


if __name__ == "__main__":
    sys.exit(main())
