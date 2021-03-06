# -*- coding: utf-8 -*-

#　23. セクション構造
'''
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
•1行に1記事の情報がJSON形式で格納される
•各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
•ファイル全体はgzipで圧縮される
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

'''

import gzip
import json


#まずイギリスに関する記事を抜き出す。複数存在した場合に対応できないけど、ま、技術の限界
with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        if json_data["title"] == "イギリス":
            cont_eng = json_data

# とりだした x の配列を確認
print(type(cont_eng))
for i in cont_eng:
    print (i)

#ふむふむ、あたりまえだけど
print(cont_eng["title"])
# →　イギリス　　少しわかってきた

#記事の方だけを取り出してみると
text_eng = cont_eng["text"]
print("text_engの型は？", type(text_eng))
print("text_engを表示してみるテスト")
print(text_eng)

#ふむふむ、ここまで来ると、僕でもわかる？なんか愚直だなぁ。
#とくに、「=」の繰り返し回数を自動処理できるとよいのだけど。
text_row = text_eng.split("\n")
section_list=[]

for row_content in text_row:
    if row_content.find("====")>=0:
        section_list.append([row_content.replace("=",""),3])
    elif row_content.find("===")>=0:
        section_list.append([row_content.replace("=",""),2])
    elif row_content.find("==")>=0:
        section_list.append([row_content.replace("=",""),1])

print("セクションの数：" + str(len(section_list)))
print(section_list)
