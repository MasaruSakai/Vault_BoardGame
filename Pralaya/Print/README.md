# Pralaya 印刷用パック

## 推奨：ローソンのB5普通紙・直出し

ローソンのネットプリントを使う場合は、次の2つのPDFを登録してください。どちらもB5縦の読み順で作成してあり、1ページを1枚のB5普通紙にそのまま印刷します。折る・切る・留める作業は不要です。

- `output/pdf/Pralaya_Chinese_Rule_Summary_B5_Lawson_Straight.pdf`
  - 简体中文のルール要約。B5片面でページ順に印刷
- `output/pdf/Pralaya_FAQ_Trilingual_B5_Lawson_Straight.pdf`
  - 日本語、English、简体中文を言語ごとに分けたFAQ。B5片面でページ順に印刷

印刷手順：

1. PDFをローソンのネットプリントへ登録する。
2. 店頭で「普通紙」→「B5」を選ぶ。
3. 片面印刷・原寸で印刷する。拡大・縮小や小冊子設定は使用しない。
4. 出てきたB5用紙を、ページ順のまま使用する。折り・裁断・ホチキス留めは不要。

中国語要約とFAQは別々のPDFとして印刷してください。ローソンの普通紙ネットプリントはB5に対応しています。

## 旧方式（保管用）

以下は以前の用途・方式のPDFです。既存資料との互換性のため削除していません。今回のローソン印刷には、上記のB5直出しPDFを優先してください。

## ファイル

- `output/pdf/Pralaya_Chinese_Rule_Summary_B5_Lawson_Straight.pdf`
  - ローソン用の新規版。B5縦・片面・読み順ページ
- `output/pdf/Pralaya_FAQ_Trilingual_B5_Lawson_Straight.pdf`
  - ローソン用の新規版。B5縦・片面・読み順ページ。表紙、3言語のQ1〜Q12、Sourcesで全8ページ
- `output/pdf/Pralaya_Chinese_Rule_Summary_B5_Lawson_Booklet.pdf`
  - 旧ファイル。新しい直出し版では使用しない
- `output/pdf/Pralaya_FAQ_Trilingual_B5_Lawson_Booklet.pdf`
  - 旧ファイル。新しい直出し版では使用しない
- `output/pdf/Pralaya_Chinese_Rule_Summary_B7_BoxInsert_A4_4up_SingleSided.pdf`
  - 箱内保存用。A4縦・片面・B7相当（90×125mm）4面付け済み
  - トンボと中央の裁断位置に沿って切り分け、ページ番号順に重ねて小型ホチキスまたはクリップ留めする
  - A4用紙2枚で8ページ。折りだけでA6になる方式ではなく、裁断・重ね留めで箱内サイズに合わせる
  - 印刷設定は「実際のサイズ（100%）」を推奨
- `output/pdf/Pralaya_Chinese_Rule_Summary_A5_Booklet_A4_2up_SingleSided.pdf`
  - 通常印刷用。A4横・片面・A5 2面付け済み
  - 箱に入れず、机上で読むための大きめの版。既存ファイルは削除せず残している
- `output/pdf/Pralaya_FAQ_Trilingual_A4_SingleSided.pdf`
  - A4縦・片面・全3ページ
  - 日本語、English、简体中文を各1ページに分離
  - タイトルと注意書きは日本語ページ冒頭に配置し、独立した表紙・Sourcesページ・Local source filesは収録していない
  - FAQ本文だけで確認できるよう、Web接続なしで必要な結論を読める構成
- `output/pdf/Pralaya_Chinese_Rule_Summary_A4_6Panel_Duplex_FoldOnly.pdf`
  - 旧案。A4横・両面・複数回折り。新しいローソン用B5冊子版を優先する
- `output/pdf/Pralaya_FAQ_Trilingual_A4_6Panel_Duplex_FoldOnly.pdf`
  - 旧案。A4横・両面・複数回折り。既存資料として保管する

## 旧方式の印刷

1. 中国語B7要約は本文を70〜90g/m²程度にする。表紙や用語表だけ120〜160g/m²にしてもよい。
2. A4を片面印刷し、B7の裁断位置で切る。B7ページは2列×2段で配置される。
3. 切り分けたページを1〜8の順に重ね、小型ホチキス1〜2か所またはクリップで留める。折り線は不要。
4. FAQはA4片面で印刷し、必要なら言語ごとに切り離して使う。日本語ページ、Englishページ、简体中文ページはそれぞれ単独で読める。
5. 各PDFには`2018 Revised Edition`を表示している。原版や旧版のルールと混在させない。

## 元資料と出典

- [簡体字中国語マニュアル](../Sources/Pralaya_Rulebook_ZH-CN.md)
- [日本語FAQ](../Wiki/concepts/faq-revised-ja.md)
- [简体中文FAQ](../Wiki/concepts/faq-revised-zh-cn.md)
- [Wikiのソース登録](../Wiki/sources/source-register.md)

旧A4片面FAQは出典URLを本文に載せず、プレイ中のオフライン参照を優先しています。新しいB5版FAQにはSourcesページとWeb URLを収録しています。Web出典とローカル原資料の対応はWikiおよび本READMEで管理します。
