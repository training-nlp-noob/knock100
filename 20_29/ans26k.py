# -*- coding: utf-8 -*-
'''
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
•1行に1記事の情報がJSON形式で格納される
•各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
•ファイル全体はgzipで圧縮される
20 Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
25 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
'''

import gzip,json,re

with gzip.open("../data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
       json_data=json.loads(line)
       if json_data["title"] == "イギリス":
             text = json_data["text"]


# 正規表現を使い、基礎情報のテンプレートの範囲を抜き出す。行毎にsplitする。一つの配列にはkey=valueという形で格納されている。
temp = re.compile(r"(\|略名)(.+)(注記)(.+?\n)",re.S).search(text).group().split("\n")

# 正規表現でkeyとvalueに分解して、辞書オブジェクトに再生成する。dic['公式国名']だけ複数行にvalueがまたがっているので、ifで回避している。
dic = {}
for row in temp:
    if re.compile(r"(\|)(.+)(\s=\s)(.+)").search(row):
        key,value = re.compile(r"(\|)(.+)(\s=\s)(.+)").search(row).group(2,4)
        dic[key] = value.replace("'","") #置換しただけ
    else:
        dic[key] += row

#最後の表示を書き換え
for keys, values in dic.items():
    print(keys + ":" + values)
