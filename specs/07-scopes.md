# 設定スコープのルール

エル子の OS には **「PC 個人」「マシンごと」という概念は存在しない**。
全ての設定・ファイル・スクリプトは次の 3 つのスコープのいずれかに属する。

## 3 つのスコープ

| スコープ | 適用範囲 | 物理的な置き場所 |
|---|---|---|
| **本元** | 本体リポジトリ（IS_SOURCE）でだけ有効 | `<source>/.claude/`, `<source>/specs/`, `<source>/release.sh` 等 |
| **プロジェクト** | エル子を使う各プロジェクトでだけ有効 | `<project>/.claude/`, `<project>/.libs/`, `<project>/.ui-specs/` 等 |
| **共通** | 本元・プロジェクト両方で有効 | `core/`, `skills/`, `specs/` (giget で配布) + `core/constants.py` の共通定数 |

## 禁止: PC 個人スコープ

`~/.claude/settings.json` のような **PC 個人グローバル設定** に erqo-next 関連の設定を書いてはいけない。

理由:
- ユーザーは複数のデバイスでこの OS を使う
- PC ごとに設定がバラバラだと、デバイス間で挙動が変わって混乱する
- 個人 PC 設定は git で管理されないので、他デバイスや他ユーザーと共有できない

例外: Claude Code 自身の純粋な個人嗜好（テーマ、エディタモード等）は OS と無関係なので `~/.claude/settings.json` に書いてよい。

## 共通スコープの実装方法

「本元・プロジェクト両方で同じ設定」を実現するには:

1. **単一の出どころを `core/constants.py` に定義する**
   - 例: `PERMISSION_DEFAULTS_ALLOW`, `PERMISSION_DEFAULTS_MODE`
2. **`core/install.py` がプロジェクト側に書き込む**
   - 例: `setup_permission_defaults(project_root)`
   - プロジェクトインストール時 / アップデート時に自動適用
3. **`core/dev.py` が本元側に書き込む**
   - 例: `cmd_setup()` 内から同じ `setup_permission_defaults` を呼ぶ
4. **両方とも constants.py の同じ定数を読む**
   - 「同じ場所が出どころ」になるので、変更は 1 か所だけで済む

## 違反時の対応

`~/.claude/settings.json` に erqo-next 関連の設定を書いた箇所を見つけたら:

1. その設定を `core/constants.py` の共通定数に移す
2. `setup_permission_defaults` のような共通設定の適用関数経由で配置する
3. PC 個人ファイルからは削除する

新規に設定を追加する場合も、最初から「本元 / プロジェクト / 共通」のいずれに属するかを判断してから配置する。
