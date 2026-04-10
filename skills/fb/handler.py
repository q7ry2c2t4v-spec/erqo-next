"""handler.py - /fb フィードバック送信 CLI

ユーザーのフィードバックを JSON レポートとして保存する。

使い方:
    python .nxt-core/skills/fb/handler.py <kind> <summary> [detail]

kind: suggestion | error | other
"""

import io
import sys
from pathlib import Path

# Windows UTF-8 出力
if sys.stdout.encoding and sys.stdout.encoding.lower().replace("-", "") != "utf8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding and sys.stderr.encoding.lower().replace("-", "") != "utf8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# core/ をパスに追加
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "core"))

from feedback import init_error_handling, send_feedback

init_error_handling()


def main() -> None:
    if len(sys.argv) < 3:
        print("usage: handler.py <kind> <summary> [detail]")
        print("  kind: suggestion | error | other")
        sys.exit(1)

    kind = sys.argv[1]
    summary = sys.argv[2]
    detail = sys.argv[3] if len(sys.argv) > 3 else ""

    path = send_feedback(kind=kind, summary=summary, detail=detail)

    if path:
        print(f"fb: フィードバックを保存しました -> {path}")
    else:
        print("fb: フィードバックの保存に失敗しました", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
