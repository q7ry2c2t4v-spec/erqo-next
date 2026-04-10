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

from paths import NXT_ROOT
from feedback import init_error_handling

init_error_handling()

# --- 定数 ---

LIBS_SHELVES = ["design", "features", "docs", "research", "rules", "session-logs", "archive"]

STANDARD_DIRS = [
    *[f".libs/{s}" for s in LIBS_SHELVES],
    ".claude/state",
    "scripts",
    ".ui-specs",
]

GITIGNORE_LINES = [
    ".claude/state/",
    ".claude/settings.local.json",
    "node_modules/",
    ".next/",
]

OS_SKILLS_FILENAME = "_os_skills.json"

QA_CONFIG_TEMPLATES = ["eslint.config.mjs", "playwright.config.ts", "lighthouserc.js"]


# --- ユーティリティ ---


def _nxt_relpath(project_root: Path) -> str:
    """NXT_ROOT のプロジェクトルート相対パス (posix 形式)。"""
    return NXT_ROOT.relative_to(project_root).as_posix()


def _claude_md_content(project_name: str, nxt_path: str) -> str:
    return (
        f"# {project_name}\n"
        f"\n"
        f"## erqo-nxt OS\n"
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


# --- セットアップ関数 ---


def setup_claude_md(project_root: Path) -> bool:
    """CLAUDE.md を作成する。既存の場合はスキップ。"""
    claude_md = project_root / "CLAUDE.md"
    if claude_md.exists():
        print("  CLAUDE.md: 既存 (スキップ)")
        return False
    nxt_path = _nxt_relpath(project_root)
    content = _claude_md_content(project_root.name, nxt_path)
    claude_md.write_text(content, encoding="utf-8")
    print("  CLAUDE.md: 作成")
    return True


def setup_hooks(project_root: Path) -> bool:
    """settings.json に SessionStart Hook を設定する。既存の Hook はマージ。"""
    nxt_path = _nxt_relpath(project_root)
    hook_config = _hook_config(nxt_path)

    settings_path = project_root / ".claude" / "settings.json"
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
    print(f"  settings.json: Hook {'追加' if added else '設定済み (変更なし)'}")
    return added


def _scan_skills() -> list[str]:
    """NXT_ROOT/skills/ 内のスキルを自動スキャンする。"""
    skills_dir = NXT_ROOT / "skills"
    if not skills_dir.exists():
        return []
    return sorted(
        d.name for d in skills_dir.iterdir()
        if d.is_dir() and (d / "SKILL.md").exists()
    )


def _rewrite_skill_paths(dst_dir: Path, nxt_path: str) -> None:
    """コピー先の SKILL.md 内の {nxt} プレースホルダを実パスに置換する。"""
    skill_md = dst_dir / "SKILL.md"
    if not skill_md.exists():
        return
    content = skill_md.read_text(encoding="utf-8")
    rewritten = content.replace("{nxt}", nxt_path)
    if rewritten != content:
        skill_md.write_text(rewritten, encoding="utf-8")


def setup_skills(project_root: Path, update_mode: bool) -> int:
    """スキルを .claude/skills/ にコピーする。

    新規: 全スキルをコピー。
    更新: _os_skills.json に記録されたスキルのみ上書き。固有スキルは保持。
    """
    nxt_path = _nxt_relpath(project_root)
    src_dir = NXT_ROOT / "skills"
    dst_dir = project_root / ".claude" / "skills"
    dst_dir.mkdir(parents=True, exist_ok=True)

    os_skills = _scan_skills()
    if not os_skills:
        print("  スキル: ソースなし (スキップ)")
        return 0

    # 更新モード: _os_skills.json で管理対象を判定
    if update_mode:
        manifest_path = project_root / ".claude" / "state" / OS_SKILLS_FILENAME
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                managed = set(manifest.get("skills", []))
            except (json.JSONDecodeError, OSError):
                managed = set(os_skills)
        else:
            managed = set(os_skills)
        targets = [s for s in os_skills if s in managed]
    else:
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

    print(f"  スキル: {count} 個コピー")
    return count


def setup_os_skills_manifest(project_root: Path) -> None:
    """_os_skills.json を生成する。OS 提供スキルの一覧を記録。"""
    os_skills = _scan_skills()
    manifest = {"version": "1.0.0", "skills": os_skills}

    manifest_path = project_root / ".claude" / "state" / OS_SKILLS_FILENAME
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"  _os_skills.json: {len(os_skills)} 個のスキルを記録")


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
    gitignore = project_root / ".gitignore"

    if gitignore.exists():
        content = gitignore.read_text(encoding="utf-8")
        existing = {line.strip() for line in content.splitlines()}
        missing = [line for line in GITIGNORE_LINES if line not in existing]
        if not missing:
            print("  .gitignore: 設定済み (変更なし)")
            return False
        if not content.endswith("\n"):
            content += "\n"
        content += "\n".join(missing) + "\n"
        gitignore.write_text(content, encoding="utf-8")
        print(f"  .gitignore: {len(missing)} 行追加")
    else:
        gitignore.write_text("\n".join(GITIGNORE_LINES) + "\n", encoding="utf-8")
        print("  .gitignore: 作成")

    return True


def setup_qa_configs(project_root: Path) -> int:
    """品質チェック設定ファイルをテンプレートから生成する。既存は上書きしない。"""
    templates_dir = NXT_ROOT / "specs" / "templates"
    if not templates_dir.exists():
        print("  品質チェック設定: テンプレートなし (スキップ)")
        return 0

    created = 0
    skipped = []
    for filename in QA_CONFIG_TEMPLATES:
        src = templates_dir / filename
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
    for f in ["CLAUDE.md", ".gitignore"]:
        ok = (project_root / f).exists()
        print(f"  {'OK' if ok else 'NG'} {f}")
        all_ok = all_ok and ok

    # settings.json + SessionStart Hook
    settings_path = project_root / ".claude" / "settings.json"
    if settings_path.exists():
        try:
            settings = json.loads(settings_path.read_text(encoding="utf-8"))
            has_hook = "SessionStart" in settings.get("hooks", {})
        except (json.JSONDecodeError, OSError):
            has_hook = False
    else:
        has_hook = False
    print(f"  {'OK' if has_hook else 'NG'} settings.json (SessionStart Hook)")
    all_ok = all_ok and has_hook

    # スキル
    skills_dir = project_root / ".claude" / "skills"
    has_skills = skills_dir.exists() and any(skills_dir.iterdir()) if skills_dir.exists() else False
    label = "OK" if has_skills else "--"
    print(f"  {label} .claude/skills/ (スキル)")

    # .libs/ 標準棚
    for shelf in LIBS_SHELVES:
        ok = (project_root / ".libs" / shelf).exists()
        print(f"  {'OK' if ok else 'NG'} .libs/{shelf}/")
        all_ok = all_ok and ok

    return all_ok


# --- メイン ---


def main() -> None:
    update_mode = "--update" in sys.argv
    project_root = NXT_ROOT.parent

    mode = "アップデート" if update_mode else "インストール"
    print(f"erqo-nxt {mode}: {project_root.name}")
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
