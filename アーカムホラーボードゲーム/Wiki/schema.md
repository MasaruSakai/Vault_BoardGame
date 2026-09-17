---
type: schema
title: アーカムホラー 第3版 Wiki Schema
description: Sourcesからアーカムホラー 第3版のLLM Wiki / OKFを生成・保守するためのローカル規約。
tags: [arkham-horror, schema, llm-wiki, okf]
language: ja
timestamp: "2026-09-17"
status: active
---

# アーカムホラー 第3版 Wiki Schema

## 目的

`Sources/`を人間が管理する原典、`Wiki/`を原典から整理した検索可能な知識層として扱う。OKFでは、各知識単位をMarkdownファイルにし、YAML frontmatterの`type`でページの役割を宣言する。

## ディレクトリ構成

```text
アーカムホラーボードゲーム/
├── Sources/                 # 原典画像。変更しない
└── Wiki/                    # OKF知識バンドル
    ├── index.md             # ルート入口
    ├── wiki-guide.md        # 探索・更新ガイド
    ├── schema.md            # この規約
    ├── log.md               # 更新履歴
    ├── overview/            # ゲーム概要・内容物
    ├── how-to-play/         # 準備・ラウンド・アクション
    ├── rules/               # ルール群の概念ノート
    ├── reference/           # 公式訂正・FAQ・用語・補足
    ├── syntheses/           # 複数資料の統合・コミュニティ資料
    └── sources/              # 出典台帳・原典画像・読み起こし
```

## ページ型

| `type` | 用途 | 配置先 |
|---|---|---|
| `entity` | ゲーム、探索者、カードなどの固有対象 | `overview/`または`rules/` |
| `concept` | ルール、ゲーム構造、処理手順 | `overview/`、`how-to-play/`、`rules/` |
| `reference` | 公式エラッタ、FAQ、用語、早見表 | `reference/` |
| `synthesis` | BGG議論、比較、戦略、プレイ体験の統合 | `syntheses/` |
| `source` | 原典とWikiページの対応、出典の説明 | `sources/` |
| `schema` | このWikiの維持規約 | Wiki root |

## Frontmatter

`index.md`、各ディレクトリの`index.md`、`log.md`以外のMarkdownは、少なくとも次の項目を持つ。

```yaml
---
type: concept
title: Human-readable title
description: One-line routing summary.
tags: [arkham-horror, rules]
language: ja
source_files:
  - ../../Sources/example.jpg
timestamp: "2026-09-17"
status: stable
---
```

既存ノートの`generated`や`sources`は保持してよい。`source_files`または`sources`から原典を追跡できることを優先する。

## 出典と引用

- `Sources/`は原典資料として変更しない。
- Wiki本文の事実は、frontmatterの`sources`または末尾の`## 出典`で追跡できるようにする。
- ローカル原典は標準Markdownの相対リンク、Web資料は絶対URLで記載する。
- 公式ルール、公式エラッタ、公式FAQ、カード本文、シナリオ本文と、BGGなどのコミュニティ二次資料を区別する。
- 複数資料が食い違う場合は、単一の値に丸めず、公式資料を優先した理由または不確実性を本文に残す。

## 更新手順

1. `Sources/`の新規・変更ファイルを確認する。
2. 影響する概要、遊び方、ルール、リファレンスを特定する。
3. 必要なら統合・コミュニティ資料を更新する。
4. frontmatter、相対リンク、出典を確認する。
5. ルートと各分野の`index.md`、`log.md`を更新する。
6. `Sources/`自体は変更せず、Wiki側の差分をレビュー可能な形で残す。

## OKFチェックリスト

- [ ] `Sources/`と`Wiki/`が分離している。
- [ ] root `index.md`と各分野の`index.md`が全ページを案内している。
- [ ] `index.md`と`log.md`以外のMarkdownに非空の`type`がある。
- [ ] 事実を含むページから原典またはWeb出典へ戻れる。
- [ ] コミュニティ提案を公式ルールとして扱っていない。
- [ ] リンク先が新しいディレクトリ構成と一致している。
