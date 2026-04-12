---
name: dsgn
target: project
description: /dsgn - プロジェクト初期の大枠設計。ユーザーとの対話でプロジェクトの目的・全体像・機能セクション一覧を策定し、.libs/design/project-spec/ に保存する。
effort: max
---

# /dsgn - 対話・設計スキル

## 概要

プロジェクト初期に1度実行し、大枠の機能セクションを決める。深入りしない。

## 実行手順

### 1. ユーザーとの対話

以下をユーザーと対話しながら整理する:
- プロジェクトの目的・ゴール
- 主要な機能（セクション単位で）
- 全体の構成イメージ

**注意:** 各セクションの詳細には踏み込まない。詳細は `/tp` で行う。

### 2. 設計書の作成

対話で方針が固まったら、承認を取ってから作成する。

**保存先:** `.libs/design/project-spec/`

```markdown
# DSGN-PROJECT-SPEC — プロジェクト設計概要

タグ: 設計, 要件, overview, design

## DSGN-PROJECT-SPEC.概要 — 概要
プロジェクトの目的と全体像

## DSGN-PROJECT-SPEC.機能一覧 — 機能セクション一覧

| セクション | 概要 | ステータス |
|---|---|---|
| AUTH | 認証・セッション管理 | 未着手 |
| API | REST APIエンドポイント | 未着手 |
```

### 3. 外部サーバー情報の定義（MCP 経由で触るサーバーがある場合のみ）

プロジェクトが Cloudflare / GitHub / Vercel / Supabase などの外部サーバーを MCP 経由で操作する場合、このステップで使うサーバーとリソースを明示する。これは `specs/07-scopes.md`「外部サーバー操作のプロジェクト境界」で参照される **機械的な判定源** になる。

**保存先:** `.libs/design/project-spec/servers.md`
**識別コード:** `PROJECT-SERVERS`

```markdown
# PROJECT-SERVERS — このプロジェクトが使う外部サーバー

タグ: 外部サーバー, MCP, cloudflare, github, servers

## PROJECT-SERVERS.cloudflare — Cloudflare
- **アカウント ID:** `1234567890abcdef...`
- **使用リソース:**
  - Worker: `my-app-api`（用途: REST API）
  - Durable Object namespace: `SESSION`（用途: セッション管理）
  - R2 Bucket: `my-app-uploads`（用途: ユーザーアップロード保存）
  - KV Namespace: `my-app-cache`（用途: 短期キャッシュ）

## PROJECT-SERVERS.github — GitHub
- **Org / User:** `my-org`
- **使用リポジトリ:**
  - `my-org/my-app`（このプロジェクトの本体）
```

**記載の原則:**

1. **このプロジェクトで実際に使うリソース** だけ書く（関係ないリソースは書かない）
2. サービスやリソースの追加・変更は対話 → 承認 → このページを更新
3. 外部サーバーを一切使わない純粋ローカルアプリではこのファイルは作らない（その場合 MCP 経由の外部サーバー操作自体が発生しない）

### 4. インデックス更新

作成後、以下を実行する:

```bash
python "{nxt}/core/index.py" reindex
```

### 重要なルール

1. **深入りしない** — セクション一覧を速やかに策定する。各セクションの詳細設計は `/tp` で行う
2. **ページフォーマット準拠** — ヘッダー（`# ID — タイトル`）、タグ行、セクション記法を守る
3. **170行目安** — 情報量が多い場合はファイルを分割する
4. **関連ページ** — 片方向でよい（逆リンクの追記は不要）
5. **サーバー情報も設計の一部** — MCP 経由で外部サーバーを触るプロジェクトでは `PROJECT-SERVERS` ページを作る。AI は勝手に記載範囲を広げず、対話 → 承認 → 編集の流れで更新する（詳細は `specs/07-scopes.md`）
