"""coding_rules_hook.py — PreToolUse コーディングルール通知 Hook

エル子が Write / Edit / NotebookEdit を呼んだ瞬間に、対象ファイルに適用される
コーディングルールファイルの一覧を stderr に流して AI コンテキストへ注入する。
ブロックはしない (exit 0)。情報提供のみ。

write_guard.py と並んで PreToolUse Hook (matcher: Write|Edit|NotebookEdit) に
登録される。順序は write_guard.py が先 (保護パスで止める) → coding_rules_hook.py
(情報提供) の順。

呼び出し元:
- PreToolUse Hook (matcher: Write|Edit|NotebookEdit)

動作仕様:
- stdin の JSON から tool_input.file_path を抽出
- coding_rules.get_applicable_rules() で適用ルール一覧を機械判定
- L2 or L3 が含まれる (=コード) ときだけ stderr 出力
- L1 のみ (=コードでない md など) は黙って終了
- file_path が取得不能・例外発生は fail-open (exit 0)

責務分離:
- 判定ロジックは coding_rules.py の get_applicable_rules() に集約
- このスクリプトは「stdin → 判定 → stderr」の I/O 仲介のみ
- specs/08-responsibility.md の機械判定原則に整合
"""

import io
import json
import os
import sys
from pathlib import Path

# Windows UTF-8 出力 (日本語ラベルが含まれるため必須)
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from constants import CODING_RULES_HOOK_FOOTER, CODING_RULES_HOOK_HEADER
from coding_rules import get_applicable_rules


def _resolve_target(file_path: str, project_dir: str) -> Path | None:
    """tool_input.file_path をプロジェクトルートからの絶対パスに解決する。

    プロジェクト外や解釈不能なパスは None。
    """
    try:
        fp = Path(file_path)
        if not fp.is_absolute():
            fp = Path(project_dir) / fp
        return fp.resolve()
    except (ValueError, OSError):
        return None


def _format_message(rules: list[tuple[Path, str]], project_root: Path) -> str:
    """stderr に出すメッセージを組み立てる。"""
    lines = [CODING_RULES_HOOK_HEADER]
    for rule_path, label in rules:
        try:
            rel = rule_path.relative_to(project_root).as_posix()
        except ValueError:
            rel = str(rule_path)
        lines.append(f"- {rel} ({label})")
    lines.append(CODING_RULES_HOOK_FOOTER)
    return "\n".join(lines)


def main() -> None:
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR")
    if not project_dir:
        return  # fail-open

    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return  # fail-open

    tool_input = data.get("tool_input", {}) or {}
    file_path = (
        tool_input.get("file_path")
        or tool_input.get("notebook_path")
        or ""
    )
    if not file_path:
        return

    project_root = Path(project_dir).resolve()
    target = _resolve_target(file_path, project_dir)
    if target is None:
        return

    rules = get_applicable_rules(target, project_root)

    # L1 ハブ 1 件しか含まれていなければ「コードファイルではない」とみなして黙る
    if len(rules) <= 1:
        return

    print(_format_message(rules, project_root), file=sys.stderr)
    # 情報提供のみ。ブロックしない (exit 0)。


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # 失敗時は AI 作業を妨げないため fail-open
        sys.exit(0)
