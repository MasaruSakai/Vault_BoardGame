---
type: schema
title: Pralaya Wiki Schema
description: Pralaya WikiをLLM WikiとOKF v0.1の規約で維持するためのローカルスキーマ。
tags: [Pralaya, schema, llm-wiki, okf]
language: ja
timestamp: "2026-09-10"
status: active
---

# Pralaya Wiki Schema

## Purpose

このファイルは、`Pralaya/Sources`から`Pralaya/Wiki`へ知識をコンパイルする際のローカル規約です。LLM Wikiでは、Sourcesを人間が管理する不変の根拠、WikiをLLMが要約・相互リンクする知識層として扱います。OKFでは、各知識単位をMarkdownファイルとして保存し、YAML frontmatterの`type`で型を宣言します。

## Directory structure

```text
Pralaya/
├── Sources/                 # immutable source root
└── Wiki/                    # OKF bundle / compiled knowledge
    ├── index.md             # bundle entry point
    ├── log.md               # append-only operation history
    ├── schema.md            # this file
    ├── entities/            # named game/product entities
    ├── concepts/            # durable rules and domain knowledge
    ├── syntheses/            # comparisons and analyses
    └── sources/              # source register and provenance
```

## Page types

| `type` | 用途 | 配置先 |
|---|---|---|
| `entity` | ゲーム、製品、人物などの固有対象 | `entities/` |
| `concept` | ルール、カード、ゲーム構造などの知識単位 | `concepts/` |
| `synthesis` | 複数資料を統合した比較・分析 | `syntheses/` |
| `source` | 根拠ファイルの役割・出典・確実性の記録 | `sources/` |
| `schema` | このWikiの維持規約 | Wiki root |

## Frontmatter

すべての概念ページは、先頭に次の基本項目を持ちます。

```yaml
---
type: concept
title: Human-readable title
description: One-line summary.
tags: [Pralaya, rules]
language: ja
source_files:
  - ../../Sources/Pralaya_Rulebook_JA.md
timestamp: "2026-09-10"
status: stable
---
```

`type`は必須です。`title`、`description`、`tags`、`timestamp`、`source_files`、`language`、`status`は、検索性・出典追跡・保守性のために標準項目として使用します。OKFの許容範囲内で、ドメイン固有の追加項目も使用できます。

## Index and log

- `index.md`はバンドルの入口で、frontmatterは`okf_version`だけにします。
- `index.md`は、全ページをカテゴリ別に列挙します。
- `log.md`はfrontmatterを持たず、日付の新しい順に更新履歴を追記します。
- サブディレクトリの`index.md`もfrontmatterを持たないナビゲーションファイルとします。

## Source and citation policy

- `Sources`は根拠資料であり、Wiki生成時に書き換えません。
- Wiki本文の事実には、末尾の`# Citations`で根拠を列挙します。
- 手元のSourceは相対リンク、Web資料は通常の絶対URLリンクで記載します。
- 一次資料（公式マニュアル・公式告知）と二次資料（レビュー・個人解説）を区別します。
- 根拠が不一致の場合は、単一の値に丸めず、本文に不確実性を残します。

## Cross-linking

Wiki内のリンクは、移動に強く、一般のMarkdownビューアでも開ける標準相対リンクを使用します。関連ページは本文中の`See also`または「関連ページ」節からリンクします。

## Ingest/update workflow

1. `Sources`の新規・変更ファイルを確認する。
2. 影響するconcept/entity/synthesisを特定する。
3. 既存ページを更新し、必要なら新しい概念ページを作る。
4. frontmatter、相対リンク、`# Citations`を確認する。
5. root `index.md`と`log.md`を更新する。
6. Sources自体は変更せず、Wikiの差分をレビュー可能な形で残す。

## OKF conformance checklist

- [ ] `index.md`と`log.md`以外のMarkdownにYAML frontmatterがある。
- [ ] 各frontmatterに空でない`type`がある。
- [ ] root `index.md`が全ページを列挙している。
- [ ] 外部情報を使ったページに`# Citations`がある。
- [ ] リンク先と、一次資料・二次資料の区別を確認している。
