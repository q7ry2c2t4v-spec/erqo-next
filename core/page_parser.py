"""page_parser.py — ページフォーマット解析モジュール

ページテキストからヘッダーメタデータとセクション構造を抽出する。
TP テーブルのパース関数もここで提供する。

公開定数（TP_FILE_PATTERN, STATE_FILE_PREFIX, HISTORY_DIR_NAME, STATUS_*）は
constants.py に集約されている。各モジュールは constants から直接 import すること。
"""

import re
from pathlib import Path

# --- TP テーブル列インデックス（モジュール内部のみ） ---

_TP_COL_ID = 1
_TP_COL_NAME = 2
_TP_COL_DEPS = 3
_TP_COL_STATUS = 4
_TP_MIN_COLS = 5
_TP_SKIP_IDS = {"識別コード", "---", "#"}


def parse_tp_row(line: str) -> dict | None:
    """TP テーブル行をパースする。ヘッダー・区切り行は None。

    Returns: {"id", "name", "deps", "status"} or None
    """
    if "|" not in line:
        return None
    cells = [c.strip() for c in line.split("|") if c.strip()]
    if len(cells) < _TP_MIN_COLS:
        return None
    tid = cells[_TP_COL_ID]
    if tid in _TP_SKIP_IDS:
        return None
    return {
        "id": tid,
        "name": cells[_TP_COL_NAME],
        "deps": cells[_TP_COL_DEPS],
        "status": cells[_TP_COL_STATUS],
    }


def find_section_dir(task_id: str, base_dir: Path) -> Path | None:
    """タスク ID の先頭セグメントからセクションディレクトリを探す。

    PIPE-STATE → まず "pipe" を探し、なければ "pipe" で始まるフォルダを探す。
    """
    section = task_id.split("-")[0].lower()
    exact = base_dir / section
    if exact.exists():
        return exact
    for d in sorted(base_dir.iterdir()):
        if d.is_dir() and d.name.startswith(section):
            return d
    return None


def parse_header(text: str) -> dict | None:
    """ページテキストからヘッダーメタデータを抽出する。

    Returns: {"id", "title", "tags": list, "related": list} or None
    """
    lines = text.split("\n")
    if not lines:
        return None

    # H1: # ID-CODE — タイトル
    m = re.match(r"^#\s+(\S+)\s+—\s+(.+)$", lines[0])
    if not m:
        return None

    header = {
        "id": m.group(1),
        "title": m.group(2).strip(),
        "tags": [],
        "related": [],
    }

    # H1 直後からメタデータを取得（最初のセクション見出しまで）
    for line in lines[1:]:
        stripped = line.strip()
        if stripped.startswith("#"):
            break
        if stripped.startswith("関連:"):
            raw = stripped[len("関連:"):].strip()
            header["related"] = [s.strip() for s in raw.split(",") if s.strip()]
        elif stripped.startswith("タグ:"):
            raw = stripped[len("タグ:"):].strip()
            header["tags"] = [s.strip() for s in raw.split(",") if s.strip()]

    return header


def parse_sections(text: str) -> list[dict]:
    """ページテキストからセクション構造を抽出する。

    Returns: [{"id", "title", "level": int, "content": str}, ...]
    """
    sections = []
    current = None

    for line in text.split("\n"):
        # ## ID.section — タイトル  or  ### ID.sub — タイトル
        m = re.match(r"^(#{2,6})\s+(\S+)\s+—\s+(.+)$", line)
        if m:
            if current is not None:
                current["content"] = current["content"].strip()
                sections.append(current)
            current = {
                "id": m.group(2),
                "title": m.group(3).strip(),
                "level": len(m.group(1)),
                "content": "",
            }
        elif current is not None:
            current["content"] += line + "\n"

    if current is not None:
        current["content"] = current["content"].strip()
        sections.append(current)

    return sections
