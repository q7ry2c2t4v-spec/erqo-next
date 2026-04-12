"""load.py - タスク読み込み + UI 判定 + コンテキスト収集 (/codi ステップ1)

TP ページからタスク情報を読み、ルール (スコープフィルタ付き)・
UI 判定・docs 検索・関連ページ収集を行い、コンテキストを返す。

使い方:
    python .nxt-core/core/load.py TASK-ID
"""

import io
import re
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import LIBS_DIR, IS_SOURCE, DESIGN_DIR, FEATURES_DIR, RULES_DIR
from constants import (
    TP_FILE_PATTERN,
    HISTORY_DIR_NAME,
    UI_ID_PATTERNS,
    UI_TAG_KEYWORDS,
    LAYOUT_ID_PATTERNS,
    LAYOUT_TAG_KEYWORDS,
)
from page_parser import parse_tp_row, parse_header, find_section_dir
from index import collect as index_collect
from docs import search as docs_search
from feedback import init_error_handling

init_error_handling()


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


def collect_rules(rules_dir: Path, task_types: list[str]) -> str:
    """プロジェクトルールをスコープフィルタリング付きでロードする。

    ルールファイル内の `適用:` メタデータを読み、task_types のいずれかに
    合致するものだけ返す。適用メタデータがないルールは全タスクに適用 (all)。

    task_types は包含関係を展開したリスト。例:
      - layout タスク → ["layout", "ui", "all"]
      - ui タスク     → ["ui", "all"]
      - 通常タスク    → ["all"]
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

        # フィルタリング: task_types のいずれかが scope に含まれるなら採用
        if scope == "all" or any(tt in scope for tt in task_types):
            parts.append(content)

    return "\n---\n".join(parts)


# --- UI / レイアウト判定 ---


def _score_keywords(
    task_id: str,
    task_info: dict | None,
    tp_content: str,
    id_patterns: list[str],
    tag_keywords: list[str],
) -> tuple[int, list[str]]:
    """タスク ID / タグ / 説明文に含まれるキーワードをスコアリングする。

    _judge_ui と _judge_layout の共通処理。
    Returns: (score, matched_keywords)
    """
    score = 0
    matched: list[str] = []

    # 1. タスク ID パターン
    segments = task_id.split("-")
    for seg in segments:
        if seg.upper() in id_patterns:
            score += 3
            matched.append(seg.lower())

    # 2. TP ページのタグ
    header = parse_header(tp_content)
    if header:
        for tag in header["tags"]:
            if tag.lower() in tag_keywords:
                score += 2
                matched.append(tag.lower())

    # 3. タスク説明文
    if task_info:
        name_lower = task_info.get("name", "").lower()
        for kw in tag_keywords:
            if kw in name_lower:
                score += 1
                if kw not in matched:
                    matched.append(kw)

    return score, matched


def _judge_ui(task_id: str, task_info: dict | None, tp_content: str) -> dict:
    """タスクが UI 関連かどうかをスコアリングで判定する。

    Returns: {"is_ui": bool, "docs_keywords": list[str]}
    """
    score, matched = _score_keywords(
        task_id, task_info, tp_content, UI_ID_PATTERNS, UI_TAG_KEYWORDS
    )
    return {"is_ui": score >= 2, "docs_keywords": list(set(matched))}


def _judge_layout(task_id: str, task_info: dict | None, tp_content: str) -> dict:
    """UI タスクの中でさらに「レイアウトタスク」かどうかを判定する。

    LAYOUT_ID_PATTERNS の語は UI_ID_PATTERNS にも含まれているため、
    レイアウトタスクは必然的に UI 判定でも true になる (layout ⊂ ui)。

    Returns: {"is_layout": bool, "docs_keywords": list[str]}
    """
    score, matched = _score_keywords(
        task_id, task_info, tp_content, LAYOUT_ID_PATTERNS, LAYOUT_TAG_KEYWORDS
    )
    return {"is_layout": score >= 2, "docs_keywords": list(set(matched))}


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

    # --- UI / レイアウト判定 ---
    # layout ⊂ ui の包含関係で 3 値化する。
    #   layout タスク → task_type="layout", task_types=["layout","ui","all"]
    #   ui タスク     → task_type="ui",     task_types=["ui","all"]
    #   それ以外      → task_type="all",    task_types=["all"]
    ui_result = _judge_ui(task_id, task_info, tp_content)
    layout_result = _judge_layout(task_id, task_info, tp_content)

    if layout_result["is_layout"]:
        task_type = "layout"
        task_types = ["layout", "ui", "all"]
    elif ui_result["is_ui"]:
        task_type = "ui"
        task_types = ["ui", "all"]
    else:
        task_type = "all"
        task_types = ["all"]

    if task_type == "layout":
        merged_keywords = list(set(layout_result["docs_keywords"] + ui_result["docs_keywords"]))
        parts.append(
            f"## レイアウト判定: レイアウトタスク (キーワード: {', '.join(merged_keywords)})\n\n"
            "デザインリファレンスは /layo で収集済み。/codi では本棚ページを参照して実装する。"
        )
    elif task_type == "ui":
        parts.append(
            f"## UI 判定: UI タスク (キーワード: {', '.join(ui_result['docs_keywords'])})"
        )
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
    rules_content = collect_rules(RULES_DIR, task_types)
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
