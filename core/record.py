"""record.py - 記録統合 (/codi ステップ4: recording)

features ページ作成・FIX マージ・TP ステータス更新・ユーザーガイド管理を
1モジュールに統合。旧 record.py + auto_commit.py + guide_update.py の統合版。

使い方:
    python .nxt-core/core/record.py TASK-ID                              # 新規/FIX 準備
    python .nxt-core/core/record.py TASK-ID merge --changed S1,S2 --file PATH  # FIX マージ
    python .nxt-core/core/record.py TASK-ID status                       # TP ステータス更新
    python .nxt-core/core/record.py TASK-ID guide SECTION                # ガイドファイルパス
    python .nxt-core/core/record.py TASK-ID guide_index SECTION          # index.md 再生成
"""

import io
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import LIBS_DIR, IS_SOURCE, DESIGN_DIR, FEATURES_DIR, UI_SPECS_DIR
from constants import (
    TP_FILE_PATTERN,
    STATUS_DONE,
    STATUS_TODO,
    STATUS_WIP,
    HISTORY_DIR_NAME,
    INDEX_MD_FILENAME,
    LAYOUT_ID_PATTERNS,
    STORYBOOK_SHELF_NAME,
)
from page_parser import parse_sections, find_section_dir
from feedback import init_error_handling

init_error_handling()

# --- 定数 ---

TEMPLATE = """\
# {task_id} — {title}

関連: {related}
タグ: {tags}

## {task_id}.概要 — 概要
(何を実装したか)

## {task_id}.仕様 — 仕様詳細
(具体的な仕様・動作・設定)

## {task_id}.設計判断 — なぜこうしたか
(選んだ理由、却下した代替案、トレードオフ)

## {task_id}.構成 — ファイル構成
(変更・追加したファイルとその役割)

## {task_id}.トラブル — 問題と解決
(遭遇した問題、解決策、修正内容)

## {task_id}.参考リサーチ — 参考にした外部情報
(ウェブリサーチで参照した公式ドキュメント・仕様書・記事の URL、要点、引用箇所を記録する。リサーチを行わなかった場合は「該当なし」と明記する)

## {task_id}.備考 — 補足
(依存関係、今後の構成予定、注意事項)
"""

RE_SECTION = re.compile(r"^## ([A-Z0-9][A-Z0-9-]+\.\S+)\s*[—\-]\s*(.+)$", re.MULTILINE)


# --- ユーティリティ ---


def _check_project():
    """プロジェクト環境チェック。"""
    if IS_SOURCE:
        print("エラー: 本体リポジトリでは実行できません。", file=sys.stderr)
        sys.exit(1)
    if not LIBS_DIR or not LIBS_DIR.exists():
        print("エラー: .libs/ が見つかりません。", file=sys.stderr)
        sys.exit(1)


def _is_fix_task(task_id: str) -> bool:
    return "-FIX-" in task_id or task_id.endswith("-FIX")


def _is_layout_task(task_id: str) -> bool:
    """タスク ID がレイアウト系かどうかを機械判定する。"""
    segments = task_id.split("-")
    return any(seg.upper() in LAYOUT_ID_PATTERNS for seg in segments)


def _bookshelf_page_path(task_id: str) -> Path | None:
    """本棚正本ページのパスを返す (存在チェックなし)。"""
    if LIBS_DIR is None:
        return None
    slug = task_id.lower()
    return LIBS_DIR / STORYBOOK_SHELF_NAME / slug / f"{slug}.md"


def _get_original_id(fix_task_id: str) -> str:
    """FIX タスク ID から元の識別コードを取得。AUTH-SESSION-FIX-001 → AUTH-SESSION"""
    parts = fix_task_id.split("-")
    result = []
    for part in parts:
        if part == "FIX":
            break
        result.append(part)
    return "-".join(result)


def _get_filename(task_id: str) -> str:
    return task_id.lower().replace("_", "-") + ".md"


def _merge_sections(old_content: str, new_sections: dict[str, str]) -> str:
    """旧ページと新セクションをマージする。"""
    first_match = RE_SECTION.search(old_content)
    header = old_content[:first_match.start()].rstrip() if first_match else old_content

    result_parts = [header]
    matches = list(RE_SECTION.finditer(old_content))

    for i, match in enumerate(matches):
        section_title = match.group(2).strip()
        heading_line = match.group(0)
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(old_content)

        if section_title in new_sections:
            result_parts.append(f"\n{heading_line}\n{new_sections[section_title]}")
        else:
            old_body = old_content[start:end].rstrip()
            result_parts.append(f"\n{heading_line}{old_body}")

    return "\n".join(result_parts) + "\n"


# --- features ページ ---


def create_record(task_id: str) -> None:
    """features ページを新規作成、または FIX 準備をする。"""
    _check_project()
    section = task_id.split("-")[0].lower()
    section_dir = FEATURES_DIR / section
    section_dir.mkdir(parents=True, exist_ok=True)

    if _is_fix_task(task_id):
        original_id = _get_original_id(task_id)
        original_path = section_dir / _get_filename(original_id)
        if not original_path.exists():
            print(f"エラー: 元ページ {original_path} が見つかりません。", file=sys.stderr)
            sys.exit(1)

        history_dir = section_dir / HISTORY_DIR_NAME
        history_dir.mkdir(exist_ok=True)
        date_str = datetime.now().strftime("%Y%m%d")
        archive_path = history_dir / f"{original_path.stem}.{date_str}.md"
        shutil.copy2(original_path, archive_path)

        print("record: 修正準備完了")
        print(f"  元ページ: {original_path}")
        print(f"  アーカイブ: {archive_path}")
    else:
        filepath = section_dir / _get_filename(task_id)
        tp_id = f"TP-{section.upper()}"

        # レイアウトタスク: 本棚ページへの参照を自動付与
        related = tp_id
        bookshelf_path = _bookshelf_page_path(task_id)
        if _is_layout_task(task_id) and bookshelf_path and bookshelf_path.exists():
            bookshelf_rel = str(
                bookshelf_path.relative_to(LIBS_DIR.parent)
            ).replace("\\", "/")
            related = f"{tp_id}, {bookshelf_rel}"

        content = TEMPLATE.format(
            task_id=task_id, title="タイトル", related=related, tags="タグ",
        )
        filepath.write_text(content, encoding="utf-8")
        print(f"record: 新規ページ作成 -> {filepath}")
        if _is_layout_task(task_id) and bookshelf_path and bookshelf_path.exists():
            print(f"  デザイン設計書: {bookshelf_path}")


def run_merge(task_id: str, changed: list[str], new_file: str) -> None:
    """FIX セクションマージを実行する。"""
    _check_project()
    original_id = _get_original_id(task_id)
    section = task_id.split("-")[0].lower()
    original_path = FEATURES_DIR / section / _get_filename(original_id)

    if not original_path.exists():
        print(f"エラー: 元ページ {original_path} が見つかりません。", file=sys.stderr)
        sys.exit(1)

    new_path = Path(new_file)
    if not new_path.exists():
        print(f"エラー: {new_file} が見つかりません。", file=sys.stderr)
        sys.exit(1)

    old_content = original_path.read_text(encoding="utf-8")
    new_content = new_path.read_text(encoding="utf-8")

    # parse_sections から辞書に変換
    new_secs = {}
    for sec in parse_sections(new_content):
        new_secs[sec["title"]] = sec["content"]

    merge_target = {}
    for name in changed:
        if name in new_secs:
            merge_target[name] = new_secs[name]
        else:
            print(f"警告: セクション '{name}' が見つかりません。スキップ。", file=sys.stderr)

    if not merge_target:
        print("エラー: マージ対象のセクションがありません。", file=sys.stderr)
        sys.exit(1)

    merged = _merge_sections(old_content, merge_target)
    original_path.write_text(merged, encoding="utf-8")
    print(f"record: マージ完了 -> {original_path}")
    print(f"  変更: {', '.join(merge_target.keys())}")


# --- TP ステータス更新 ---


def update_status(task_id: str) -> None:
    """TP ページのタスクステータスを「完了」に更新する。"""
    _check_project()
    section_dir = find_section_dir(task_id, DESIGN_DIR)

    if not section_dir:
        print(f"エラー: セクションディレクトリが見つかりません ({task_id})。", file=sys.stderr)
        sys.exit(1)

    for tp_file in section_dir.glob(TP_FILE_PATTERN):
        try:
            content = tp_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        if task_id not in content:
            continue

        lines = content.splitlines()
        updated = False
        new_lines = []
        for line in lines:
            if task_id in line and "|" in line:
                line = re.sub(rf"{STATUS_TODO}|{STATUS_WIP}", STATUS_DONE, line)
                updated = True
            new_lines.append(line)

        if updated:
            tp_file.write_text("\n".join(new_lines), encoding="utf-8")
            print(f"record: {task_id} のステータスを「完了」に更新 -> {tp_file}")
            return

    print(f"警告: {task_id} が TP ページ内に見つかりません。", file=sys.stderr)


# --- ユーザーガイド ---


def _guide_dir() -> Path:
    """ユーザーガイドディレクトリ (.ui-specs/)。"""
    return UI_SPECS_DIR


def guide_prepare(section: str) -> None:
    """ガイドファイルのパスを返す (なければディレクトリを作成)。"""
    _check_project()
    d = _guide_dir()
    d.mkdir(parents=True, exist_ok=True)
    filepath = d / f"{section.lower()}.md"
    print(f"record: guide -> {filepath}")


def guide_update_index(section: str) -> None:
    """全ガイドファイルをスキャンして index.md を再生成する。"""
    _check_project()
    d = _guide_dir()
    if not d.exists():
        return

    sections = []
    for md_file in sorted(d.glob("*.md")):
        if md_file.name == INDEX_MD_FILENAME:
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        title = md_file.stem
        for line in content.splitlines():
            if line.strip().startswith("# "):
                title = line.strip()[2:].strip()
                break
        sections.append({"title": title, "filename": md_file.name})

    lines = ["# 機能ガイド", ""]
    if sections:
        lines.append("| 機能 | ファイル |")
        lines.append("|---|---|")
        for sec in sections:
            lines.append(f"| [{sec['title']}]({sec['filename']}) | {sec['filename']} |")
    else:
        lines.append("(まだ機能ガイドはありません)")
    lines.append("")

    index_path = d / INDEX_MD_FILENAME
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"record: {INDEX_MD_FILENAME} 更新 - {len(sections)} セクション -> {index_path}")


# --- メイン ---


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python core/record.py TASK-ID [merge|status|guide|guide_index] ...", file=sys.stderr)
        sys.exit(1)

    task_id = sys.argv[1].upper()

    if len(sys.argv) < 3:
        # デフォルト: 新規作成 / FIX 準備
        create_record(task_id)
        return

    action = sys.argv[2]

    if action == "merge":
        changed = []
        new_file = None
        i = 3
        while i < len(sys.argv):
            if sys.argv[i] == "--changed" and i + 1 < len(sys.argv):
                changed = [s.strip() for s in sys.argv[i + 1].split(",") if s.strip()]
                i += 2
            elif sys.argv[i] == "--file" and i + 1 < len(sys.argv):
                new_file = sys.argv[i + 1]
                i += 2
            else:
                i += 1
        if not changed or not new_file:
            print("usage: ... merge --changed SEC1,SEC2 --file PATH", file=sys.stderr)
            sys.exit(1)
        run_merge(task_id, changed, new_file)

    elif action == "status":
        update_status(task_id)

    elif action == "guide":
        if len(sys.argv) < 4:
            print("usage: ... guide SECTION", file=sys.stderr)
            sys.exit(1)
        guide_prepare(sys.argv[3])

    elif action == "guide_index":
        if len(sys.argv) < 4:
            print("usage: ... guide_index SECTION", file=sys.stderr)
            sys.exit(1)
        guide_update_index(sys.argv[3])

    else:
        print(f"エラー: 不明なアクション '{action}'", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
