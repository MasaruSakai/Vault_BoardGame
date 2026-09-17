---
type: source
title: クランク！カタコンベ Source Register
description: ClankCatacombs/Sources配下の原典画像とBGGフォーラム索引、Wikiでの利用箇所を記録する台帳。
tags: [clank-catacombs, sources, provenance, register]
language: ja
source_files:
  - ../../Sources/rulebook-page-01.jpg
  - ../../Sources/rulebook-page-18.jpg
  - ../../Sources/bgg-forums-index.md
timestamp: "2026-09-17"
status: stable
---

# Source Register

## Source policy

`ClankCatacombs/Sources`はraw source rootです。画像はルールブックの原典、BGGファイルはコミュニティ議論への索引として扱います。LLM Wiki側で要約・構造化し、Sources自体は書き換えません。

## Local source map

| Source | 内容 | 根拠レベル | 主な利用先 |
|---|---|---|---|
| [rulebook-page-01.jpg](../../Sources/rulebook-page-01.jpg)〜[18.jpg](../../Sources/rulebook-page-18.jpg) | 日本語版ルール説明書のページ画像 | 一次資料 | [Concepts](../concepts/index.md)、[原典ページ対応表](source-page-map.md) |
| [bgg-forums-index.md](../../Sources/bgg-forums-index.md) | BGG Rules／Strategyの分類とページ入口 | コミュニティ索引 | [ゲーム概要](../concepts/game-overview.md)、各ルール確認時の補足 |
| [bgg-rules-forum.md](../../Sources/bgg-rules-forum.md) | Rules 204件への入口と、代表的な疑問20件のQ&A | コミュニティ二次資料 | Rulesの疑問を結論・根拠つきで確認する入口 |
| [bgg-strategy-forum.md](../../Sources/bgg-strategy-forum.md) | Strategy 6件の投稿内容と実戦フレーム | コミュニティ二次資料 | 戦略・デッキ構築の補足 |

## Source priority

1. 日本語版ルールブック画像
2. ルールブックの図版・Token Reference Guide
3. BGGフォーラム（質問・経験談・非公式の回答）

BGGの投稿は公式裁定ではありません。公式原典だけでは確定できない場合は「要確認」として残し、投稿者の解釈を基本ルールへ混ぜないでください。
