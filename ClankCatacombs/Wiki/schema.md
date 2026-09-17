---
type: schema
title: クランク！カタコンベ Wiki Schema
description: SourcesからLLM Wiki／OKF知識バンドルを生成・保守するためのローカル規約。
tags: [clank-catacombs, schema, llm-wiki, okf]
language: ja
timestamp: "2026-09-17"
status: active
---

# クランク！カタコンベ Wiki Schema

## 目的

`Sources`は人間が管理する不変の根拠、`Wiki`はそこからLLMが検索・要約・相互リンクする知識層とします。知識を概念単位のMarkdownへ分割し、YAML frontmatterで型・出典・状態を宣言します。

## ディレクトリ構成

```text
ClankCatacombs/
├── Sources/                 # 原典画像・外部フォーラム索引
└── Wiki/                    # OKF知識バンドル
    ├── index.md             # バンドル入口
    ├── log.md               # 追記式の更新履歴
    ├── schema.md            # この規約
    ├── entities/            # ゲームなど固有対象
    ├── concepts/            # ルール・カード・タイルなどの概念
    └── sources/              # 出典台帳と対応表
```

## ページ型

| `type` | 用途 | 配置先 |
|---|---|---|
| `entity` | ゲーム、製品などの固有対象 | `entities/` |
| `concept` | 準備、手番、戦闘、カード、タイルなどの知識単位 | `concepts/` |
| `source` | 根拠ファイルと照合範囲の記録 | `sources/` |
| `schema` | Wikiの維持規約 | Wiki root |

## Frontmatter

概念ページとエンティティページは、`type`、`title`、`description`、`tags`、`language`、`source_files`、`timestamp`、`status`を標準項目とします。

```yaml
---
type: concept
title: Human-readable title
description: One-line summary.
tags: [clank-catacombs, rules]
language: ja
source_files:
  - ../../Sources/rulebook-page-01.jpg
timestamp: "2026-09-17"
status: stable
---
```

`index.md`と`log.md`はナビゲーション／履歴のためfrontmatterを最小限にし、サブディレクトリの`index.md`もナビゲーション専用とします。

## Sourceと引用

- `Sources`自体は書き換えず、Wiki側から相対リンクで参照します。
- ルール上の数値・アイコン・例外は、概念ページの`source_files`と本文中の原典リンクで追跡できるようにします。
- BGGなどの外部資料はコミュニティ情報として公式原典と区別し、`sources/source-register.md`に根拠レベルを記録します。
- 原典画像とコミュニティ投稿が食い違う場合は、原典画像を優先し、不確実性を隠しません。

## 更新手順

1. `Sources`の新規・変更資料を確認する。
2. 影響するconcept、entity、sourceページを特定する。
3. 必要なページを更新し、相対リンクとfrontmatterを確認する。
4. root `index.md`と`log.md`を更新する。
5. Markdownリンクと原典参照を検証する。

## OKF適合チェック

- [ ] `index.md`と`log.md`以外のMarkdownに非空の`type`がある。
- [ ] 概念・エンティティページに`title`、`description`、`language`、`status`がある。
- [ ] root `index.md`が全カテゴリの入口を列挙している。
- [ ] 各概念ページが原典画像へ追跡可能である。
- [ ] 外部フォーラムは公式ルールと混同しない。
