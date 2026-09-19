---
type: concept
title: 手番の進行
description: 開始処理、コントロール確認、コンパイル確認、カード行動、キャッシュ、終了処理の順序。
tags: [compile, rules, turn, timing]
language: ja
source_files:
  - ../../Sources/コンパイル - 2.jpg
  - ../../Sources/コンパイル - 1.jpg
timestamp: "2026-09-19"
status: stable
---

# 手番の進行

手番は次の順に進む。カードテキストが手順を変更する場合は、[カードテキストと解決順](card-text-and-timing.md)を優先する。

1. **開始** — 自分側で見えている「Start」効果を解決する。
2. **コントロール確認** — 2本以上のラインで自分の合計価値が相手より高ければ、コントロールカードを得る。
3. **コンパイル確認** — 条件を満たすなら、該当ラインを1本選んでコンパイルする。条件を満たした場合、この手番の通常行動はコンパイルだけになる。
4. **行動** — コンパイルしなかった場合、自分側のラインにカードを1枚プレイする。プレイできない、またはカードがない場合はリフレッシュする。
5. **キャッシュ確認** — 手札が6枚以上なら、5枚になるまでキャッシュをクリアする。
6. **終了** — 手番を終え、自分側で見えている「End」効果を解決する。

コンパイル前にコントロール確認・プロトコル並べ替えが処理される点は、BGGの[Compile with Control order](https://boardgamegeek.com/thread/3363472/psychic-1-plus-darkness-2-game-winning-combo)および[Controlに関するRulesスレッド一覧](https://boardgamegeek.com/boardgame/406652/compile-main-1/forums/66)でも繰り返し議論されている。
