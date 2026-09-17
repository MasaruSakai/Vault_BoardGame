---
type: concept
title: 世代の進行
description: 手番順、研究開発、アクション、産出の4フェイズと、各世代での手番の処理。
tags: [terraforming-mars, generations, phases, turn-order]
sources:
  - id: rulebook-page-08
    resource: ../references/source-pages/rulebook-page-08.jpg
    title: 日本語版ルール説明書 8ページ
  - id: rulebook-page-11
    resource: ../references/source-pages/rulebook-page-11.jpg
    title: 日本語版ルール説明書 11ページ
  - id: rulebook-page-12
    resource: ../references/source-pages/rulebook-page-12.jpg
    title: 日本語版ルール説明書 12ページ
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

# 世代の進行

ゲームは次の4フェイズを世代ごとに順番に実行する。

## 1. 手番順フェイズ

親マーカーをすぐ左隣へ渡し、受け取ったプレイヤーが新しい親になる。世代マーカーを1つ上げる。ただし最初の世代はこのフェイズを飛ばす。

## 2. 研究開発フェイズ

各プレイヤーはプロジェクトの山から4枚引き、0～4枚を1枚3M€で手札に購入する。購入しなかったカードは裏向きで捨て札にする。手札上限はない。

プロジェクトの山が尽きたら、捨て札をシャッフルして新しい山を作る。最初の世代はこのフェイズも飛ばす。

## 3. アクション・フェイズ

親から時計回りに進み、各プレイヤーは自分の手番で1つまたは2つのアクションを実行するか、パスする。2つのアクションは同じ種類でもよく、組み合わせも自由。

1回でもアクションを実行したプレイヤーは、他のプレイヤーの手番の後も再び手番を得る。パスしたプレイヤーはその世代のアクション・フェイズから抜ける。全員がパスするとフェイズ終了。

選べるアクションは[アクション](actions.md)にまとめる。

## 4. 産出フェイズ

全プレイヤーが同時に処理する。

1. プレイヤーボードの電力ボックスにある全電力を発熱ボックスへ移す。
2. M€を「TR + M€産出量」だけ、その他の一般資源を各産出量だけ得る。新たな資源は対応するボックスに置く。
3. 使用済みの青いアクションカードからプレイヤー・マーカーを除去し、次の世代に再使用できるようにする。

グローバル・パラメータがすべて最大値に到達している場合は、この産出フェイズの後にゲームを終了する。終了時の追加の植物変換については[ゲーム終了と得点計算](game-end-and-scoring.md)を参照。
