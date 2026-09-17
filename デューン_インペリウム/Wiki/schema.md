---
type: schema
title: デューン：インペリウム 反乱 Wiki Schema
description: 日本語ルールブックからデューン：インペリウム 反乱のLLM Wikiを生成・保守するためのローカル規約。
tags: [dune-imperium, uprising, schema, llm-wiki, okf]
language: ja
timestamp: "2026-09-17"
status: active
---

# デューン：インペリウム 反乱 Wiki Schema

## Purpose

`Sources`は人間が管理する不変の根拠、`Wiki`はそこからLLMが検索・要約・相互リンクする知識層とする。知識を概念単位のMarkdownへ分割し、YAML frontmatterで型・出典・状態を宣言する。

## Directory structure

```text
デューン_インペリウム/
├── Sources/                 # 人間が管理する日本語ルールブックと補助索引
└── Wiki/                    # OKF知識バンドル
    ├── index.md             # バンドル入口
    ├── log.md               # 追記式の更新履歴
    ├── schema.md            # この規約
    ├── entities/            # ゲームなどの固有対象
    ├── concepts/            # ルール・構造・用語
    ├── faq/                 # 疑問を公式ルールへ振り分けるFAQ・論点索引
    ├── strategy/            # コミュニティ戦略を概念ページへ接続するマップ
    └── sources/             # 出典台帳
```

## Page types

| `type` | 用途 | 配置先 |
|---|---|---|
| `entity` | ゲーム、製品などの固有対象 | `entities/` |
| `concept` | 準備、手番、戦闘、カードなどの知識単位 | `concepts/` |
| `faq` | 疑問、確認手順、未解決論点のルーター | `faq/` |
| `map` | 複数のソースや概念を接続する検索用マップ | `strategy/` |
| `source` | 根拠ファイルと照合範囲の記録 | `sources/` |
| `schema` | このWikiの維持規約 | Wiki root |

## Frontmatter

概念・エンティティ・FAQ・マップの内容ページは、次の標準項目を持つ。

```yaml
---
type: concept
title: Human-readable title
description: One-line summary.
tags: [dune-imperium, rules]
language: ja
source_files:
  - ../../Sources/JP_DUNE_IMPERIUM_UPRISING_Rulebook.pdf
timestamp: "2026-09-17"
status: stable
---
```

`type`、`title`、`description`、`tags`、`language`、`source_files`、`timestamp`、`status`を標準項目とする。`source_files`はWikiページから見た相対パスで書く。

## Index, navigation, and log

- root `index.md`はfrontmatterを`okf_version`だけにする。
- root `index.md`は全ページをカテゴリ別に列挙する。
- サブディレクトリの`index.md`はfrontmatterを持たないナビゲーションページにする。
- `log.md`はfrontmatterを持たず、新しい日付を上に追記する。

## Source and citation policy

- `Sources`自体は書き換えない。
- ルール上の事実は各ページ末尾の`# Citations`で、ローカルPDFのページへリンクする。
- 外部資料を照合に使った場合は、`sources/source-register.md`に根拠レベルとURLを記録する。
- BGGのようなコミュニティ資料は、`faq/`や`strategy/`の論点索引に使い、公式ルールを記述する`concepts/`の根拠と混同しない。
- ローカル原典と外部資料に差がある場合は、ローカル日本語ルールブックを優先し、差異を隠さない。
- 裁定が明示されていないものは推測で補わず、「要確認」として残す。

## Cross-linking

Wiki内リンクは標準相対リンクを使う。本文の説明に関連ページを埋め込み、必要に応じて末尾に`## 関連ページ`を置く。

## Ingest/update workflow

1. `Sources`の新規・変更ファイルを確認する。
2. 影響するconcept/entity/sourceページを特定する。
3. 既存ページを更新し、必要なら概念ページを追加する。
4. frontmatter、相対リンク、`# Citations`を確認する。
5. root `index.md`と`log.md`を更新する。
6. `Sources`は変更せず、Wikiだけをレビュー可能な差分として残す。

## OKF conformance checklist

- [ ] `index.md`と`log.md`以外のMarkdownにYAML frontmatterがある。
- [ ] 各frontmatterに空でない`type`がある。
- [ ] root `index.md`が全ページを列挙している。
- [ ] 各概念ページに`# Citations`がある。
- [ ] FAQ・マップページは、正規資料とコミュニティ資料の役割を明記している。
- [ ] 外部資料を使った場合、source registerに一次資料・二次資料の区別がある。
