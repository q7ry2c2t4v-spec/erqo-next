"""install.py - プロジェクトセットアップスクリプト

新規インストールとアップデートを兼用する。
プロジェクトルートから実行する。

使い方:
    python .nxt-core/core/install.py            # 新規
    python .nxt-core/core/install.py --update   # 更新
"""

import io
import json
import shutil
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import NXT_ROOT, IS_SOURCE, TEMPLATES_DIR
from constants import (
    LIBS_SHELVES,
    DEFAULT_GITIGNORE_LINES,
    QA_CONFIG_TEMPLATES,
    CLAUDE_DIR_NAME,
    CLAUDE_MD_FILENAME,
    GITIGNORE_FILENAME,
    LIBS_DIR_NAME,
    OS_SKILLS_FILENAME,
    SCRIPTS_DIR_NAME,
    SETTINGS_FILENAME,
    SKILL_MD_FILENAME,
    SKILLS_DIR_NAME,
    STATE_DIR_NAME,
    UI_SPECS_DIR_NAME,
)
from feedback import init_error_handling

init_error_handling()

# --- モジュール内派生定数 ---

STANDARD_DIRS = [
    *[f"{LIBS_DIR_NAME}/{s}" for s in LIBS_SHELVES],
    f"{CLAUDE_DIR_NAME}/{STATE_DIR_NAME}",
    SCRIPTS_DIR_NAME,
    UI_SPECS_DIR_NAME,
]


# --- ユーティリティ ---


def _nxt_relpath(project_root: Path) -> str:
    """NXT_ROOT のプロジェクトルート相対パス (posix 形式)。"""
    return NXT_ROOT.relative_to(project_root).as_posix()


def _claude_md_content(project_name: str, nxt_path: str) -> str:
    return (
        f"# {project_name}\n"
        f"\n"
        f"## erqo-next OS\n"
        f"@{nxt_path}/specs/00-identity.md\n"
        f"@{nxt_path}/specs/01-workflow.md\n"
        f"@{nxt_path}/specs/02-skills.md\n"
        f"@{nxt_path}/specs/03-tools.md\n"
        f"@{nxt_path}/specs/04-project-guide.md\n"
        f"@{nxt_path}/specs/05-session.md\n"
        f"\n"
        f"## プロジェクトルール\n"
    )


def _hook_config(nxt_path: str) -> dict:
    return {
        "SessionStart": [
            {
                "matcher": "startup|resume",
                "hooks": [{
                    "type": "command",
                    "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/session.py"',
                    "timeout": 10,
                    "statusMessage": "プロジェクト情報を読み込み中...",
                }],
            },
            {
                "matcher": "compact",
                "hooks": [{
                    "type": "command",
                    "command": f'python "$CLAUDE_PROJECT_DIR/{nxt_path}/core/session.py" --compact',
                    "timeout": 10,
                    "statusMessage": "コンテキストを復元中...",
                }],
            },
        ]
    }


def _claude_dir(project_root: Path) -> Path:
    return project_root / CLAUDE_DIR_NAME


def _state_dir(project_root: Path) -> Path:
    return _claude_dir(project_root) / STATE_DIR_NAME


def _project_skills_dir(project_root: Path) -> Path:
    return _claude_dir(project_root) / SKILLS_DIR_NAME


def _settings_path(project_root: Path) -> Path:
    return _claude_dir(project_root) / SETTINGS_FILENAME


def _os_skills_manifest_path(project_root: Path) -> Path:
    return _state_dir(project_root) / OS_SKILLS_FILENAME


# --- セットアップ関数 ---


def setup_claude_md(project_root: Path) -> bool:
    """CLAUDE.md を作成する。既存の場合はスキップ。"""
    claude_md = project_root / CLAUDE_MD_FILENAME
    if claude_md.exists():
        print(f"  {CLAUDE_MD_FILENAME}: 既存 (スキップ)")
        return False
    nxt_path = _nxt_relpath(project_root)
    content = _claude_md_content(project_root.name, nxt_path)
    claude_md.write_text(content, encoding="utf-8")
    print(f"  {CLAUDE_MD_FILENAME}: 作成")
    return True


def setup_hooks(project_root: Path) -> bool:
    """settings.json に SessionStart Hook を設定する。既存の Hook はマージ。"""
    nxt_path = _nxt_relpath(project_root)
    hook_config = _hook_config(nxt_path)

    settings_path = _settings_path(project_root)
    settings_path.parent.mkdir(parents=True, exist_ok=True)

    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            settings = {}
    else:
        settings = {}

    hooks = settings.setdefault("hooks", {})
    existing_matchers = set()
    if "SessionStart" in hooks:
        for entry in hooks["SessionStart"]:
            existing_matchers.add(entry.get("matcher", ""))
    else:
        hooks["SessionStart"] = []

    added = False
    for hook_entry in hook_config["SessionStart"]:
        if hook_entry["matcher"] not in existing_matchers:
            hooks["SessionStart"].append(hook_entry)
            added = True

    settings_path.write_text(
        json.dumps(settings, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  {SETTINGS_FILENAME}: Hook {'追加' if added else '設定済み (変更なし)'}")
    return added


def _scan_skills() -> list[str]:
    """NXT_ROOT/skills/ 内のスキルを自動スキャンする。"""
    skills_dir = NXT_ROOT / SKILLS_DIR_NAME
    if not skills_dir.exists():
        return []
    return sorted(
        d.name for d in skills_dir.iterdir()
        if d.is_dir() and (d / SKILL_MD_FILENAME).exists()
    )


def _rewrite_skill_paths(dst_dir: Path, nxt_path: str) -> None:
    """コピー先の SKILL.md 内の {nxt} プレースホルダを実パスに置換する。

    本体リポジトリ（nxt_path == "."）の場合は "{nxt}/" ごと除去する。
    プロジェクトの場合は "{nxt}" を相対パスに置換する。
    """
    skill_md = dst_dir / SKILL_MD_FILENAME
    if not skill_md.exists():
        return
    content = skill_md.read_text(encoding="utf-8")
    if nxt_path == ".":
        rewritten = content.replace("{nxt}/", "")
    else:
        rewritten = content.replace("{nxt}", nxt_path)
    if rewritten != content:
        skill_md.write_text(rewritten, encoding="utf-8")


def setup_skills(project_root: Path, update_mode: bool) -> int:
    """スキルを .claude/skills/ にコピーする。

    新規: 全スキルをコピー。
    更新: 前回 _os_skills.json に記録されていたスキルのみ管理する。
          - 現在も存在するスキル → 上書きコピー
          - 削除されたスキル → .claude/skills/ から削除（stale 除去）
          - 新規追加されたスキル → コピー（自動取り込み）
          固有スキル（マニフェスト外）は保持される。
    """
    nxt_path = _nxt_relpath(project_root)
    src_dir = NXT_ROOT / SKILLS_DIR_NAME
    dst_dir = _project_skills_dir(project_root)
    dst_dir.mkdir(parents=True, exist_ok=True)

    os_skills = _scan_skills()
    if not os_skills:
        print("  スキル: ソースなし (スキップ)")
        return 0

    # 更新モード: 前回のマニフェストと突き合わせて stale 削除を行う
    removed = 0
    if update_mode:
        manifest_path = _os_skills_manifest_path(project_root)
        previous_managed: set[str] = set()
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                previous_managed = set(manifest.get("skills", []))
            except (json.JSONDecodeError, OSError):
                previous_managed = set()

        # stale: 前回管理していたが現在の skills/ に存在しないもの
        current = set(os_skills)
        stale = previous_managed - current
        for skill_name in sorted(stale):
            stale_path = dst_dir / skill_name
            if stale_path.exists():
                shutil.rmtree(stale_path)
                removed += 1

    # コピー対象: 新規モードでも更新モードでも現在の os_skills 全てを反映
    targets = os_skills

    count = 0
    for skill_name in targets:
        src_skill = src_dir / skill_name
        dst_skill = dst_dir / skill_name
        if dst_skill.exists():
            shutil.rmtree(dst_skill)
        shutil.copytree(src_skill, dst_skill)
        _rewrite_skill_paths(dst_skill, nxt_path)
        count += 1

    if removed:
        print(f"  スキル: {count} 個コピー / {removed} 個削除")
    else:
        print(f"  スキル: {count} 個コピー")
    return count


def setup_os_skills_manifest(project_root: Path) -> None:
    """_os_skills.json を生成する。OS 提供スキルの一覧を記録。"""
    os_skills = _scan_skills()
    manifest = {"version": "1.0.0", "skills": os_skills}

    manifest_path = _os_skills_manifest_path(project_root)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  {OS_SKILLS_FILENAME}: {len(os_skills)} 個のスキルを記録")


def setup_directories(project_root: Path) -> list[str]:
    """必要なディレクトリを作成する。"""
    created = []
    for d in STANDARD_DIRS:
        path = project_root / d
        if not path.exists():
            path.mkdir(parents=True, exist_ok=True)
            created.append(d)

    if created:
        print(f"  ディレクトリ: {len(created)} 個作成")
    else:
        print("  ディレクトリ: すべて存在 (変更なし)")
    return created


def setup_gitignore(project_root: Path) -> bool:
    """.gitignore を生成する。既存の場合は不足分を追記。"""
    gitignore = project_root / GITIGNORE_FILENAME

    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        existing = {line.strip() for line in content.splitlines()}
        missing = [line for line in DEFAULT_GITIGNORE_LINES if line not in existing]
        if not missing:
            print(f"  {GITIGNORE_FILENAME}: 設定済み (変更なし)")
            return False
        if not content.endswith("\n"):
            content += "\n"
        content += "\n".join(missing) + "\n"
        gitignore.write_text(content, encoding="utf-8")
        print(f"  {GITIGNORE_FILENAME}: {len(missing)} 行追加")
    else:
        gitignore.write_text("\n".join(DEFAULT_GITIGNORE_LINES) + "\n", encoding="utf-8")
        print(f"  {GITIGNORE_FILENAME}: 作成")

    return True


def setup_qa_configs(project_root: Path) -> int:
    """品質チェック設定ファイルをテンプレートから生成する。既存は上書きしない。"""
    if not TEMPLATES_DIR.exists():
        print("  品質チェック設定: テンプレートなし (スキップ)")
        return 0

    created = 0
    skipped = []
    for filename in QA_CONFIG_TEMPLATES:
        src = TEMPLATES_DIR / filename
        dst = project_root / filename
        if not src.exists():
            continue
        if dst.exists():
            skipped.append(filename)
            continue
        shutil.copy2(src, dst)
        created += 1

    if created:
        print(f"  品質チェック設定: {created} ファイル生成")
    if skipped:
        print(f"  品質チェック設定: {len(skipped)} ファイル既存 (スキップ)")
    if not created and not skipped:
        print("  品質チェック設定: テンプレートなし (スキップ)")
    return created


def verify_installation(project_root: Path) -> bool:
    """インストール検証。必須ファイル・ディレクトリの存在チェック。"""
    print("\n検証:")
    all_ok = True

    # ファイルチェック
    for f in [CLAUDE_MD_FILENAME, GITIGNORE_FILENAME]:
        ok = (project_root / f).exists()
        print(f"  {'OK' if ok else 'NG'} {f}")
        all_ok = all_ok and ok

    # settings.json + SessionStart Hook
    settings_path = _settings_path(project_root)
    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
            has_hook = "SessionStart" in settings.get("hooks", {})
        except (json.JSONDecodeError, OSError):
            has_hook = False
    else:
        has_hook = False
    print(f"  {'OK' if has_hook else 'NG'} {SETTINGS_FILENAME} (SessionStart Hook)")
    all_ok = all_ok and has_hook

    # スキル
    skills_dir = _project_skills_dir(project_root)
    has_skills = skills_dir.exists() and any(skills_dir.iterdir()) if skills_dir.exists() else False
    label = "OK" if has_skills else "--"
    print(f"  {label} {CLAUDE_DIR_NAME}/{SKILLS_DIR_NAME}/ (スキル)")

    # .libs/ 標準棚
    for shelf in LIBS_SHELVES:
        ok = (project_root / LIBS_DIR_NAME / shelf).exists()
        print(f"  {'OK' if ok else 'NG'} {LIBS_DIR_NAME}/{shelf}/")
        all_ok = all_ok and ok

    return all_ok


# --- メイン ---


def main() -> None:
    if IS_SOURCE:
        print("エラー: このスクリプトはプロジェクト内でのみ実行できます。", file=sys.stderr)
        sys.exit(1)

    update_mode = "--update" in sys.argv
    project_root = NXT_ROOT.parent

    mode = "アップデート" if update_mode else "インストール"
    print(f"erqo-next {mode}: {project_root.name}")
    print()

    # 1. CLAUDE.md (新規のみ)
    if not update_mode:
        setup_claude_md(project_root)

    # 2. Hook 設定
    setup_hooks(project_root)

    # 3. スキルコピー
    setup_skills(project_root, update_mode)

    # 4. _os_skills.json
    setup_os_skills_manifest(project_root)

    # 5. ディレクトリ作成
    setup_directories(project_root)

    # 6. .gitignore
    if not update_mode:
        setup_gitignore(project_root)

    # 7. 品質チェック設定 (新規のみ)
    if not update_mode:
        setup_qa_configs(project_root)

    # 8. 検証
    all_ok = verify_installation(project_root)

    print(f"\n{mode}{'完了' if all_ok else '完了 (一部 NG あり)'}")
    if not update_mode and all_ok:
        print("新しいセッションを開始して /dsgn で設計フェーズを始めてください。")


if __name__ == "__main__":
    main()
