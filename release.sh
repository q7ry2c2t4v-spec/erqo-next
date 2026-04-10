#!/usr/bin/env bash
# release.sh — erqo-next リリーススクリプト
#
# 使い方:
#   bash release.sh v1.0.0
#
# フロー:
#   1. VERSION ファイルを更新
#   2. 配布対象の必須ファイルを検証
#   3. git commit + tag
#   4. GitHub Releases にアーカイブをアップロード

set -euo pipefail

# --- 引数チェック ---

if [ $# -lt 1 ]; then
  echo "usage: bash release.sh <version>"
  echo "  例: bash release.sh v1.0.0"
  exit 1
fi

VERSION_TAG="$1"
VERSION_NUM="${VERSION_TAG#v}"  # v1.0.0 → 1.0.0

# セマンティックバージョニングの簡易チェック
if ! echo "$VERSION_NUM" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
  echo "エラー: バージョンは vX.Y.Z 形式で指定してください (例: v1.0.0)"
  exit 1
fi

# --- ディレクトリ検出 ---

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
NXT_ROOT="$SCRIPT_DIR"

echo "=== erqo-next release $VERSION_TAG ==="
echo ""

# --- 1. VERSION ファイル更新 ---

echo "1/4 VERSION 更新: $VERSION_NUM"
echo "$VERSION_NUM" > "$NXT_ROOT/VERSION"

# --- 2. 必須ファイル検証 ---

echo "2/4 必須ファイル検証..."

ERRORS=0

# core/ モジュール
CORE_FILES=(
  "core/paths.py"
  "core/feedback.py"
  "core/page_parser.py"
  "core/index.py"
  "core/docs.py"
  "core/install.py"
  "core/session.py"
  "core/state.py"
  "core/load.py"
  "core/record.py"
)

for f in "${CORE_FILES[@]}"; do
  if [ ! -f "$NXT_ROOT/$f" ]; then
    echo "  NG: $f が見つかりません"
    ERRORS=$((ERRORS + 1))
  fi
done

# specs/ (00-05)
for i in $(seq 0 5); do
  pattern="$NXT_ROOT/specs/0${i}-*.md"
  if ! ls $pattern 1>/dev/null 2>&1; then
    echo "  NG: specs/0${i}-*.md が見つかりません"
    ERRORS=$((ERRORS + 1))
  fi
done

# skills/ (SKILL.md を持つフォルダが1つ以上)
SKILL_COUNT=$(find "$NXT_ROOT/skills" -name "SKILL.md" 2>/dev/null | wc -l)
if [ "$SKILL_COUNT" -lt 1 ]; then
  echo "  NG: skills/ に SKILL.md を持つフォルダがありません"
  ERRORS=$((ERRORS + 1))
fi

# VERSION ファイル
if [ ! -f "$NXT_ROOT/VERSION" ]; then
  echo "  NG: VERSION ファイルが見つかりません"
  ERRORS=$((ERRORS + 1))
fi

if [ "$ERRORS" -gt 0 ]; then
  echo ""
  echo "エラー: $ERRORS 件の問題があります。修正してから再実行してください。"
  exit 1
fi

echo "  OK: 全ファイル確認済み (core: ${#CORE_FILES[@]}, specs: 6, skills: $SKILL_COUNT)"

# --- 3. git commit + tag ---

echo "3/4 git tag $VERSION_TAG..."

cd "$NXT_ROOT"  # リポジトリルートへ
git add -A
git commit -m "release: $VERSION_TAG" || echo "  (変更なし — コミットスキップ)"
git tag -a "$VERSION_TAG" -m "Release $VERSION_TAG"

echo "  タグ作成完了: $VERSION_TAG"

# --- 4. GitHub Releases ---

echo "4/4 GitHub Releases..."

if ! command -v gh &>/dev/null; then
  echo "  警告: gh コマンドが見つかりません。手動で push + release を作成してください:"
  echo "    git push origin main --tags"
  echo "    gh release create $VERSION_TAG --title \"$VERSION_TAG\" --generate-notes"
  exit 0
fi

git push origin main --tags
gh release create "$VERSION_TAG" --title "$VERSION_TAG" --generate-notes

echo ""
echo "=== リリース完了: $VERSION_TAG ==="
