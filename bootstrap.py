#!/usr/bin/env python3
"""bootstrap.py — erqo-next プロジェクト初期化ブートストラップ

プロジェクトディレクトリで実行するだけでプル子をインストールする。
Next.js + Playwright + Storybook のスターターテンプレート付き。
スタンドアロン (標準ライブラリのみ、core/ に依存しない)。

使い方:
    cd <プロジェクトディレクトリ>
    python /path/to/erqo-next/bootstrap.py
"""

import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

# --- Windows UTF-8 出力 ---
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8",
                                  line_buffering=True)
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8",
                                  line_buffering=True)

# --- 定数 ---
# スタンドアロンスクリプトのため core/constants.py には依存しない。
# 以下はこのモジュール内でのみ使用する固有定数。

NXT_CORE_DIR_NAME = ".nxt-core"
STACKS_DIR_NAME = "stacks"
NEXTJS_VARIANT_DIR_NAME = "nextjs"
STARTER_DIR_NAME = "starter"
# 配布ディレクトリ: stacks/ が入るので docs/ を外した
# (docs は stacks/nextjs/docs/ に移動済み、stacks/ 経由で届く)
DIST_DIRS = ("specs", "core", "skills", STACKS_DIR_NAME)
DIST_FILES = ("VERSION",)
SOURCE_MARKER_FILES = ("core/paths.py", "core/constants.py", "core/install.py")
GITHUB_REPO = "q7ry2c2t4v-spec/erqo-next"
INSTALL_SCRIPT_REL = "core/install.py"


def _nextjs_starter_rel() -> Path:
    """Next.js スターターのソース相対パス (ソースルート or NXT_CORE_DIR_NAME 基点)。"""
    return Path(STACKS_DIR_NAME) / NEXTJS_VARIANT_DIR_NAME / STARTER_DIR_NAME


# --- 関数 ---


def detect_source() -> Path | None:
    """スクリプト自身の場所からソースリポジトリを自動検出する。"""
    script_dir = Path(__file__).resolve().parent
    if all((script_dir / m).exists() for m in SOURCE_MARKER_FILES):
        return script_dir
    return None


def find_command(name: str) -> str:
    """コマンドを PATH から検索する。見つからなければエラー終了。"""
    cmd = shutil.which(name)
    if not cmd:
        print(f"エラー: {name} が見つかりません。", file=sys.stderr)
        sys.exit(1)
    return cmd


def init_git(project_root: Path) -> None:
    """git リポジトリを初期化する (まだでなければ)。"""
    if (project_root / ".git").exists():
        print("  git: リポジトリ検出済み")
        return
    subprocess.run(
        ["git", "init"], cwd=str(project_root), check=True, capture_output=True,
    )
    print("  git: リポジトリを初期化しました")


def copy_starter(project_root: Path, starter_src: Path) -> None:
    """スターターテンプレートをプロジェクトルートにコピーする。"""
    if not starter_src.exists():
        print("  スターター: テンプレートなし (スキップ)")
        return
    shutil.copytree(
        starter_src, project_root,
        ignore=shutil.ignore_patterns("__pycache__"),
        dirs_exist_ok=True,
    )
    print("  スターター: テンプレートをコピーしました")


def copy_nxt_core(project_root: Path, source: Path) -> None:
    """ソースから .nxt-core/ にコアモジュールをコピーする。"""
    nxt_dir = project_root / NXT_CORE_DIR_NAME
    if nxt_dir.exists():
        shutil.rmtree(nxt_dir)
    nxt_dir.mkdir()

    for d in DIST_DIRS:
        src = source / d
        if src.exists():
            shutil.copytree(
                src, nxt_dir / d, ignore=shutil.ignore_patterns("__pycache__"),
            )

    for f in DIST_FILES:
        src = source / f
        if src.exists():
            shutil.copy2(src, nxt_dir / f)

    print(f"  コア: {NXT_CORE_DIR_NAME}/ にコピーしました")


def fetch_from_github(project_root: Path) -> None:
    """giget で GitHub から取得し、starter と core を分離配置する。"""
    npx = find_command("npx")

    nxt_dir = project_root / NXT_CORE_DIR_NAME
    if nxt_dir.exists():
        shutil.rmtree(nxt_dir)

    print(f"  取得: gh:{GITHUB_REPO}")
    sys.stdout.flush()
    subprocess.run(
        [npx, "giget", f"gh:{GITHUB_REPO}", NXT_CORE_DIR_NAME],
        cwd=str(project_root),
        check=True,
    )

    # stacks/nextjs/starter/ を .nxt-core/ 配下からプロジェクトルートに移動
    starter_in_nxt = nxt_dir / _nextjs_starter_rel()
    if starter_in_nxt.exists():
        shutil.copytree(starter_in_nxt, project_root, dirs_exist_ok=True)
        shutil.rmtree(starter_in_nxt)

    print("  スターター + コア: 配置完了")


def update_package_name(project_root: Path) -> None:
    """package.json のプロジェクト名をディレクトリ名に更新する。"""
    pkg_path = project_root / "package.json"
    if not pkg_path.exists():
        return
    try:
        data = json.loads(pkg_path.read_text(encoding="utf-8"))
        data["name"] = project_root.name.lower().replace(" ", "-")
        pkg_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    except (json.JSONDecodeError, OSError):
        pass


def run_install(project_root: Path) -> None:
    """install.py を実行する。"""
    install_py = project_root / NXT_CORE_DIR_NAME / INSTALL_SCRIPT_REL
    if not install_py.exists():
        print(f"エラー: {install_py} が見つかりません", file=sys.stderr)
        sys.exit(1)
    sys.stdout.flush()
    subprocess.run(
        [sys.executable, str(install_py)],
        cwd=str(project_root),
        check=True,
    )


def install_dependencies(project_root: Path) -> None:
    """npm install で依存パッケージをインストールする。"""
    pkg_path = project_root / "package.json"
    if not pkg_path.exists():
        print("  npm: package.json なし (スキップ)")
        return
    npm = find_command("npm")
    print("  npm: 依存パッケージをインストール中...")
    sys.stdout.flush()
    subprocess.run(
        [npm, "install"],
        cwd=str(project_root),
        check=True,
    )
    print("  npm: インストール完了")


def install_playwright(project_root: Path) -> None:
    """Playwright のブラウザバイナリをインストールする。"""
    npx = find_command("npx")
    print("  Playwright: ブラウザをインストール中...")
    sys.stdout.flush()
    subprocess.run(
        [npx, "playwright", "install", "--with-deps"],
        cwd=str(project_root),
        check=True,
    )
    print("  Playwright: インストール完了")


# --- メイン ---


def main() -> None:
    project_root = Path.cwd().resolve()
    source = detect_source()

    # ソースリポジトリ自身への誤インストール防止
    if source and project_root == source:
        print(
            "エラー: ソースリポジトリ内では実行できません。\n"
            "プロジェクトディレクトリに移動してから実行してください。",
            file=sys.stderr,
        )
        sys.exit(1)

    print(f"erqo-next ブートストラップ: {project_root.name}")
    print()

    # 1. スターターテンプレート + コアモジュール配置
    if source:
        print(f"ソース検出: {source}")
        copy_starter(project_root, source / _nextjs_starter_rel())
        copy_nxt_core(project_root, source)
    else:
        fetch_from_github(project_root)

    # 2. package.json のプロジェクト名更新
    update_package_name(project_root)

    # 3. git 初期化
    init_git(project_root)

    print()

    # 4. install.py 実行 (CLAUDE.md, Hook, スキル, QA 設定)
    run_install(project_root)

    print()

    # 5. npm install
    install_dependencies(project_root)

    print()

    # 6. Playwright ブラウザ取得
    install_playwright(project_root)

    print("\nセットアップ完了!")
    print("新しい Claude Code セッションを開始して /dsgn で設計フェーズを始めてください。")


if __name__ == "__main__":
    main()
