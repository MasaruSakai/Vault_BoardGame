---
type: guide
title: このWikiの使い方
description: LLM Wikiとしての探索順序、原典との関係、OKF文書の更新規則を定める。
tags: [llm-wiki, okf, navigation, maintenance]
language: ja
timestamp: "2026-09-17"
status: active
---

# 読み方

1. まずルートの[index](index.md)を読み、質問に最も近い分野を選ぶ。
2. 分野内の`index.md`から、必要な概念ノートだけを開く。
3. 数値、アイコン、例外条件を回答するときは、各ノートの`sources`にある原典ページも確認する。
4. 関連事項が必要な場合だけ本文中の相対リンクを辿る。

# 情報の層

- `../Sources/`: ルールブック画像とBGGフォーラム索引。事実確認のための原典・補助索引。
- `Wiki/concepts/`: 原典から整理した、検索可能な知識。
- `Wiki/entities/`: ゲームなど固有対象の説明。
- `Wiki/sources/`: 出典台帳とページ対応表。
- 各`index.md`: 内容を一行ずつ案内するルーター。段階的開示の入口。
- 各概念ノート: 1つの目的またはルール群を説明する本文。

# OKF規則

- `index.md`と`log.md`以外のMarkdownには、非空の`type`を含むYAML frontmatterを付ける。
- `title`は人間向けの名称、`description`は索引やLLMのルーティングに使える一文にする。
- 出典は`sources`に記録し、Wiki内の関係は標準Markdownの相対リンクで表す。
- 新しい分野を作る場合、そのディレクトリにも`index.md`を置く。
- 更新内容は[log](log.md)へ新しい日付順で記録する。

# 回答時の原則

Wiki本文は検索と理解のための整理情報であり、ルールの最終的な根拠は原典です。Wiki本文と画像が食い違う場合は原典を優先し、Wikiを修正します。
