#!/usr/bin/env python3
"""update.py — .nxt-core/ を giget 経由で最新版に更新する

スタンドアロン (標準ライブラリのみ、core/ 非依存)。プル子・プタ子の
プロジェクトルートに配布される `.nxt-core/update.py` から実行する。

使い方:
    cd <プロジェクトルート>
    python .nxt-core/update.py

フロー:
    1. npx giget で `.nxt-core-new-<ts>/` に最新版を取得
    2. 配布対象外 (CLAUDE.md / .libs/ / .claude/ / bootstrap.py 等) を cleanup
    3. 取得物の sanity check (主要ファイルが揃っているか)
    4. 現 `.nxt-core/` を `.nxt-core-old-<ts>/` にリネーム (退避)
    5. 新 `.nxt-core-new-<ts>/` を `.nxt-core/` にリネーム (反映)
    6. install.py --update を呼んで `.claude/` 側を再同期
    7. 成功時: 退避した `.nxt-core-old-<ts>/` を削除
    8. 失敗時: rollback (新規取得分を削除、退避ディレクトリを `.nxt-core/` に戻す)

設計の意図:
    install.py --update は `.claude/` 配下 (Hook / skills / settings)
    のみを管理し、`.nxt-core/` 自体は触らない設計。本元での修正を
    各プロジェクトに届けるには `.nxt-core/` の取り直しが別途必要。
    本スクリプトはその空白を埋める。
"""

import io
import shutil
import subprocess
import sys
from datetime import datetime
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
# bootstrap.py と同じ値を持つ箇所は意図的に二重定義 (giget 取得前に動く必要があるため)。

NXT_CORE_DIR_NAME = ".nxt-core"
GITHUB_REPO = "q7ry2c2t4v-spec/erqo-next"
INSTALL_SCRIPT_REL = "core/install.py"
# 取得物の sanity check に使うマーカーファイル群。
# これらが揃っていれば「最低限 .nxt-core/ として機能する」と判定する。
FETCHED_MARKER_FILES = (
    "core/paths.py",
    "core/install.py",
    "core/constants.py",
    "VERSION",
)
# 配布対象ホワイトリスト (bootstrap.py の DIST_DIRS / DIST_FILES と一致)。
# giget は .gigetignore を尊重しないため、取得後にこれら以外を削除する。
DIST_DIRS = ("specs", "core", "skills", "stacks")
DIST_FILES = ("VERSION", "update.py")


# --- ヘルパー ---


def _find_command(name: str) -> str:
    """コマンドを PATH から検索する。見つからなければエラー終了。"""
    cmd = shutil.which(name)
    if not cmd:
        print(f"エラー: {name} が見つかりません。", file=sys.stderr)
        sys.exit(1)
    return cmd


def _read_version(nxt_dir: Path) -> str:
    """`.nxt-core/VERSION` を読む。読めなければ 'unknown'。"""
    version_file = nxt_dir / "VERSION"
    if not version_file.exists():
        return "unknown"
    try:
        return version_file.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeDecodeError):
        return "unknown"


def _fetch_new_core(project_root: Path, dst: Path) -> None:
    """giget で GitHub から最新版を取得して `dst` に展開する。"""
    npx = _find_command("npx")
    print(f"  取得: gh:{GITHUB_REPO} -> {dst.name}/")
    sys.stdout.flush()
    subprocess.run(
        [npx, "giget", f"gh:{GITHUB_REPO}", dst.name],
        cwd=str(project_root),
        check=True,
    )


def _cleanup_giget_artifacts(nxt_dir: Path) -> None:
    """giget で取得した `.nxt-core/` から本元固有ファイル/ディレクトリを削除する。

    giget はリポジトリ全体を取得するため、本元の `CLAUDE.md` / `.libs/` /
    `.claude/` / `bootstrap.py` / `release.sh` / `.gitignore` / `.gigetignore` 等が
    `.nxt-core/` 配下に混入する。`.nxt-core/CLAUDE.md` が残ると
    `core/paths.py:find_project_root()` が `IS_SOURCE=True` と誤判定して
    後続の `install.py --update` が止まるため、ホワイトリスト外を明示的に削除する。
    """
    allowed = set(DIST_DIRS) | set(DIST_FILES)
    removed: list[str] = []
    for entry in nxt_dir.iterdir():
        if entry.name in allowed:
            continue
        if entry.is_dir():
            shutil.rmtree(entry, ignore_errors=True)
        else:
            try:
                entry.unlink()
            except OSError:
                continue
        removed.append(entry.name)
    if removed:
        print(f"  giget 取得物の cleanup: {len(removed)} エントリ削除 ({', '.join(sorted(removed))})")


def _verify_fetched_core(new_dir: Path) -> bool:
    """取得物の sanity check (主要ファイルが揃っているか)。"""
    missing = [m for m in FETCHED_MARKER_FILES if not (new_dir / m).exists()]
    if missing:
        print(
            f"エラー: 取得物に必要なファイルが欠けています: {', '.join(missing)}",
            file=sys.stderr,
        )
        return False
    return True


def _swap_in_new_core(nxt_dir: Path, new_dir: Path, old_dir: Path) -> None:
    """`.nxt-core/` を `old_dir` に退避してから `new_dir` を `.nxt-core/` に昇格する。

    途中で失敗した場合は呼び出し元側で rollback する。
    """
    nxt_dir.rename(old_dir)
    try:
        new_dir.rename(nxt_dir)
    except OSError:
        # 新版への切替に失敗 → 退避した旧版を戻す
        if nxt_dir.exists():
            shutil.rmtree(nxt_dir, ignore_errors=True)
        old_dir.rename(nxt_dir)
        raise


def _run_install_update(nxt_dir: Path, project_root: Path) -> int:
    """`install.py --update` を子プロセスで実行する。終了コードを返す。"""
    install_py = nxt_dir / INSTALL_SCRIPT_REL
    if not install_py.exists():
        print(
            f"警告: {install_py.relative_to(project_root)} が見つかりません。"
            "スキル同期をスキップします。",
            file=sys.stderr,
        )
        return 0
    return subprocess.run(
        [sys.executable, str(install_py), "--update"],
        cwd=str(project_root),
    ).returncode


# --- メイン ---


def main() -> None:
    project_root = Path.cwd().resolve()
    nxt_dir = project_root / NXT_CORE_DIR_NAME

    if not nxt_dir.exists():
        print(
            f"エラー: {NXT_CORE_DIR_NAME}/ が見つかりません。\n"
            "  既存プル子/プタ子のプロジェクトルートで実行してください。\n"
            "  新規セットアップなら bootstrap.py を使ってください。",
            file=sys.stderr,
        )
        sys.exit(1)

    old_version = _read_version(nxt_dir)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    new_dir = project_root / f"{NXT_CORE_DIR_NAME}-new-{timestamp}"
    old_dir = project_root / f"{NXT_CORE_DIR_NAME}-old-{timestamp}"

    print(f"erqo-next update: {project_root.name}")
    print(f"  現バージョン: {old_version}")
    print()

    # 1. giget で `.nxt-core-new-<ts>/` に取得
    try:
        if new_dir.exists():
            shutil.rmtree(new_dir)
        _fetch_new_core(project_root, new_dir)
    except subprocess.CalledProcessError as exc:
        print(f"エラー: giget が失敗しました (exit {exc.returncode})", file=sys.stderr)
        if new_dir.exists():
            shutil.rmtree(new_dir, ignore_errors=True)
        sys.exit(1)

    # 2. giget 取得物から本元固有ファイルを削除
    _cleanup_giget_artifacts(new_dir)

    # 3. sanity check
    if not _verify_fetched_core(new_dir):
        shutil.rmtree(new_dir, ignore_errors=True)
        sys.exit(1)

    new_version = _read_version(new_dir)
    print(f"  新バージョン: {new_version}")
    print()

    # 4. 退避 + 切替
    try:
        _swap_in_new_core(nxt_dir, new_dir, old_dir)
    except OSError as exc:
        print(
            f"エラー: {NXT_CORE_DIR_NAME}/ の切替に失敗しました: {exc}",
            file=sys.stderr,
        )
        # _swap_in_new_core が rollback 済み。残骸の new_dir だけ片付ける
        if new_dir.exists():
            shutil.rmtree(new_dir, ignore_errors=True)
        sys.exit(1)

    print(f"  {NXT_CORE_DIR_NAME}/: 取り替え完了 ({old_version} -> {new_version})")
    print()

    # 5. install.py --update で .claude/ 側を再同期
    install_rc = _run_install_update(nxt_dir, project_root)
    if install_rc != 0:
        print(
            f"警告: install.py --update が失敗しました (exit {install_rc})。\n"
            f"  {NXT_CORE_DIR_NAME}/ 自体の更新は成功しています。\n"
            f"  退避した旧版は {old_dir.name}/ に残しています (内容確認後に手動削除可)。",
            file=sys.stderr,
        )
        sys.exit(install_rc)

    # 6. 旧版を削除
    print()
    shutil.rmtree(old_dir, ignore_errors=True)
    print(f"  {old_dir.name}/: 削除完了")
    print()
    print(f"update 完了! ({old_version} -> {new_version})")


if __name__ == "__main__":
    main()
