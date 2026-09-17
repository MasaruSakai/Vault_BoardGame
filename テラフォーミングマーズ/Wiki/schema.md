---
type: schema
title: テラフォーミング・マーズ Wiki Schema
description: SourcesからLLM Wiki / OKF知識バンドルを生成・保守するためのローカル規約。
tags: [terraforming-mars, schema, llm-wiki, okf]
language: ja
timestamp: "2026-09-17"
status: active
---

# テラフォーミング・マーズ Wiki Schema

## 目的

`Sources`を根拠資料、`Wiki`を検索・要約・相互リンクの知識層として分離する。ルール本文、頻出質問、戦略議論を同じページに混在させず、出典の強さが読者に分かる構造にする。

## ディレクトリ構成

```text
テラフォーミングマーズ/
├── Sources/                 # 日本語マニュアルとBGGトピック別資料
└── Wiki/
    ├── index.md             # バンドル入口
    ├── wiki-guide.md        # 探索・更新の案内
    ├── log.md               # 追記式の更新履歴
    ├── schema.md            # この規約
    ├── entities/            # ゲームという固有対象
    ├── concepts/            # 概念ノートの索引
    ├── overview/            # 概要・内容物・盤面
    ├── rules/               # 準備・世代・アクション・終了
    ├── reference/           # アイコン・出典・ページ対応
    ├── faq/                 # ルール論点のルーター
    ├── strategy/            # 戦略論点のルーター
    └── syntheses/           # 複数資料の統合要約
```

ルールブック由来の本文ノートは`concepts/`に置き、`overview/`や`rules/`などの分野別`index.md`から参照する。索引・FAQ・戦略マップを本文から分離し、OKFの段階的開示を保つ。

## ページ型

| `type` | 用途 | 主な場所 |
|---|---|---|
| `entity` | ゲームなど固有対象の説明 | `entities/` |
| `concept` | ルール・資源・タイルなどの知識単位 | `concepts/` |
| `faq` | 疑問を公式根拠と補助資料へ振り分ける | `faq/` |
| `strategy-map` | 戦略トピックを条件別に分類する | `strategy/` |
| `synthesis` | 複数の補助資料を横断して要約する | `syntheses/` |
| `source` / `source-map` | 根拠資料・対応表を記録する | `sources/`、ルート |
| `guide` / `schema` | Wikiの読み方・維持規約 | Wiki root |

## Frontmatter

本文ページは、次の共通項目を持つ。

```yaml
---
type: concept
title: 人間向けタイトル
description: 索引とLLMルーティングに使える一文。
tags: [terraforming-mars, rules]
language: ja
source_files:
  - ../Sources/TM_RULEBOOK_JPN-reprint2018w.pdf
timestamp: "2026-09-17"
status: stable
---
```

原典ページを細かく示す本文ノートでは、既存の`sources`欄とページ画像リンクも併用する。`index.md`はナビゲーション専用、`log.md`は履歴専用として扱う。

## 出典の優先順位

1. 日本語版ルール説明書、カード本文、公式訂正があればそれら。
2. Wikiの概念ノートは、一次資料を検索しやすくした要約。
3. BGG Rulesはコミュニティによるルール論点の補助資料。
4. BGG Strategyは戦略・カード評価の補助資料で、公式ルールではない。

## 更新時の検証

- 追加資料を`Sources`に登録してから、影響するFAQ・戦略マップ・統合要約を更新する。
- Markdownリンクはリンク元ファイルからの相対パスとして解決する。
- ルールと戦略の主張を同じ段落に混ぜない。
- BGGの件数や内容は取得時点の情報であることを明記する。
- 更新内容を[更新履歴](log.md)に追記する。
