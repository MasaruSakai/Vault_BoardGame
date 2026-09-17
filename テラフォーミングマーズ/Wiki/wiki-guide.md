---
type: guide
title: このWikiの使い方
description: テラフォーミング・マーズWikiをLLM Wiki / OKFとして探索・更新するための案内。
tags: [terraforming-mars, llm-wiki, okf, navigation, maintenance]
language: ja
source_files:
  - ../Sources/index.md
  - ../Sources/bgg-forums.md
timestamp: "2026-09-17"
status: active
---

# このWikiの使い方

## 探索順序

1. ルートの[index](index.md)で質問に近い分野を選ぶ。
2. 分野別`index.md`で、必要な本文ノートや論点マップへ進む。
3. ルール上の数値・アイコン・例外は、本文ノートの`sources`と[原典ページ対応表](source-page-map.md)で照合する。
4. BGGの個別トピックを読む場合は、RulesかStrategyか、基本ゲームかソロ・拡張かを確認する。

## 情報の層

| 層 | 場所 | 役割 |
|---|---|---|
| 一次資料 | `../Sources/TM_RULEBOOK_JPN-reprint2018w.pdf` | 日本語版ルール説明書。ルール判断の最優先根拠。 |
| 補助資料 | `../Sources/bgg-rules/` | BGG Rulesの個別トピック。コミュニティによる裁定・解釈。 |
| 補助資料 | `../Sources/bgg-strategy/` | BGG Strategyの個別トピック。条件付きの経験則・カード評価。 |
| 構造化知識 | `concepts/`、`overview/`、`rules/`など | 原典を概念・用途別に再配置したWiki層。 |
| 統合ルーター | `faq/`、`strategy/`、`syntheses/` | 同じ論点を複数の出典へ案内する索引・要約。 |

## ルールと戦略を分ける

- ルールノートは「何ができるか」「いつ処理するか」「何点になるか」を説明する。
- FAQは、本文ルールで迷いやすい個別論点を出典へ振り分ける。BGG投稿を公式裁定として扱わない。
- Strategyは、人数・初期手札・ドラフト・拡張・プレイ環境で結論が変わる経験則として扱う。
- ルール本文へ戦略上の「強い」「弱い」を混ぜず、必要なら[戦略論点マップ](strategy/topic-map.md)から別に参照する。

## 表記ルール

- 日本語を主表記とし、カード・タグ・資源の固有語は必要に応じて英語名を併記する。
- 1ノートは1つの目的または密接なルール群に限定する。
- 断定的な評価には、前提条件と根拠トピックを添える。
- `Sources`の本文を大量転載せず、要点とリンクをWiki側に置く。
