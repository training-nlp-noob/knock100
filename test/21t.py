# -*- coding: utf-8 -*-

# Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import gzip
import json
import re

eng_json = []
repattern = re.compile("イギリス",re.U)

# 以下で記事中に、文字列"イギリス"を含む記事の題名と内容を集めた辞書オブジェクトを作成

with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    print(wiki[wiki.keys()[2]]["title"])

#                 for line in wiki:
#        print(line)


    #json_data = json.loads[wiki(1)]
#print(json_data)

'''
        m = repattern.search(json_data["text"])
        if m:
            art = {"title":json_data["title"] , "text":json_data["text"]}
            eng_json.append(art)

pattern = re.compile("Category")

for i in eng_json:
    m = pattern.search(i["text"])
    if m:
        print (i["title"])
        print (i["text"])
'''
