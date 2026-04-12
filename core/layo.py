"""layo.py — /layo レイアウトデザイン策定オーケストレーター

input.md の内容 + docs 検索 + コーディングルール + 関連ページ収集 +
プロジェクトルールをまとめて stdout に出力する。
SKILL.md のステップ 1 と 5 で呼ばれる。

使い方:
    python core/layo.py TASK-ID
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

from paths import LIBS_DIR, DOCS_DIR, RULES_DIR, SPECS_CODING_DIR, IS_SOURCE
from constants import (
    STORYBOOK_SHELF_NAME,
    STORYBOOK_INPUT_FILENAME,
    RECON_REFERENCE_SECTION_SUFFIX,
    RECON_REQUEST_SECTION_SUFFIX,
    CODING_L3_NEXTJS_FILENAME,
)
from page_parser import parse_sections
from index import collect as index_collect
from docs import search as docs_search
from load import collect_rules
from feedback import init_error_handling

init_error_handling()


# --- ヘルパー ---


def _task_slug(task_id: str) -> str:
    """タスク ID をスラグ化する (clone.py と同一ロジック)。"""
    return task_id.lower()


def _storybook_dir(task_id: str) -> Path | None:
    """本棚ディレクトリのパス。"""
    if LIBS_DIR is None:
        return None
    return LIBS_DIR / STORYBOOK_SHELF_NAME / _task_slug(task_id)


def _storybook_page_path(task_id: str) -> Path | None:
    """本棚正本ページのパス。"""
    d = _storybook_dir(task_id)
    if d is None:
        return None
    slug = _task_slug(task_id)
    return d / f"{slug}.md"


def _input_path(task_id: str) -> Path | None:
    """input.md のパス。"""
    d = _storybook_dir(task_id)
    if d is None:
        return None
    return d / STORYBOOK_INPUT_FILENAME


def _determine_mode(task_id: str) -> str:
    """本棚ページの存在で新規/更新を機械判定する。"""
    page = _storybook_page_path(task_id)
    if page and page.exists():
        return "update"
    return "new"


def _extract_keywords_from_input(content: str) -> list[str]:
    """input.md から docs 検索用キーワードを機械抽出する。

    2 つのソースから抽出:
    1. 参考 URL のドメイン名 (例: stripe.com → stripe)
    2. 要望セクションの英単語 (3 文字以上)
    """
    keywords: list[str] = []

    for sec in parse_sections(content):
        sid = sec.get("id", "")

        # URL → ドメインキーワード
        if sid.endswith(RECON_REFERENCE_SECTION_SUFFIX):
            for line in sec["content"].split("\n"):
                m = re.match(r"^\s*[-*]\s+https?://(?:www\.)?([^/\s]+)", line)
                if m:
                    name = m.group(1).split(".")[0]
                    if len(name) >= 3:
                        keywords.append(name)

        # 要望テキスト → 英単語
        if sid.endswith(RECON_REQUEST_SECTION_SUFFIX):
            for word in re.findall(r"[a-zA-Z]{3,}", sec["content"]):
                keywords.append(word.lower())

    return list(set(keywords))


def _coding_rule_paths() -> list[str]:
    """レイアウトタスクに常時適用するコーディングルールのパスを返す。"""
    paths = []
    l3 = SPECS_CODING_DIR / CODING_L3_NEXTJS_FILENAME
    if l3.exists():
        paths.append(f"{l3}  §1 デザイン値トークン化 (Tailwind v4 @theme)")
    return paths


# --- メイン ---


def load_layo(task_id: str) -> str:
    """タスク ID から /layo 用コンテキストを収集して返す。"""
    if IS_SOURCE:
        return "エラー: 本体リポジトリでは /layo を実行できません。"

    if not LIBS_DIR or not LIBS_DIR.exists():
        return "エラー: .libs/ が見つかりません。install.py を実行してください。"

    parts: list[str] = []

    # --- 1. モード判定 ---
    mode = _determine_mode(task_id)
    mode_label = "更新 (本棚ページあり)" if mode == "update" else "新規 (本棚ページなし)"
    parts.append(f"## モード: {mode_label}")

    # --- 2. input.md ---
    input_file = _input_path(task_id)
    input_content = ""
    if input_file and input_file.exists():
        try:
            input_content = input_file.read_text(encoding="utf-8")
            parts.append(f"## 取材入力\n\n{input_content}")
        except (OSError, UnicodeDecodeError):
            parts.append("## 取材入力\n\n(読み込みエラー)")
    else:
        parts.append("## 取材入力\n\n(input.md 未作成 — ステップ 2 で対話から作成)")

    # --- 3. キーワード抽出 ---
    keywords = _extract_keywords_from_input(input_content) if input_content else []
    if keywords:
        parts.append(f"## 抽出キーワード\n\n{', '.join(keywords)}")

    # --- 4. デザインリファレンス検索 ---
    if keywords and DOCS_DIR.exists():
        doc_results = docs_search(keywords, max_results=10)
        if doc_results:
            doc_lines = [
                f"- `{r['path']}` (score: {r['score']:.1f})"
                for r in doc_results
            ]
            parts.append(
                "## 関連デザインリファレンス\n\n"
                "以下のドキュメントを Read してデザイン判断に活用すること:\n\n"
                + "\n".join(doc_lines)
            )
        else:
            parts.append("## 関連デザインリファレンス\n\n(該当なし)")
    elif not DOCS_DIR.exists():
        parts.append("## 関連デザインリファレンス\n\n(docs/ が見つかりません)")

    # --- 5. コーディングルール参照 ---
    rule_paths = _coding_rule_paths()
    if rule_paths:
        rule_lines = [f"- `{p}`" for p in rule_paths]
        parts.append(
            "## コーディングルール (デザイン関連)\n\n"
            "以下のルールファイルを Read してトークン設計に反映すること:\n\n"
            + "\n".join(rule_lines)
        )

    # --- 6. プロジェクトルール ---
    if RULES_DIR and RULES_DIR.exists():
        rules_content = collect_rules(RULES_DIR, ["layout", "ui", "all"])
        if rules_content:
            parts.append(f"## プロジェクトルール\n\n{rules_content}")

    # --- 7. 関連ページ ---
    if keywords:
        related = index_collect(keywords)
        if related:
            related_lines = []
            for r in related[:10]:
                path = LIBS_DIR / r["path"] if r.get("path") else None
                if path and path.exists():
                    try:
                        related_lines.append(path.read_text(encoding="utf-8"))
                    except (OSError, UnicodeDecodeError):
                        pass
            if related_lines:
                parts.append(
                    f"## 関連ページ\n\n" + "\n---\n".join(related_lines)
                )

    # --- 8. 現在の本棚ページ (更新モード) ---
    if mode == "update":
        page = _storybook_page_path(task_id)
        if page and page.exists():
            try:
                page_content = page.read_text(encoding="utf-8")
                parts.append(f"## 現在の本棚ページ\n\n{page_content}")
            except (OSError, UnicodeDecodeError):
                parts.append("## 現在の本棚ページ\n\n(読み込みエラー)")

    return "\n\n---\n\n".join(parts)


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: python core/layo.py TASK-ID", file=sys.stderr)
        sys.exit(1)

    task_id = sys.argv[1].upper()
    print(load_layo(task_id))


if __name__ == "__main__":
    main()
