---
title: World Government Terraforming とゲーム終了判定
type: bgg-topic
forum: Rules
thread_id: 3345792
source_url: https://boardgamegeek.com/thread/3345792/rules-question
captured_at: 2026-09-17
tags: [world-government, solo, game-end, solar-phase]
---

# World Government Terraforming とゲーム終了判定

## 質問

ソーラーフェイズの World Government Terraforming（世界政府によるテラフォーミング）で最後のグローバルパラメータを満たした場合、その場でゲームが終わるのか、次の世代があるのか、という確認。スレッドでは別件として、上限を超えて置かれたフローターの「最大値」が何を制限するかも扱われている。

## 結論

ゲーム終了チェックはソーラーフェイズの先に行われ、World Government Terraforming はその後の処理として行われる。このため、World Government の処理で最後のパラメータが目標に達しても、その処理の直後に現在世代が巻き戻ったり、途中で最終得点へ移ったりはしない。次の世代へ進み、規定の終了タイミングでゲーム終了を処理する。

この読み方は「パラメータが達成された瞬間にゲームを止める」のではなく、ルールが指定したフェイズ境界で終了を確認する、という Terraforming Mars の基本構造と一致する。

## 応用メモ

- ソーラーフェイズ開始時の終了チェックと、同フェイズ中の世界政府処理を分けて考える。
- 世界政府で上げるパラメータにも、通常どおりグローバルパラメータの上限がある。
- 別件の Saturn Surfing では、カードの「Max 5」がフローター数全体ではなく、そのアクションで得るM€にかかる、という整理も示されている。カード上の Max がどの効果に付属しているかを読むこと。

## 出典

- [BGG: Rules Question](https://boardgamegeek.com/thread/3345792/rules-question)
- [Sources の日本語マニュアル](../TM_RULEBOOK_JPN-reprint2018w.pdf)
