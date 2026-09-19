---
type: schema
title: コンパイル Wiki Schema
description: Sourcesを不変の根拠、Wikiを検索・要約用のOKF知識層として保守する規約。
tags: [compile, schema, llm-wiki, okf]
language: ja
timestamp: "2026-09-19"
status: active
---

# コンパイル Wiki Schema

## ディレクトリ構成

```text
コンパイル/
├── Sources/                 # ルール画像
└── Wiki/
    ├── index.md             # 入口
    ├── log.md               # 更新履歴
    ├── schema.md            # この規約
    ├── wiki-guide.md        # 探索・回答ルール
    ├── entities/            # ゲームなど固有対象
    ├── concepts/            # ルール・用語
    ├── faq/                 # Rules Q&A
    ├── strategy/            # Strategy議論
    └── sources/             # 出典台帳・対応表
```

## ページ型

| `type` | 用途 |
|---|---|
| `entity` | ゲームそのもの、製品などの固有対象 |
| `concept` | 準備、手番、ライン、コンパイルなどのルール単位 |
| `faq` | 質問→回答→根拠の統合 |
| `strategy` | 実戦上の評価、コンボ、ドラフト論 |
| `source` | 原典・外部フォーラムの出典記録 |
| `guide` | Wikiの探索・回答規則 |
| `schema` | Wikiの維持規約 |

## 保守規則

- `Sources`は書き換えず、Wikiから相対リンクする。
- `index.md`と`log.md`を除くMarkdownには、非空の`type`を含むfrontmatterを置く。
- ルールの数値・順序・例外には`source_files`を付ける。
- BGGのコミュニティ情報は、公式ルールと明示的に区別する。
- 更新時は、このルートの`index.md`と`log.md`も確認する。
