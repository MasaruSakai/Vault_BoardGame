---
type: faq
title: ルールFAQ：タイミング・カード・終了
description: 効果をいつ解決できるか、カードをどこに置くか、契約とゲーム終了を具体例で確認するFAQ。
tags: [dune-imperium, uprising, faq, timing, cards, endgame]
language: ja
source_files:
  - ../../Sources/JP_DUNE_IMPERIUM_UPRISING_Rulebook.pdf
  - ../../Sources/bgg-rules-forum.md
timestamp: "2026-09-17"
status: curated
---

# ルールFAQ：タイミング・カード・終了

## 1. 派遣先のコストを、派遣後に得た資源で払える？

**質問。** 指導者の指輪、プレイしたカード、スパイ回収などで資源を得られるなら、先に代行者を置いてからその資源で派遣先のコストを払ってよいか。

**回答。** できない。派遣先のコストは、代行者を置く時点で「直ちに」支払える必要がある。代行者を置いた後に解決するカード効果・マス効果で得た資源を、すでに発生した派遣コストへ遡って使うことはできない。

**具体例。** 水1が必要なマスへ、手持ちの水が0の状態で行き、派遣後にカードから水1を得る、という処理は不可。逆に、派遣前にプレイできるプロット策謀で水を得て、その水を持った状態で派遣するなら可能。

**根拠／確度。** 日本語ルールブック p.9の派遣コストの順序から確定。BGGでも同じ原則が「指導者の指輪で得た資源を派遣コストに使えるか」という類似質問で確認されている。[Can you claim the Signet Ring bonus first?](https://boardgamegeek.com/thread/3103502/can-you-claim-the-signet-ring-bonus-first)

## 2. Stabanの指輪と《Special Mission》は、どちらを先に解決する？

**質問。** Stabanの指輪効果と、派遣・公開中に使えるプロット策謀《Special Mission》が同じ手番に関係する。指輪で得るものを派遣コストやカード効果の前提にできるか。

**回答。** まず「派遣コストの支払い」と「派遣後の効果解決」を分ける。派遣コストは代行者を置く前に満たす。派遣後に指輪やカードの効果を解決する順序は、カード本文が指定しない限り、同じ手番中に処理できる効果の範囲で選ぶ。ただし、派遣後に得た資源で派遣コストを支払ったことにはできない。

**読み違えやすい点。** 《Special Mission》を「派遣先へ行く前」に使えるプロット策謀として扱えるかは、そのカードの本文と使用タイミングを確認する。カードを裏向きに保持したまま、効果だけを先取りすることはできない。

**根拠／確度。** 前半はルールブック p.9から確定。個別カードの最終処理はカード本文を優先する。[Rules question about timing: Staban's ring + Intrigue card Special Mission](https://boardgamegeek.com/thread/3725877/rules-question-about-timing-stabans-ring-plus-intr) は質問の具体例を確認する入口だが、BGG本文だけから公式裁定へ広げない。

## 3. 「カードがプレイ中」とは、どのカード？

**質問。** 代行者の派遣に使ったカード、公開したカード、捨て場のカード、策謀カードのどれを「プレイ中」と数えるのか。

**回答。** そのラウンドに表向きにプレイして自分の前に置いている帝国カードを「プレイ中」として扱う。代行者の派遣に使ったカードは派遣側で処理し、後の公開／説得力の手番で同じカードの下段効果をもう一度適用しない。公開したカードは公開後の自分の前に置かれ、下段効果と公開時の戦力を処理する。捨て場・山札・手札にあるだけのカードはプレイ中ではない。

**具体例。** 先にカードAで代行者を派遣し、後で残りの手札を公開しても、カードAの下段効果は「公開したカード」として再発動しない。

**根拠／確度。** 日本語ルールブック p.12、[説得力の行使とデッキ構築](../concepts/reveal-turn.md)から確定。[“Card in play”](https://boardgamegeek.com/thread/3721163/card-in-play) は用語の具体例を確認するスレッド。

## 4. 手番中に得た報酬は、その手番の後続処理に使える？

**質問。** カードやマスの効果でソラリ・水・香料・カード・部隊などを得たとき、同じ手番の次の効果やカード獲得に使えるか。

**回答。** 効果が解決されて実際に得た後なら、通常は同じ手番の後続処理に使える。ただし、すでに支払うべきだったコストへ遡って使えない。また、「次に」「直ちに」「この手番中に」など、カード本文に順序指定がある場合は本文を優先する。

**確認手順。** ①いま支払うコストか、②効果解決後の任意の支出か、③カード本文の指定があるか、の順に確認する。[Reward during an action](https://boardgamegeek.com/thread/3579989/if-you-get-a-reward-during-a-action-can-you-prefor) のような疑問はこの3段階で分ける。

**根拠／確度。** ①はルールブック p.9で確定、②と③は各カードの本文を確認する。個別カードの文言を省略して一般則だけで裁定しない。

## 5. 契約は、取った手番と同じ手番に達成できる？

**質問。** CHOAMの契約を取った直後、同じ代行者の派遣や収穫で条件を満たしたことにできるか。

**回答。** 契約を取る前にすでに行った派遣や収穫は、その契約の達成には使えない。契約を取った後、同じ手番の後続処理が契約条件を満たすかは、契約の種類と本文に従う。特に「次に指定マスへ派遣したとき」型は、契約取得後の将来の派遣として扱う。

**根拠／確度。** [CHOAMチョアムモジュール](../concepts/choam-module.md) と日本語ルールブック pp.16-17。BGGの[Contracts key rules](https://boardgamegeek.com/thread/3700288/accomplishing-contracts-key-rules) と[Spice Must Flow contract](https://boardgamegeek.com/thread/3691828/completing-spice-must-flow-contract-in-1-turn) は契約ごとの具体例を確認する入口。

## 6. ゲームは必ず7ラウンドで終わる？

**質問。** Strategyで「ラウンド7固定」と言われることがあるが、7ラウンド終了が公式ルールなのか。

**回答。** 固定ではない。ラウンド終了時、誰かの勝利点が10以上、または紛争カードの山が空ならゲーム終了へ進む。それ以外は次ラウンドへ進む。したがって、10点到達のタイミングや紛争カードの残り枚数によって、7ラウンドより前にも後にもなり得る。

**根拠／確度。** 日本語ルールブック pp.14-15、[ゲーム終了と勝敗](../concepts/endgame.md)から確定。[Does the game always should end on round 7?](https://boardgamegeek.com/thread/3738479/does-the-game-always-should-end-on-round-7) は戦略上の経験則と公式終了条件を分けて読む。

## 7. 終盤の策謀カードで、開始時の目標カードを裏返せる？

**質問。** 終盤の策謀カードが「該当する種類の表向き紛争カードを裏返す」とき、開始時の目標カードも対象になるか。

**回答。** 目標カードがルール上「紛争カードとして数える」と明記されているなら対象になる。通常の目標カードを、本文にその扱いがないのに紛争カードとして扱ってはいけない。

**根拠／確度。** カード本文を根拠にする個別裁定。BGGの[Endgame Intrigues: Desert Mouse / Crysknife / Ornithopter](https://boardgamegeek.com/thread/3193526/endgame-intrigues-desert-mouse-crysknife-ornopt) では、開発者が「紛争カードとして数える」と書かれた目標カードは対象になると回答している。

## 未解決・カード本文待ち

- [Edge case with gather intelligence and false orders](https://boardgamegeek.com/thread/3737236/edge-case-with-gather-intelligence-and-false-order) — 「諜報活動」と「False Orders」のどの効果が先かは、カード本文と実際の投稿内容を見て裁定する。タイトルだけで結論を作らない。
- [a question about endgame intrigue](https://boardgamegeek.com/thread/3726680/a-question-about-endgame-intrigue) — 終盤策謀の対象カードが本文上の対象条件を満たすかを個別確認する。

## 関連ページ

- [ルールFAQ・論点ルーティング](rules-faq.md)
- [代行者の派遣](../concepts/agent-turn.md)
- [説得力の行使とデッキ構築](../concepts/reveal-turn.md)
- [ゲーム終了と勝敗](../concepts/endgame.md)
- [CHOAMチョアムモジュール](../concepts/choam-module.md)

# Citations

- [日本語ルールブック](../../Sources/JP_DUNE_IMPERIUM_UPRISING_Rulebook.pdf) — pp. 8-17。
- [BGG Rules Forumの台帳](../../Sources/bgg-rules-forum.md) — 個別スレッドの発見元。
