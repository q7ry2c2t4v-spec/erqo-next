"""handler.py - /fb フィードバック送信 CLI

ユーザーのフィードバックを JSON レポートとして保存する。

使い方:
    python .nxt-core/skills/fb/handler.py <kind> <summary> [detail]
    python .nxt-core/skills/fb/handler.py <kind> <summary> --detail-file PATH

kind: suggestion | error | other

--detail-file は detail に `|` などシェル特殊文字が含まれるとき用。
Windows + Git Bash で `||` が CMD の論理 OR として誤解釈される事故を防ぐ。
"""

import argparse
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
    parser = argparse.ArgumentParser(
        description="erqo-next フィードバック送信 CLI",
    )
    parser.add_argument("kind", help="suggestion | error | other")
    parser.add_argument("summary", help="フィードバックの要約")
    parser.add_argument(
        "detail",
        nargs="?",
        default="",
        help="詳細 (省略可、シェルに | を渡しにくい場合は --detail-file を使う)",
    )
    parser.add_argument(
        "--detail-file",
        dest="detail_file",
        help="詳細を読み込むファイルパス (UTF-8)。指定時は positional の detail より優先",
    )
    args = parser.parse_args()

    if args.detail_file:
        detail_path = Path(args.detail_file)
        if not detail_path.exists():
            print(f"fb: --detail-file が存在しません -> {detail_path}", file=sys.stderr)
            sys.exit(1)
        detail = detail_path.read_text(encoding="utf-8")
    else:
        detail = args.detail

    path = send_feedback(kind=args.kind, summary=args.summary, detail=detail)

    if path:
        print(f"fb: フィードバックを保存しました -> {path}")
    else:
        print("fb: フィードバックの保存に失敗しました", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
