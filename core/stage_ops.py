"""stage_ops.py — 自動ステージングスクリプト

git status の変更ファイル一覧から、ブラックリストに該当しないものを
機械的にステージングする。/wrap の手動ファイル指定手順を置き換え、
AI の曖昧判断（specs/08-responsibility.md）を排除するためのもの。

呼び出し元:
- /wrap ステップ 5-4（ステージング）

使い方:
    python core/stage_ops.py collect   # 対象を表示（dry-run）
    python core/stage_ops.py stage     # 実際に git add 実行
"""

import io
import subprocess
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from constants import STAGE_BLACKLIST_PREFIXES
from paths import PROJECT_ROOT
from feedback import init_error_handling

init_error_handling()


def _require_root() -> Path:
    if PROJECT_ROOT is None:
        print("エラー: プロジェクトルートが見つかりません。", file=sys.stderr)
        sys.exit(1)
    return PROJECT_ROOT


def _run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    root = _require_root()
    result = subprocess.run(
        cmd, capture_output=True, text=True,
        cwd=str(root), encoding="utf-8",
    )
    if check and result.returncode != 0:
        print(f"エラー: {' '.join(cmd)}", file=sys.stderr)
        if result.stderr.strip():
            print(f"  {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)
    return result


def _is_blacklisted(path: str) -> bool:
    """ブラックリストプレフィックスに前方一致するか。"""
    normalized = path.replace("\\", "/")
    return any(normalized.startswith(prefix) for prefix in STAGE_BLACKLIST_PREFIXES)


def _parse_status_line(line: str) -> str | None:
    """git status --porcelain=v1 の 1 行からファイルパスを取り出す。

    フォーマット: "XY path" または "XY old -> new"（リネーム時）。
    """
    if len(line) < 4:
        return None
    rest = line[3:]
    if " -> " in rest:
        rest = rest.split(" -> ", 1)[1]
    if rest.startswith('"') and rest.endswith('"'):
        rest = rest[1:-1]
    return rest


def _collect_files() -> tuple[list[str], list[str]]:
    """ステージング候補と除外候補に分類する。

    .gitignore に該当するファイルは git status が既に除外済み。
    残りに対してブラックリストプレフィックスを適用する。
    """
    result = _run(["git", "status", "--porcelain=v1"])
    included: list[str] = []
    excluded: list[str] = []
    for line in result.stdout.splitlines():
        path = _parse_status_line(line)
        if path is None:
            continue
        if _is_blacklisted(path):
            excluded.append(path)
        else:
            included.append(path)
    return included, excluded


def _print_list(label: str, items: list[str]) -> None:
    print(f"{label}: {len(items)} ファイル")
    for path in items:
        print(f"  {path}")


# --- 公開 API ---


def cmd_collect() -> None:
    """ステージング対象を表示する（dry-run、git add は実行しない）。"""
    included, excluded = _collect_files()
    if not included and not excluded:
        print("変更なし")
        return
    if included:
        _print_list("ステージング対象", included)
    if excluded:
        if included:
            print()
        _print_list("除外（ブラックリスト）", excluded)


_GIT_ADD_BATCH_SIZE = 200  # Windows の CreateProcess 引数長制限 (~32k) を避けるためのバッチ幅


def _git_add_batched(files: list[str]) -> None:
    """`git add -- <files>` をバッチ分割して実行する (Windows の引数長制限回避)。"""
    for i in range(0, len(files), _GIT_ADD_BATCH_SIZE):
        batch = files[i:i + _GIT_ADD_BATCH_SIZE]
        _run(["git", "add", "--"] + batch)


def cmd_stage() -> None:
    """ステージング対象を実際に git add する。"""
    included, excluded = _collect_files()
    if not included:
        if excluded:
            print("ステージング対象なし（ブラックリストのみ）")
        else:
            print("変更なし")
        return
    _git_add_batched(included)
    _print_list("ステージング完了", included)
    if excluded:
        print()
        _print_list("除外", excluded)


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python core/stage_ops.py <collect|stage>", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1]
    if command == "collect":
        cmd_collect()
    elif command == "stage":
        cmd_stage()
    else:
        print(f"エラー: 不明なコマンド '{command}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
