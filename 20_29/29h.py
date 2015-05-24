# -*- coding: utf-8 -*-

# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

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
        dic[key] = value
    else:
        dic[key] += row
        print("xxx" + row)

for keys, values in dic.items():
    print(keys + ":" + values)

URL = "http://ja.wikipedia.org/w/ファイル:" + dic['国旗画像']
print(URL)
