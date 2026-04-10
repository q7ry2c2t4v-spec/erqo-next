"""load.py - タスク読み込み + UI 判定 + コンテキスト収集 (/codi ステップ1)

TP ページからタスク情報を読み、ルール (スコープフィルタ付き)・
UI 判定・docs 検索・関連ページ収集を行い、コンテキストを返す。

使い方:
    python .nxt-core/core/load.py TASK-ID
"""

import io
import json
import re
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import LIBS_DIR, IS_SOURCE, DESIGN_DIR, FEATURES_DIR, RULES_DIR
from page_parser import parse_tp_row, parse_header, TP_FILE_PATTERN, HISTORY_DIR_NAME, find_section_dir
from index import collect as index_collect
from docs import search as docs_search
from feedback import init_error_handling

init_error_handling()

# --- UI 判定キーワード ---

UI_ID_PATTERNS = ["UI", "CARD", "VIEWER", "THEME", "COLOR", "LAYOUT", "NAV", "PAGE"]
UI_TAG_KEYWORDS = ["ui", "コンポーネント", "レイアウト", "画面", "component", "layout", "page"]


# --- TP 探索 ---


def _find_tp_page(task_id: str, design_dir: Path) -> tuple[Path | None, dict | None]:
    """タスク ID から TP ページとタスク情報を探す。"""
    section_dir = find_section_dir(task_id, design_dir)
    if not section_dir:
        return None, None

    for md_file in section_dir.glob(TP_FILE_PATTERN):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        if task_id not in content:
            continue

        task_info = None
        for line in content.splitlines():
            row = parse_tp_row(line)
            if row and row["id"] == task_id:
                task_info = row
                break
        return md_file, task_info

    return None, None


# --- セクション features ---


def _collect_section_features(task_id: str, features_dir: Path) -> str:
    """同セクション内の全 features ページを読み込む。"""
    section_dir = find_section_dir(task_id, features_dir)
    if not section_dir:
        return ""

    parts = []
    for md_file in sorted(section_dir.glob("*.md")):
        if HISTORY_DIR_NAME in md_file.parts:
            continue
        try:
            parts.append(md_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError):
            continue
    return "\n---\n".join(parts)


# --- ルール (スコープフィルタリング) ---


def _collect_rules(rules_dir: Path, task_type: str) -> str:
    """プロジェクトルールをスコープフィルタリング付きでロードする。

    ルールファイル内の `適用:` メタデータを読み、task_type に合致するものだけ返す。
    適用メタデータがないルールは全タスクに適用 (all)。
    """
    if not rules_dir.exists():
        return ""

    parts = []
    for md_file in sorted(rules_dir.glob("*.md")):
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        # 適用スコープを抽出
        scope = "all"
        for line in content.splitlines()[:10]:
            m = re.match(r"^適用:\s*(.+)$", line)
            if m:
                scope = m.group(1).strip().lower()
                break

        # フィルタリング
        if scope == "all" or task_type in scope:
            parts.append(content)

    return "\n---\n".join(parts)


# --- UI 判定 ---


def _judge_ui(task_id: str, task_info: dict | None, tp_content: str) -> dict:
    """タスクが UI 関連かどうかをスコアリングで判定する。

    Returns: {"is_ui": bool, "docs_keywords": list[str]}
    """
    score = 0
    docs_keywords = []

    # 1. タスク ID パターン
    segments = task_id.split("-")
    for seg in segments:
        if seg.upper() in UI_ID_PATTERNS:
            score += 3
            docs_keywords.append(seg.lower())

    # 2. TP ページのタグに UI キーワード
    header = parse_header(tp_content)
    if header:
        for tag in header["tags"]:
            if tag.lower() in UI_TAG_KEYWORDS:
                score += 2
                docs_keywords.append(tag.lower())

    # 3. タスク説明文に UI キーワード
    if task_info:
        name_lower = task_info.get("name", "").lower()
        for kw in UI_TAG_KEYWORDS:
            if kw in name_lower:
                score += 1
                if kw not in docs_keywords:
                    docs_keywords.append(kw)

    return {"is_ui": score >= 2, "docs_keywords": list(set(docs_keywords))}


# --- メイン ---


def load_task(task_id: str) -> str:
    """タスク ID からコンテキストを収集して返す。"""
    if IS_SOURCE:
        return "エラー: 本体リポジトリでは /codi を実行できません。"

    if not LIBS_DIR or not LIBS_DIR.exists():
        return "エラー: .libs/ が見つかりません。install.py を実行してください。"

    parts = []

    # --- TP ページからタスク情報 ---
    tp_path, task_info = _find_tp_page(task_id, DESIGN_DIR)
    if tp_path is None:
        return f"エラー: タスク {task_id} が見つかりません。TP ページに登録されているか確認してください。"

    tp_content = tp_path.read_text(encoding="utf-8")

    if task_info:
        parts.append(f"## 対象タスク: {task_info['id']} - {task_info['name']} ({task_info['deps']})")

    parts.append(f"## タスク計画\n\n{tp_content}")

    # --- UI 判定 ---
    ui_result = _judge_ui(task_id, task_info, tp_content)
    task_type = "ui" if ui_result["is_ui"] else "all"

    if ui_result["is_ui"]:
        parts.append(f"## UI 判定: UI タスク (キーワード: {', '.join(ui_result['docs_keywords'])})")

        # docs 検索
        if ui_result["docs_keywords"]:
            doc_results = docs_search(ui_result["docs_keywords"], max_results=10)
            if doc_results:
                doc_lines = [f"- {r['path']} (score: {r['score']})" for r in doc_results]
                parts.append(f"## 関連ドキュメント\n\n" + "\n".join(doc_lines))

    # --- 同セクション features ---
    section_features = _collect_section_features(task_id, FEATURES_DIR)
    if section_features:
        section_name = task_id.split("-")[0]
        parts.append(f"## 同セクション ({section_name}) の既存記録\n\n{section_features}")

    # --- 関連ページ収集 (index.collect) ---
    keywords = task_id.split("-")
    if task_info:
        keywords.extend(task_info.get("name", "").split())
    related = index_collect(keywords)
    if related:
        section_prefix = task_id.split("-")[0] + "-"
        other = [r for r in related if not r["id"].startswith(section_prefix) and r["id"] != task_id]
        if other:
            related_lines = []
            for r in other[:10]:
                path = LIBS_DIR / r["path"] if r.get("path") else None
                if path and path.exists():
                    try:
                        related_lines.append(path.read_text(encoding="utf-8"))
                    except (OSError, UnicodeDecodeError):
                        pass
            if related_lines:
                parts.append(f"## 関連ページ (他セクション)\n\n" + "\n---\n".join(related_lines))

    # --- ルール (スコープフィルタリング) ---
    rules_content = _collect_rules(RULES_DIR, task_type)
    if rules_content:
        parts.append(f"## プロジェクトルール\n\n{rules_content}")

    return "\n\n---\n\n".join(parts)


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python core/load.py TASK-ID", file=sys.stderr)
        sys.exit(1)

    task_id = sys.argv[1].upper()
    print(load_task(task_id))


if __name__ == "__main__":
    main()
