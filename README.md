# 青空文庫API

## 機能

+ タイトルで検索したい場合
````
/title=<検索したいタイトル(一部でも可)>
````
に対してGETリクエストを送ることでjson形式で関連する情報を返します

以下、人間失格を検索した場合の例です
```example.json
'{"ID":{"7687":301},
"title":{"7687":"人間失格"},
"title_read":{"7687":"にんげんしっかく"},
"ソート用読み":{"7687":"にんけんしつかく"},
"sub_title":{"7687":null},
"sub_title_read":{"7687":null},
"origin_title":{"7687":null},
"first_books":{"7687":"「展望」筑摩書房、1948（昭和23）年6～8月号"},
"janle_number":{"7687":"NDC 913"},
"文字遣い種別":{"7687":"新字新仮名"},
"作品著作権フラグ":{"7687":"なし"},
"公開日":{"7687":"1999-01-01"},
"最終更新日":{"7687":"2014-09-17"},
"図書カードURL":{"7687":"https:\\/\\/www.aozora.gr.jp\\/cards\\/000035\\/card301.html"},
"writer_ID":{"7687":35},"last_name":{"7687":"太宰"},
"first_name":{"7687":"治"},"last_name_read":{"7687":"だざい"},
"first_name_read":{"7687":"おさむ"},
"姓読みソート用":{"7687":"たさい"},
"名読みソート用":{"7687":"おさむ"},
"first_name_alphabet":{"7687":"Dazai"},
"last_name_alphabet":{"7687":"Osamu"},
"役割フラグ":{"7687":"著者"},
"birthday":{"7687":"1909-06-19"},
"dead_day":{"7687":"1948-06-13"},
"人物著作権フラグ":{"7687":"なし"},
"底本名1":{"7687":"人間失格"},
"底本出版社名1":{"7687":"新潮文庫、新潮社"},
"底本初版発行年1":{"7687":"1952（昭和27）年10月30日、1985（昭和60）年１月30日100刷改版"},
"入力に使用した版1":{"7687":"1985（昭和60）年１月30日100刷改版"},
"校正に使用した版1":{"7687":"1998（平成10）年3月5日136刷"},
"底本の親本名1":{"7687":null},
"底本の親本出版社名1":{"7687":null},
"底本の親本初版発行年1":{"7687":null},
"底本名2":{"7687":null},
"底本出版社名2":{"7687":null},
"底本初版発行年2":{"7687":null},
"入力に使用した版2":{"7687":null},
"校正に使用した版2":{"7687":null},
"底本の親本名2":{"7687":null},
"底本の親本出版社名2":{"7687":null},
"底本の親本初版発行年2":{"7687":null},
"入力者":{"7687":"細渕真弓"},
"校正者":{"7687":"八巻美恵"},
"テキストファイルURL":{"7687":"https:\\/\\/www.aozora.gr.jp\\/cards\\/000035\\/files\\/301_ruby_5915.zip"},
"テキストファイル最終更新日":{"7687":"2011-01-09"},
"テキストファイル符号化方式":{"7687":"ShiftJIS"},
"テキストファイル文字集合":{"7687":"JIS X 0208"},
"テキストファイル修正回数":{"7687":5.0},
"XHTML\\/HTMLファイルURL":{"7687":"https:\\/\\/www.aozora.gr.jp\\/cards\\/000035\\/files\\/301_14912.html"},
"XHTML\\/HTMLファイル最終更新日":{"7687":"2011-01-09"},
"XHTML\\/HTMLファイル符号化方式":{"7687":"ShiftJIS"},
"XHTML\\/HTMLファイル文字集合":{"7687":"JIS X 0208"},
"XHTML\\/HTMLファイル修正回数":{"7687":1.0}}'
```
とりあえず公式に提供されている情報はすべて返すようにしています。

また、
````angular2
/first_name=<検索したい作家の名前>
````
や
````
/last_name=<検索したい作家の苗字>
````
でリクエストを送ることで、名前から作家の出している本の情報を得ることができます。

<br>順次機能を追加していく予定です。

<br>プルリク、issue待ってます。
