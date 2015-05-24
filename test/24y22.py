# -*- coding: utf-8 -*-

'''
24. ファイル参照の抽出
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
•1行に1記事の情報がJSON形式で格納される
•各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
•ファイル全体はgzipで圧縮される
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．

記事から参照されているメディアファイルをすべて抜き出せ．

'''

import gzip,json,re

# lineをstr1,str2で切って間に挟まれる部分をprintする
# str1がなければ1を返す
def findCut(line,str1,str2):
    start=line.find(str1)
    if start<0:
        return 1
    else:
        start+=len(str1)
        stop=line[start:-1].find(str2)
        print(line[start:start+stop])
        return 0

# jawiki-country.josn.gzからtitle=イギリスのtextを\n区切りでtextに収納
with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
       json_data=json.loads(line)
       if json_data["title"] == "イギリス":
             text = json_data["text"].split("\n")

# MAIN
for line in text:
    findCut(line,"ファイル:","|")
    findCut(line,"File:","|")

