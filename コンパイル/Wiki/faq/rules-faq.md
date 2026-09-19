---
type: faq
title: Rules FAQ：質問と回答
description: コンパイルのルール画像とBGG Rulesフォーラムの主要質問を、回答・根拠・注意点の順に整理する。
tags: [compile, faq, rules, bgg]
language: ja
source_files:
  - ../../Sources/コンパイル - 1.jpg
  - ../../Sources/コンパイル - 2.jpg
  - ../sources/bgg-rules-forum.md
timestamp: "2026-09-19"
status: review
---

# Rules FAQ：質問と回答

## 読み方

BGG Rulesは2026-09-19確認時点で277トピックある。ここでは、本文と返信を確認できた質問、およびルール画像から繰り返し参照される判断を、質問→回答→根拠の順に正規化した。BGGの返信はコミュニティ／デザイナー補足であり、ルール画像と食い違う場合は画像を優先する。

## BGG本文を確認した質問

### Q1. 「相手のカードを1枚シフトする」とき、移動先は誰が決めるか

**A.** 効果を書いたカードの所有者が、対象カードと移動先のスタックを決める。対象カードの所有者が決めるのではない。

根拠：[When I shift an opponent card, who decides where it goes?](https://boardgamegeek.com/thread/3760686/when-i-shift-an-opponent-card-who-decides-where-it)、[カードテキストと解決順](../concepts/card-text-and-timing.md)。

### Q2. 「Discard 1 card」は相手の手札を捨てさせられるか

**A.** 特に指定がなければ、自分の手札から1枚を自分のトラッシュへ移す。相手の手札を対象にするには、カードが相手を明示する必要がある。

根拠：[Discarding your opponent's cards](https://boardgamegeek.com/thread/3760026/discarding-your-opponents-cards)、[手札・デッキ・トラッシュ](../concepts/hand-deck-trash.md)。

## 基本ルール

### Q3. コンパイル条件は何か

**A.** 自分側の合計価値が10以上で、同じラインの相手側の合計より大きいこと。条件を満たすラインを1本選び、両者のそのラインのカードをトラッシュし、プロトコルをコンパイル済みにして1枚引く。

根拠：[コンパイルと勝利](../concepts/compile-and-win.md)、`コンパイル - 1.jpg`。

### Q4. 複数ラインが同時にコンパイル条件を満たしたらどうするか

**A.** その手番のプレイヤーが1本を選ぶ。1回のコンパイルで処理するのは1ラインである。

根拠：[コンパイルと勝利](../concepts/compile-and-win.md)、`コンパイル - 1.jpg`。

### Q5. コントロール確認とコンパイル確認はどちらが先か

**A.** 手番のコントロール確認・プロトコル並べ替えを先に処理し、その後にコンパイルを確認する。残り1プロトコルの場面では、必要なプロトコルを勝利ラインへ移してからコンパイルする判断がある。

根拠：[手番の進行](../concepts/turn-structure.md)、[コントロールと並べ替え](../concepts/control-and-rearrange.md)、[BGG Compile with Control order](https://boardgamegeek.com/thread/3556795/extremely-long-games-due-to-control)。

### Q6. 表向きカードを対応しないラインに置けるか

**A.** 置ける。ただし、表向きカードのプロトコル表示とラインが一致しないなら、そのカードの中央コマンドは解決しない。配置自体が禁止されるわけではない。

根拠：[ライン・スタック・コマンド](../concepts/lines-stacks-commands.md)、`コンパイル - 2.jpg`。

### Q7. 中央コマンドはいつ解決するか

**A.** カードをプレイ、反転、公開して中央コマンドが見えた直後に解決する。新しく見えたテキストは、他のテキストに割り込む。

根拠：[カードテキストと解決順](../concepts/card-text-and-timing.md)、`コンパイル - 1.jpg`。

### Q8. 効果の対象や移動先は誰が選ぶか

**A.** 効果を持つカードの所有者が選ぶ。対象カードが相手側にあっても、カード所有者が自分なら自分が選択する。

根拠：BGG [When I shift an opponent card, who decides where it goes?](https://boardgamegeek.com/thread/3760686/when-i-shift-an-opponent-card-who-decides-where-it)、[カードテキストと解決順](../concepts/card-text-and-timing.md)。

### Q9. 覆われたカードは通常の効果の対象になるか

**A.** 通常はならない。特に「覆われたカード」などと指定された効果だけが、覆われたカードを対象にする。

根拠：[ライン・スタック・コマンド](../concepts/lines-stacks-commands.md)、`コンパイル - 1.jpg`。

### Q10. 相手のカードを公開した場合、その中央コマンドを誰が解決するか

**A.** カードの所有者が解決する。カードを公開したプレイヤーや、カードが置かれている側のプレイヤーに自動的に処理権が移るわけではない。

根拠：[カードテキストと解決順](../concepts/card-text-and-timing.md)、`コンパイル - 1.jpg`。

### Q11. カードを重ねたとき、下のカードはどう扱うか

**A.** 新しいカードを既存カードの上に置く。価値と上段コマンドが見えるように重ね、カードが覆われたことで見えなくなった中央／下段テキストは有効でなくなる。

根拠：[ライン・スタック・コマンド](../concepts/lines-stacks-commands.md)。

### Q12. リフレッシュでデッキが足りない場合はどうするか

**A.** 残りのデッキをすべて引き、トラッシュをシャッフルして新しいデッキにし、手札が5枚になるまで続ける。デッキもトラッシュも空なら、引けるカードはない。

根拠：[手札・デッキ・トラッシュ](../concepts/hand-deck-trash.md)、`コンパイル - 2.jpg`。

### Q13. 手札が6枚以上になったらどうするか

**A.** キャッシュをクリアし、5枚になるまで手札をトラッシュする。カード効果が明示的に別の上限を指定する場合は、その効果を優先する。

根拠：[手札・デッキ・トラッシュ](../concepts/hand-deck-trash.md)、`コンパイル - 2.jpg`。

### Q14. デッキもトラッシュも空のとき、ドロー以外の効果は止まるか

**A.** 実行できないドロー部分だけを飛ばし、同じ効果内に実行可能な別の処理があれば続ける。

根拠：[カードテキストと解決順](../concepts/card-text-and-timing.md)、`コンパイル - 1.jpg`。

### Q15. コントロールカードでプロトコルをどう動かすか

**A.** リフレッシュ時、コントロールカードを持つプレイヤーがプロトコルの位置を変更する。プロトコルを裏返すことはできず、ライン内のコマンドカードは移動しない。

根拠：[コントロールと並べ替え](../concepts/control-and-rearrange.md)、`コンパイル - 1.jpg`。

### Q16. プロトコルを並べ替えたら、コマンドカードも一緒に移るか

**A.** 移らない。プロトコルの位置だけが変わり、各ラインのコマンドカードはその場に残る。

根拠：[コントロールと並べ替え](../concepts/control-and-rearrange.md)。

### Q17. 「Discard」と「Delete」の違いは何か

**A.** Discardは手札のカードをトラッシュへ移す。Deleteは場にあるカードをトラッシュへ移す。

根拠：[手札・デッキ・トラッシュ](../concepts/hand-deck-trash.md)、`コンパイル - 1.jpg`。

### Q18. ルールとカードテキストが食い違ったらどちらが優先か

**A.** カードテキストを優先する。ただし、カードが指定していない部分は一般ルールで処理する。

根拠：[カードテキストと解決順](../concepts/card-text-and-timing.md)、`コンパイル - 1.jpg`。

### Q19. 表向き／裏向きカードの情報は誰が見られるか

**A.** 自分側の裏向きカードは自分が自由に確認できる。場の表向きカード、トラッシュの裏向きカード、手札、削除されたカードは公開情報として扱う。

根拠：`コンパイル - 1.jpg`。

### Q20. カードの所有権が変わったらどうなるか

**A.** 新しい所有者がそのカードを支配し、以後その所有者側の同じラインに置かれているカードとして扱う。効果が所有者を指定する場合は、現在の所有者を基準にする。

根拠：`コンパイル - 1.jpg`、[カードテキストと解決順](../concepts/card-text-and-timing.md)。

## 追加のルール論点

Rulesフォーラムには、Hate 3／Hate 1、Gravity 1／2、Assimilation 2、Control、Spirit 3、Fire 3、Water 1、War 0、Corruption 2など、特定カードの相互作用を扱うトピックもある。カード固有の文面を裁定する際は、まず画像のカード文面と本FAQの一般原則を確認し、必要なら[原フォーラム](https://boardgamegeek.com/boardgame/406652/compile-main-1/forums/66)の個別スレッドを開く。
