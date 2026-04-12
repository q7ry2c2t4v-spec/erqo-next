"""docs.py — デザインリファレンス検索モジュール

docs/ 配下のデザインリファレンス（Apple HIG, shadcn, tailwind, m3 等）を検索する。
検索先は paths.DOCS_DIR (= NXT_ROOT / "docs") で、layo.py から呼ばれる。

サブコマンド:
  python core/docs.py search card spacing    # キーワード検索
  python core/docs.py list [category]        # カテゴリ一覧 / ファイル一覧
  python core/docs.py show category path     # ファイル表示
"""

import sys
from pathlib import Path

from paths import DOCS_DIR

# キーワードエイリアス（簡易的な同義語展開）
KEYWORD_ALIASES = {
    "card": ["cards"],
    "button": ["buttons", "btn"],
    "dialog": ["modal", "modals", "dialogs"],
    "nav": ["navigation", "navbar"],
    "color": ["colours", "colors"],
    "space": ["spacing", "gap"],
    "font": ["typography", "text"],
    "grid": ["layout"],
    "icon": ["icons"],
    "input": ["inputs", "field", "fields"],
    "tab": ["tabs"],
    "menu": ["menus", "dropdown"],
    "toast": ["notification", "snackbar"],
    "table": ["tables", "data-table"],
}


def _docs_dir() -> Path | None:
    if DOCS_DIR and DOCS_DIR.exists():
        return DOCS_DIR
    return None


def _categories() -> list[str]:
    """カテゴリ一覧（docs/ 直下のフォルダ名）。"""
    d = _docs_dir()
    if not d:
        return []
    return sorted([p.name for p in d.iterdir() if p.is_dir()])


def _expand_keywords(keywords: list[str]) -> list[str]:
    """キーワードをエイリアスで展開する。"""
    expanded = set(kw.lower() for kw in keywords)
    for kw in keywords:
        kw_lower = kw.lower()
        # 正方向: kw がキーなら値を追加
        if kw_lower in KEYWORD_ALIASES:
            expanded.update(KEYWORD_ALIASES[kw_lower])
        # 逆方向: kw が値に含まれていればキーと他の値を追加
        for canonical, aliases in KEYWORD_ALIASES.items():
            if kw_lower in [a.lower() for a in aliases]:
                expanded.add(canonical)
                expanded.update(a.lower() for a in aliases)
    return list(expanded)


def search(keywords: list[str], max_results: int = 20) -> list[dict]:
    """キーワード検索。スコア順に結果を返す。"""
    d = _docs_dir()
    if not d:
        return []

    expanded = _expand_keywords(keywords)
    results = []

    for md in d.rglob("*.md"):
        rel = md.relative_to(d)
        rel_str = str(rel).replace("\\", "/").lower()
        name_lower = md.stem.lower()

        score = 0.0
        for kw in expanded:
            if kw == name_lower:
                score += 3.0  # ファイル名完全一致
            elif kw in name_lower:
                score += 2.0  # ファイル名部分一致
            elif kw in rel_str:
                score += 1.0  # パス含む

        if score > 0:
            category = rel.parts[0] if len(rel.parts) > 1 else ""
            results.append({
                "score": score,
                "category": category,
                "path": str(rel).replace("\\", "/"),
                "name": md.stem,
            })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:max_results]


def list_docs(category: str | None = None) -> list[str]:
    """カテゴリ一覧、またはカテゴリ内ファイル一覧。"""
    d = _docs_dir()
    if not d:
        return []

    if category is None:
        return _categories()

    cat_dir = d / category
    if not cat_dir.exists():
        return []
    return sorted(
        str(p.relative_to(cat_dir)).replace("\\", "/")
        for p in cat_dir.rglob("*.md")
    )


def show(category: str, path: str) -> str | None:
    """指定ファイルの内容を返す。"""
    d = _docs_dir()
    if not d:
        return None
    target = d / category / path
    if not target.exists():
        return None
    return target.read_text(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("usage: python core/docs.py <search|list|show> [args...]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "search":
        if len(sys.argv) < 3:
            print("usage: python core/docs.py search KW1 [KW2 ...]")
            sys.exit(1)
        results = search(sys.argv[2:])
        for r in results:
            print(f"  [{r['score']:5.1f}] [{r['category']}] {r['path']}")
        if not results:
            print("  (no results)")

    elif cmd == "list":
        cat = sys.argv[2] if len(sys.argv) > 2 else None
        items = list_docs(cat)
        for item in items:
            print(f"  {item}")
        if not items:
            print("  (empty)" if cat else "  (no categories found)")

    elif cmd == "show":
        if len(sys.argv) != 4:
            print("usage: python core/docs.py show CATEGORY PATH")
            sys.exit(1)
        content = show(sys.argv[2], sys.argv[3])
        if content is None:
            print("error: file not found", file=sys.stderr)
            sys.exit(1)
        print(content)

    else:
        print(f"unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
