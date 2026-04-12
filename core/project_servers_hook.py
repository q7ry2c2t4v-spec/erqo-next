"""project_servers_hook.py — MCP ツール呼び出し前の PROJECT-SERVERS 照合リマインダー.

PreToolUse Hook (matcher: ``mcp__.*``) から呼ばれ、PROJECT-SERVERS ページ
(``.libs/design/project-spec/servers.md``) の有無と照合義務を stderr に通知する。
ブロックしない (``exit 0``)。本元 (``IS_SOURCE``) ではスキップする。

責務:
- ``specs/07-scopes.md`` 「外部サーバー操作のプロジェクト境界」の AI 向け reminder
- 実際のリソース照合は AI 側が PROJECT-SERVERS ページを Read して行う
- この Hook は情報提供のみで、ツール実行を妨げない
"""

from __future__ import annotations

import io
import sys

# Windows の cp932 環境でも日本語ラベルを出せるように UTF-8 に切り替える
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from paths import IS_SOURCE, PROJECT_ROOT
from constants import PROJECT_SERVERS_PAGE_REL

_HEADING = "## 外部サーバー境界 (PROJECT-SERVERS 照合)"
_MSG_NO_PAGE = (
    f"{_HEADING}\n"
    f"注意: PROJECT-SERVERS ページが見つかりません ({PROJECT_SERVERS_PAGE_REL})。\n"
    "specs/07-scopes.md「外部サーバー操作のプロジェクト境界」より、\n"
    "このページが存在しないサービスは MCP 経由での操作禁止です。\n"
    "先に /dsgn または対話 → 承認 → 編集で servers.md を用意してください。"
)
_MSG_PAGE_EXISTS = (
    f"{_HEADING}\n"
    f"MCP 操作前に必ず {PROJECT_SERVERS_PAGE_REL} を Read し、\n"
    "操作対象のリソースが PROJECT-SERVERS に記載されているか照合してください。\n"
    "記載されていないリソースへの操作は禁止 (specs/07-scopes.md)。"
)


def main() -> int:
    # 本元 (エル子) では PROJECT-SERVERS を使わないのでスキップ
    if IS_SOURCE or PROJECT_ROOT is None:
        return 0

    servers_page = PROJECT_ROOT / PROJECT_SERVERS_PAGE_REL
    msg = _MSG_PAGE_EXISTS if servers_page.exists() else _MSG_NO_PAGE
    print(msg, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
