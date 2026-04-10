"""index.py — インデックス管理モジュール（reindex + collect 統合）

サブコマンド:
  python core/index.py reindex              # インデックス再生成
  python core/index.py collect KW1 KW2      # キーワード検索 + 収集
  python core/index.py rename OLD-ID NEW-ID # 識別コードリネーム
"""

import json
import math
import sys
from collections import deque

from page_parser import parse_header
from paths import INDEX_FILE, LIBS_DIR, TAG_ALIASES_FILE


# ---------------------------------------------------------------------------
# reindex
# ---------------------------------------------------------------------------

def reindex() -> dict:
    """LIBS_DIR 配下の全 .md をスキャンしてインデックスを再生成する。"""
    if not LIBS_DIR or not LIBS_DIR.exists():
        print("error: LIBS_DIR not found", file=sys.stderr)
        return {}

    index = {}
    seen_ids: dict[str, str] = {}  # id -> file path (重複検出用)

    for md in sorted(LIBS_DIR.rglob("*.md")):
        if md.name.startswith("_"):
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        header = parse_header(text)
        if not header:
            continue

        page_id = header["id"]
        rel_path = str(md.relative_to(LIBS_DIR)).replace("\\", "/")

        # 重複 ID 検出
        if page_id in seen_ids:
            print(f"warning: duplicate ID '{page_id}' in {rel_path} "
                  f"(first seen in {seen_ids[page_id]})", file=sys.stderr)
        seen_ids[page_id] = rel_path

        # 命名規則チェック（最低3セグメント推奨: CATEGORY-TOPIC-DETAIL）
        segments = page_id.split("-")
        if len(segments) < 2:
            print(f"warning: ID '{page_id}' has fewer than 2 segments", file=sys.stderr)

        stat = md.stat()
        index[page_id] = {
            "path": rel_path,
            "title": header["title"],
            "tags": header["tags"],
            "related": header["related"],
            "updated_at": stat.st_mtime,
        }

    # 保存
    _save_index(index)
    print(f"reindex: {len(index)} pages indexed")
    return index


# ---------------------------------------------------------------------------
# collect
# ---------------------------------------------------------------------------

# スコアリング重み
W_ID = 12.0
W_TITLE_EXACT = 15.0
W_TITLE_PARTIAL = 10.0
W_TAG_EXACT = 8.0
W_TAG_PARTIAL = 5.0
W_BODY_TF = 1.0

# BFS パラメータ
BFS_MAX_DEPTH = 2
BFS_DECAY = 0.5

# 結果制限
SCORE_THRESHOLD = 3.0
MAX_RESULTS = 15

# カバレッジボーナス係数
COVERAGE_BONUS = 0.3


def collect(keywords: list[str]) -> list[dict]:
    """キーワード検索 + 関連ページ収集。"""
    index = _load_index()
    if not index:
        print("error: index is empty — run reindex first", file=sys.stderr)
        return []

    aliases = _load_aliases()
    expanded = _expand_keywords(keywords, aliases)

    # 全エントリをスコアリング
    scored = {}
    for page_id, entry in index.items():
        score, matched_kws = _score_entry(page_id, entry, expanded)
        if score > 0:
            # カバレッジボーナス
            ratio = len(matched_kws) / len(keywords) if keywords else 0
            score *= 1 + COVERAGE_BONUS * ratio
            scored[page_id] = score

    # 閾値フィルタ
    scored = {k: v for k, v in scored.items() if v >= SCORE_THRESHOLD}

    # BFS で関連ページ探索
    link_scores = _bfs_related(scored, index)

    # スコア統合（検索スコアと BFS スコアの max）
    all_ids = set(scored) | set(link_scores)
    merged = {}
    for pid in all_ids:
        merged[pid] = max(scored.get(pid, 0), link_scores.get(pid, 0))

    # ソート + 上限
    results = sorted(merged.items(), key=lambda x: x[1], reverse=True)[:MAX_RESULTS]

    # 出力
    output = []
    for page_id, score in results:
        entry = index.get(page_id, {})
        output.append({
            "id": page_id,
            "score": round(score, 2),
            "path": entry.get("path", ""),
            "title": entry.get("title", ""),
        })
    return output


def _score_entry(page_id: str, entry: dict, expanded_kws: list[str]) -> tuple[float, set]:
    """1エントリのスコアを算出する。"""
    score = 0.0
    matched = set()
    id_lower = page_id.lower()
    title_lower = entry.get("title", "").lower()
    tags_lower = [t.lower() for t in entry.get("tags", [])]

    for kw in expanded_kws:
        kw_lower = kw.lower()
        kw_matched = False

        # ID マッチ
        if kw_lower in id_lower:
            score += W_ID
            kw_matched = True

        # タイトルマッチ
        if kw_lower == title_lower:
            score += W_TITLE_EXACT
            kw_matched = True
        elif kw_lower in title_lower:
            score += W_TITLE_PARTIAL
            kw_matched = True

        # タグマッチ
        for tag in tags_lower:
            if kw_lower == tag:
                score += W_TAG_EXACT
                kw_matched = True
            elif tag.startswith(kw_lower + "/") or tag.startswith(kw_lower):
                # 階層タグのプレフィックスマッチ
                score += W_TAG_PARTIAL
                kw_matched = True

        # 本文スコア（インデックスには本文を含まないため、ファイルから読む）
        if not kw_matched and LIBS_DIR:
            path = LIBS_DIR / entry.get("path", "")
            if path.exists():
                text = path.read_text(encoding="utf-8", errors="replace").lower()
                tf = text.count(kw_lower)
                if tf > 0:
                    score += W_BODY_TF * math.log(1 + tf)
                    kw_matched = True

        if kw_matched:
            matched.add(kw)

    return score, matched


def _bfs_related(seed_scores: dict, index: dict) -> dict:
    """seed からの深度制限 BFS で関連ページスコアを算出する。"""
    link_scores: dict[str, float] = {}
    queue: deque[tuple[str, int, float]] = deque()

    for pid, s in seed_scores.items():
        queue.append((pid, 0, s))

    visited: set[str] = set()

    while queue:
        pid, depth, parent_score = queue.popleft()
        if depth > BFS_MAX_DEPTH:
            continue
        if pid in visited:
            continue
        visited.add(pid)

        entry = index.get(pid)
        if not entry:
            continue

        for rel_id in entry.get("related", []):
            if rel_id not in index:
                continue
            hop_score = parent_score * BFS_DECAY
            if hop_score < SCORE_THRESHOLD:
                continue
            # max を取る（加算しない）
            if rel_id not in link_scores or hop_score > link_scores[rel_id]:
                link_scores[rel_id] = hop_score
            if depth + 1 <= BFS_MAX_DEPTH:
                queue.append((rel_id, depth + 1, hop_score))

    return link_scores


# ---------------------------------------------------------------------------
# rename
# ---------------------------------------------------------------------------

def rename(old_id: str, new_id: str) -> None:
    """識別コードリネーム（ファイル名・見出し・関連リンク・TP 記載を一括更新）。"""
    if not LIBS_DIR or not LIBS_DIR.exists():
        print("error: LIBS_DIR not found", file=sys.stderr)
        return

    count = 0
    for md in LIBS_DIR.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        new_text = text.replace(old_id, new_id)
        if new_text != text:
            md.write_text(new_text, encoding="utf-8")
            count += 1
            print(f"  updated: {md.relative_to(LIBS_DIR)}")

    # ファイル名にIDを含む場合はリネーム
    slug = old_id.lower().replace("-", "_")
    new_slug = new_id.lower().replace("-", "_")
    for md in LIBS_DIR.rglob("*.md"):
        if slug in md.stem:
            new_name = md.name.replace(slug, new_slug)
            new_path = md.parent / new_name
            md.rename(new_path)
            count += 1
            print(f"  renamed: {md.name} -> {new_name}")

    print(f"rename: {old_id} -> {new_id} ({count} files updated)")
    reindex()


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _save_index(index: dict) -> None:
    if INDEX_FILE:
        INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)
        INDEX_FILE.write_text(
            json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
        )


def _load_index() -> dict:
    if INDEX_FILE and INDEX_FILE.exists():
        return json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    return {}


def _load_aliases() -> dict:
    if not TAG_ALIASES_FILE or not TAG_ALIASES_FILE.exists():
        return {}
    return json.loads(TAG_ALIASES_FILE.read_text(encoding="utf-8"))


def _expand_keywords(keywords: list[str], aliases: dict) -> list[str]:
    """キーワードをエイリアスで展開する。"""
    expanded = list(keywords)
    for kw in keywords:
        kw_lower = kw.lower()
        for canonical, alias_list in aliases.items():
            if kw_lower == canonical.lower() or kw_lower in [a.lower() for a in alias_list]:
                expanded.append(canonical)
                expanded.extend(alias_list)
    return list(set(expanded))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("usage: python core/index.py <reindex|collect|rename> [args...]")
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "reindex":
        reindex()
    elif cmd == "collect":
        if len(sys.argv) < 3:
            print("usage: python core/index.py collect KW1 [KW2 ...]")
            sys.exit(1)
        results = collect(sys.argv[2:])
        for r in results:
            print(f"  [{r['score']:6.2f}] {r['id']} - {r['title']}")
        if not results:
            print("  (no results)")
    elif cmd == "rename":
        if len(sys.argv) != 4:
            print("usage: python core/index.py rename OLD-ID NEW-ID")
            sys.exit(1)
        rename(sys.argv[2], sys.argv[3])
    else:
        print(f"unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
