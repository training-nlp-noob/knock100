#!/usr/bin/env python
# coding=utf-8

#Q26
#強調表現の削除

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

print(dic)


"""
print(len(temp))
print (len(dic.keys()))
print ("keyの一覧")
print(dic.keys())
print ("===valueの一覧===")
print(dic.values())
"""
dic2  = dic
for n in dic2.keys():
    new_value = dic2[n].replace("'", "")
    dic2[n] = new_value

"""
print("強調表現削除後")
print(dic2.values())
"""

print(dic2)
