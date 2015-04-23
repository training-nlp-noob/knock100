# -*- coding: utf-8 -*-

# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import gzip
import json
import re

eng_json = []
repattern = re.compile("イギリス",re.U)

# 以下で記事中に、文字列"イギリス"を含む記事の題名と内容をピックアップ（もともとよみこんだjson_dataはdictなのでそのまま格納）

with gzip.open("../data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
        json_data = json.loads(line)
        m = repattern.search(json_data["text"])
        if m:
            eng_json.append(json_data)

pattern = re.compile("Category")

for i in eng_json:
    m = pattern.search(i["text"])
    if m:
        print (i["title"])
        print (i["text"])

# 少し問題文の意味が分からなかったので、取り合えず記事中に"Category"という文字列があるかないかで判断しています。
# カテゴリ名を抽出して一致させることも出来るのですが、次の問題のようなので...
