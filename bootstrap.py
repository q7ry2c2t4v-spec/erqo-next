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
GENERIC_VARIANT_DIR_NAME = "generic"
VARIANT_CHOICES = (NEXTJS_VARIANT_DIR_NAME, GENERIC_VARIANT_DIR_NAME)
DEFAULT_VARIANT = NEXTJS_VARIANT_DIR_NAME
VARIANT_ARG_PREFIX = "--variant="
STARTER_DIR_NAME = "starter"
# 配布ディレクトリ: stacks/ が入るので docs/ を外した
# (docs は stacks/nextjs/docs/ に移動済み、stacks/ 経由で届く)
DIST_DIRS = ("specs", "core", "skills", STACKS_DIR_NAME)
DIST_FILES = ("VERSION",)
SOURCE_MARKER_FILES = ("core/paths.py", "core/constants.py", "core/install.py")
GITHUB_REPO = "q7ry2c2t4v-spec/erqo-next"
INSTALL_SCRIPT_REL = "core/install.py"


def _stack_starter_rel(variant: str) -> Path:
    """variant 別スターターのソース相対パス (ソースルート or NXT_CORE_DIR_NAME 基点)。"""
    return Path(STACKS_DIR_NAME) / variant / STARTER_DIR_NAME


def _prompt_variant() -> str:
    """対話で variant を選ばせる。1/2 を nextjs/generic に変換。非対話時は DEFAULT_VARIANT。"""
    print("このプロジェクトの種類を選んでください:")
    print("  1) Next.js プロジェクト (プル子 — 標準、/layo 付き)")
    print("  2) その他のスタック (プタ子 — 最小構成、/layo なし)")
    while True:
        try:
            answer = input("番号を入力 (1/2): ").strip()
        except EOFError:
            print(f"  (非対話モード: {DEFAULT_VARIANT} として登録)")
            return DEFAULT_VARIANT
        if answer == "1":
            return NEXTJS_VARIANT_DIR_NAME
        if answer == "2":
            return GENERIC_VARIANT_DIR_NAME
        print("  エラー: 1 か 2 を入力してください。")


def _parse_variant_arg(argv: list[str]) -> str | None:
    """sys.argv から `--variant=nextjs|generic` を取り出す。

    不正値は sys.exit(2) で終了 (L1.5 責務境界バリデーション)。
    指定なしは None (対話ルートに委ねる)。
    """
    for arg in argv:
        if not arg.startswith(VARIANT_ARG_PREFIX):
            continue
        value = arg[len(VARIANT_ARG_PREFIX):].strip()
        if value not in VARIANT_CHOICES:
            print(
                f"エラー: {VARIANT_ARG_PREFIX} の値は {VARIANT_CHOICES} のいずれか "
                f"(受け取った値: {value!r})",
                file=sys.stderr,
            )
            sys.exit(2)
        return value
    return None


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


def fetch_from_github(project_root: Path, variant: str) -> None:
    """giget で GitHub から取得し、variant 別 starter と core を分離配置する。"""
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

    # stacks/<variant>/starter/ を .nxt-core/ 配下からプロジェクトルートに移動
    starter_in_nxt = nxt_dir / _stack_starter_rel(variant)
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


def run_install(project_root: Path, variant: str) -> None:
    """install.py を --variant=<variant> 付きで実行する (variant 対話を skip)。"""
    install_py = project_root / NXT_CORE_DIR_NAME / INSTALL_SCRIPT_REL
    if not install_py.exists():
        print(f"エラー: {install_py} が見つかりません", file=sys.stderr)
        sys.exit(1)
    sys.stdout.flush()
    subprocess.run(
        [sys.executable, str(install_py), f"{VARIANT_ARG_PREFIX}{variant}"],
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

    # 1. variant 選択 (プル子 nextjs / プタ子 generic)
    #    --variant=XXX があれば対話スキップ、なければ対話で聞く
    forced_variant = _parse_variant_arg(sys.argv[1:])
    variant = forced_variant if forced_variant is not None else _prompt_variant()
    print(f"  variant: {variant}")
    print()

    # 2. スターターテンプレート + コアモジュール配置
    if source:
        print(f"ソース検出: {source}")
        copy_starter(project_root, source / _stack_starter_rel(variant))
        copy_nxt_core(project_root, source)
    else:
        fetch_from_github(project_root, variant)

    # 3. package.json のプロジェクト名更新 (プル子のみ package.json が存在)
    if variant == NEXTJS_VARIANT_DIR_NAME:
        update_package_name(project_root)

    # 4. git 初期化
    init_git(project_root)

    print()

    # 5. install.py 実行 (CLAUDE.md, Hook, スキル, QA 設定, variant.json)
    run_install(project_root, variant)

    print()

    # 6. Next.js 固有の後続処理 (プタ子ではスキップ: スタック依存のセットアップに委ねる)
    if variant == NEXTJS_VARIANT_DIR_NAME:
        install_dependencies(project_root)
        print()
        install_playwright(project_root)

    print("\nセットアップ完了!")
    if variant == NEXTJS_VARIANT_DIR_NAME:
        print("新しい Claude Code セッションを開始して /dsgn で設計フェーズを始めてください。")
    else:
        print(
            "README.md に従ってスタックの初期化を行ってから、\n"
            "新しい Claude Code セッションを開始して /dsgn で設計フェーズを始めてください。"
        )


if __name__ == "__main__":
    main()
