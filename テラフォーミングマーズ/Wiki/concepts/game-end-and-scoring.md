---
type: concept
title: ゲーム終了と得点計算
description: 3つのグローバル・パラメータが最大に到達した後の終了処理、最終得点、同点判定。
tags: [terraforming-mars, end-game, scoring, victory-points]
sources:
  - id: rulebook-page-03
    resource: ../references/source-pages/rulebook-page-03.jpg
    title: 日本語版ルール説明書 3ページ
  - id: rulebook-page-05
    resource: ../references/source-pages/rulebook-page-05.jpg
    title: 日本語版ルール説明書 5ページ
  - id: rulebook-page-08
    resource: ../references/source-pages/rulebook-page-08.jpg
    title: 日本語版ルール説明書 8ページ
  - id: rulebook-page-12
    resource: ../references/source-pages/rulebook-page-12.jpg
    title: 日本語版ルール説明書 12ページ
  - id: rulebook-page-14
    resource: ../references/source-pages/rulebook-page-14.jpg
    title: 日本語版ルール説明書 14ページ
  - id: rulebook-pdf
    resource: ../../Sources/TM_RULEBOOK_JPN-reprint2018w.pdf
    title: 日本語版ルール説明書 PDF
generated: { by: agent/codex, at: "2026-09-17" }
source_files:
  - ../../Sources/TM_RULEBOOK_JPN-reprint2018w.pdf
language: ja
timestamp: "2026-09-17"
status: stable
---

# ゲーム終了と得点計算

## 終了タイミング

海洋面積率、気温、酸素濃度の3つがすべて最大値に到達したら、その世代を最後まで処理する。現在の世代の産出フェイズを終えた後、手番順に各プレイヤーへ植物を緑地タイルへ変換する最後の機会を与える。これに伴う酸素上昇、TR上昇、配置ボーナスなども処理してから最終得点を計算する。

## 得点の順序

| 順 | 得点源 | 得点 |
| ---: | --- | --- |
| 1 | TR | ゲーム終了時のTRがそのままVP |
| 2 | 褒賞 | 各褒賞の首位5VP、次席2VP。2人プレイでは次席なし |
| 3 | 称号 | 獲得した称号1つにつき5VP |
| 4 | ゲーム盤 | 緑地タイル1枚1VP。各都市は隣接する緑地1枚につき1VP（所有者不問） |
| 5 | カード | まずカード上の資源によるVP、その後にプレイ済みカードのVPを計上 |

カード上の資源によるVPを先に数え、次にプレイ済みの全カード（イベントを含む）に記載されたVPを数える。イベントはカードに直接書かれたVPだけを得て、タグは終了時のタグ数に含めない。手札に残った未プレイのカードは得点にならない。木星タグでVPになるカードなど、タグを条件とするカードは別途確認すると集計しやすい。

最もVPが多いプレイヤーが勝者。同点なら、その中でM€を最も多く持つプレイヤーが勝者となる。

## 集計上の細則

- 複数の効果が同時に発生する場合、他プレイヤーが引き金を引いた場合でも、手番プレイヤーが解決順を決める。
- カードの効果は基本的に加算する。
- 割引後の支払いコストの下限は0M€で、マイナスにはならない。
- 同じタグを複数持つカードをプレイするときは、タグの数だけカードをプレイしたものとして扱う。
- タグを参照するときは、今プレイしたカード自身のタグも参照する。
- カード上の資源を参照するときは、特記がない限り、そのカード上の資源だけを参照する。
