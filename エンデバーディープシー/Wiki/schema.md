---
type: schema
title: Wiki schema
description: OKF wikiで使うMarkdown frontmatterと出典記法。
tags: [schema, okf]
language: ja
source_files: []
timestamp: 2026-09-18
status: active
---

# Wiki schema

## Frontmatter

~~~yaml
type: concept | faq | strategy | source | entity | index | guide | log
title: ページタイトル
description: 1行要約
tags: [endeavor-deep-sea]
language: ja
source_files: [Sources/画像名.jpg]
timestamp: YYYY-MM-DD
status: active | review | archived
~~~

## 出典

- 一次資料：[マニュアル p.10](../../Sources/エンデバーディープシー - 10.jpg)
- BGGスレッド：投稿タイトルとURLを併記する。
- 1ページ内で一次資料とBGG情報を混ぜる場合は、見出しを分ける。

## 信頼度

本文中に必要に応じて「一次資料確定」「BGG回答確認」「要原文確認」「解釈」を付ける。
