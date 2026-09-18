---
type: faq
title: Rules FAQ：問題と回答
description: BGG Rulesフォーラムの頻出論点を、日本語マニュアルの根拠と照合して整理。
tags: [faq, rules, bgg]
language: ja
source_files: [Sources/エンデバーディープシー - 8.jpg, Sources/エンデバーディープシー - 10.jpg, Sources/エンデバーディープシー - 16.jpg]
timestamp: 2026-09-18
status: review
---

# Rules FAQ：問題と回答

## 読み方

BGG Rulesフォーラムは2026-09-18時点で249トピック。ここでは、タイトルと確認できた本文・返信から、繰り返し現れる論点を「質問 → 回答 → 根拠」の順に統合した。BGGの返信は公式ルールブックそのものではないため、マニュアルの記述を優先する。

## 基本行動

### Q1. ディスクを1枚使うと、その手番に全ディスクを使えるか

**A.** 1回の専門家起動で使うのは、その起動円に置いたディスクが表す1回分の行動。複数の専門家を起動できるなら、同じ手番中に順に複数回行動できる。手番を終えるかパスしたら、そのワークフェイズ中には戻らない。

根拠：[ラウンド構造](../concepts/round-structure.md)、[BGG「You get to use all your discs…」](https://boardgamegeek.com/thread/3615716/you-get-to-use-all-your-discs-avaible-in-your-turn)

### Q2. 潜水トークンを専門家起動のディスクとして使えるか

**A.** 使えない。潜水トークンは研究またはトークンに記された効果として使う資源であり、起動円へ置くディスクとは別物。

根拠：[潜水・保全・ジャーナル](../concepts/dive-conservation-journal.md)、[BGG「Can a dive token be used as a disc…」](https://boardgamegeek.com/thread/3620761/can-a-dive-token-be-used-as-a-disc-to-activate-the)

### Q3. 潜水トークンはいつ使えるか

**A.** 手番中の適切なタイミングで使う。専門家を起動する前後、専門家アクションの合間に使える効果があるが、準備フェイズで使えるとは限らない。カード/トークンが指定するタイミングを優先する。

根拠：[マニュアル p.11](../../Sources/エンデバーディープシー - 11.jpg)、[BGG「When can you dive?」](https://boardgamegeek.com/thread/3704324/when-can-you-dive)、[BGG「Can you play a dive token during Phase 1…」](https://boardgamegeek.com/thread/3610233/can-you-play-a-dive-token-during-phase-1-of-the-tu)

### Q4. 潜水トークンを複数枚、同じラウンドに使えるか

**A.** 使える。ただし、各トークンの入手・保持上限・研究上限・同じ効果の処理は個別に確認する。手番終了時に保持できる枚数を超えるトークンは残せない。

根拠：[マニュアル p.11](../../Sources/エンデバーディープシー - 11.jpg)、[BGG「Using multiple diving tiles in one round」](https://boardgamegeek.com/thread/3637421/using-multiple-diving-tiles-in-one-round)

## 移動とソナー

### Q5. 移動で開始海域へ戻れるか

**A.** 1回の移動アクション中に、開始海域へ戻ることはできない。複数の移動効果が別々に発生する場合は、各効果の文章と海域特殊ルールを確認する。

根拠：[移動・ソナー・発見](../concepts/travel-sonar-discovery.md)、[BGG「Moving to the Same tile i started from allowed?」](https://boardgamegeek.com/thread/3585231/moving-to-the-same-tile-i-started-from-allowed)

### Q6. 到着ボーナスは、その海域へ入るたびに得るか

**A.** 通常は船が新しい海域へ入ったときに得る。初期配置、再配置、特殊効果による移動は、シナリオや海域の文面で例外がないか確認する。

根拠：[マニュアル p.9](../../Sources/エンデバーディープシー - 9.jpg)、[BGG「Do you do get the Arrival bonus each time…」](https://boardgamegeek.com/thread/3414002/do-you-do-get-the-arrival-bonus-each-time-you-ente)

### Q7. ソナーで引いた2枚は、1枚目を見てから2枚目を引けるか

**A.** 2枚を引いて比較し、合法に配置できる1枚を選ぶ。1枚目を先に配置してから2枚目を判断する処理ではない。

根拠：[マニュアル p.10](../../Sources/エンデバーディープシー - 10.jpg)、[BGG「Looking at the first Ocean board drawn…」](https://boardgamegeek.com/thread/3533657/looking-at-the-first-ocean-board-drawn-before-draw)

### Q8. ソナーで合法な配置がないときはどうするか

**A.** 新しい海域を無理に置かず、マニュアルが指定する代替報酬を受け取る。シナリオの特殊配置、深度、隣接条件を確認してから「合法な配置なし」と判定する。

根拠：[マニュアル p.10](../../Sources/エンデバーディープシー - 10.jpg)、[BGG「Can I still take a Sonar action if there are no more…」](https://boardgamegeek.com/thread/3355412/can-i-still-take-a-sonar-action-if-there-are-no-mo)

### Q9. セットアップで表になった海域の発見ボーナスを得るか

**A.** 通常のソナーによる発見ではないため、セットアップ時に発見ボーナスを得るとは扱わない。シナリオが明示した場合だけ例外。

根拠：[セットアップ](../concepts/setup.md)、[BGG「Do you take the discovery bonus on the tiles disclosed during the setup…」](https://boardgamegeek.com/thread/3550153/do-you-take-the-discovery-bonus-on-the-tiles-discl)

## 保全とジャーナル

### Q10. 保全ディスクは端から置く必要があるか

**A.** サイトの空いている円へ置く。端・中央の指定がある場合は、その海域またはミッション文面を優先する。

根拠：[マニュアル p.11](../../Sources/エンデバーディープシー - 11.jpg)、[BGG「Conserve: do you need to place a disc on the edge…」](https://boardgamegeek.com/thread/3615043/conserve-do-you-need-to-place-a-disc-on-the-edge-o)

### Q11. 無料のジャーナル/公開アクションは研究コストも無料か

**A.** 「無料」が何を免除するかは、そのカードや海域の文言による。追加行動を無料にする効果と、研究コストを免除する効果は同じではない。

根拠：[マニュアル p.12](../../Sources/エンデバーディープシー - 12.jpg)、[BGG「Is a free publication action, also free of research costs」](https://boardgamegeek.com/thread/3650734/is-a-free-publication-action-also-free-of-research)

### Q12. ジャーナルの追加行動は通常の専門家起動か

**A.** 追加行動はカードに指定された独立の効果として処理する。起動円を追加で置く通常起動と同一視しない。ディスクの要否・船の場所・研究コストはカードの文面を確認する。

根拠：[ワークフェイズの行動](../concepts/work-actions.md)、[BGG「Is Journal Action (an Additional Action?)」](https://boardgamegeek.com/thread/3729198/is-journal-action-an-additional-action)

## 専門家とディスク

### Q13. 昇格は必須か

**A.** 昇格は条件を満たしたときに選べる処理として扱う。今の専門家のアクションやディスク配置を残したい場合、昇格のタイミングを見送る判断がある。

根拠：[マニュアル p.13](../../Sources/エンデバーディープシー - 13.jpg)、[BGG「Do i have to promote?」](https://boardgamegeek.com/thread/3631572/do-i-have-to-promote)

### Q14. 昇格時に専門家上のディスクはどうなるか

**A.** 供給へ戻る。昇格後、別の待機ディスクでその専門家を再び起動できる。

根拠：[マニュアル p.13](../../Sources/エンデバーディープシー - 13.jpg)、[BGG「When you promote a specialist…」](https://boardgamegeek.com/thread/3611546/when-you-promote-a-specialist-flip-him-over-and-re)

### Q15. ディスクはラウンド間に移動するか

**A.** 自動的に待機へ戻るわけではない。専門家上、海域上、ジャーナル上に置いたディスクは、それぞれのルールに従って残る。

根拠：[トラックと資源](../concepts/tracks-and-resources.md)、[BGG「Is action discs move between rounds?」](https://boardgamegeek.com/thread/3618814/is-action-discs-move-between-rounds)

### Q16. 専門家を降格できるか

**A.** 通常の任意行動として降格するルールではない。ディスラプションやカードが明示的に裏返す場合だけ、その効果を解決する。過去の昇格報酬を自動的に再取得するとは扱わない。

根拠：[マニュアル p.13](../../Sources/エンデバーディープシー - 13.jpg)、[BGG「Can you demote a specialist…」](https://boardgamegeek.com/thread/3630403/can-you-demote-a-specialist-with-a-journal-card-fo)

## 協力・ソロとミッション

### Q17. 協力/ソロの目標は個人別か全員合算か

**A.** 目標文面に個人指定がないものは、協力では全員の盤面を合わせて判定する。個人ごとの数値・記号を要求する目標は、シナリオ文面に従う。

根拠：[協力・ソロ](../concepts/cooperative-and-solo.md)、[BGG「Co-op scoring」](https://boardgamegeek.com/thread/3517885/co-op-scoring)

### Q18. ミッション3のフィールド記号は何を数えるか

**A.** 海域や獲得ジャーナルに示される対象フィールド記号を確認する。協力では「各プレイヤーが保持」なのか「チーム全体」なのかを、ミッション3の目標文面に従う。

根拠：[ミッション3](../../Sources/エンデバーディープシー - 21.jpg)、[BGG「For Scenario 3 Goal 3, what symbols actually count?」](https://boardgamegeek.com/thread/3598241/for-scenario-3-goal-3-what-symbols-actually-count)

### Q19. 協力の目標が不可能に見える場合、途中で失敗扱いになるか

**A.** 通常はゲーム終了時の必要目標数で判定する。目標カード公開後に達成可能性を確認し、後続ラウンドの船・ディスク・トラックを逆算する。

根拠：[協力・ソロ](../concepts/cooperative-and-solo.md)、[BGG「Mission 7 Goal 3 Coop. Is it even reachable?」](https://boardgamegeek.com/thread/3756978/mission-7-goal-3-coop-is-it-even-reachable)

### Q20. ディスラプションで属性が減ったとき、専門家や船を失うか

**A.** カードが明示する損失だけを適用する。属性低下と、専門家・船・ディスクの除去は別処理であり、連鎖的に失うとは限らない。

根拠：[協力・ソロ](../concepts/cooperative-and-solo.md)、[BGG「Is there a ruling on losing things during setbacks ?」](https://boardgamegeek.com/thread/3390218/is-there-a-ruling-on-losing-things-during-setbacks)

## BGG Rules全件の索引

指定フォーラムは249トピックあり、以下の5ページで全件を確認できる。トピック本文は更新されるため、個別リンクを一次キーとし、上記FAQでは繰り返し現れる論点を正規化した。

- [1–50](https://boardgamegeek.com/boardgame/367966/endeavor-deep-sea/forums/66?pageid=1)
- [51–100](https://boardgamegeek.com/boardgame/367966/endeavor-deep-sea/forums/66?pageid=2)
- [101–150](https://boardgamegeek.com/boardgame/367966/endeavor-deep-sea/forums/66?pageid=3)
- [151–200](https://boardgamegeek.com/boardgame/367966/endeavor-deep-sea/forums/66?pageid=4)
- [201–249](https://boardgamegeek.com/boardgame/367966/endeavor-deep-sea/forums/66?pageid=5)

主な論点群は、潜水トークン、ソナー/深度、移動/到着ボーナス、ジャーナル/保全、専門家の昇格、ディスク位置、協力/ソロ目標、ミッション6〜10の特殊処理に分かれる。
