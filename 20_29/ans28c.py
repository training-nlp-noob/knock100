#!/usr/bin/env python
# coding=utf-8

#Q28
#マークアップの削除

import gzip,json,re

with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
       json_data=json.loads(line)
       if json_data["title"] == "イギリス":
             text = json_data["text"]

#http://d.hatena.ne.jp/yumimue/20071220/1198141598

# "{{"から ""}}""を探して抜き出してみたかったけど挫折
#print(text)
# 正規表現を使い、基礎情報のテンプレートの範囲を抜き出す。行毎にsplitする。一つの配列にはkey=valueという形で格納されている。
temp = re.compile(r"(\|略名)(.+)(注記)(.+?\n)",re.S).search(text).group().split("\n")

#print(temp)
# 公式国名のエラー回避を考える
# |で始まる行がkey

dic = {}
for row in temp:
    if row.find("|") == 0:
        row = row.replace("|","").replace (" = ","=")
        demark = row.find("=")
        key = row[:demark]
        value = row[demark+1:]
        dic[key] = value
    else :   #公式国名
        dic[key] += row


def remove_markdown1 (d_obj,pat):
    for n in d_obj:
        d_obj[n] = re.sub(pat,"",d_obj[n])
    return(d_obj)

# http://docs.python.jp/3.4/howto/regex.html#grouping
# re.sub(pattern, repl, string, count=0, flags=0)
#  のところを参照

def remove_markdown2 (d_obj,pat):
    for n in d_obj:
        d_obj[n] = re.sub(pat, r"\0", d_obj[n])
    return(d_obj)

#名前つけたときの取り出し方がわかんない
# コンパイルしてないけどいいのかしら・

dic = remove_markdown1 (dic, r"'")
dic = remove_markdown2 (dic, r"\[\[ファイル:(.+?)\]\]")
dic = remove_markdown2 (dic, r"\[\[Category:(.+?)\]\}")
dic = remove_markdown2 (dic, r"\[http:(.+?)\]")
dic = remove_markdown1 (dic, r"\[\[|\]\]")

for p in dic.items():
    print(p)
    print("=========")
