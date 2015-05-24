# -*- coding: utf-8 -*-

import MeCab,re

# neko.txt.mecabの読み込み
with open("../data/neko.txt.mecab", encoding="utf8") as f:
    text=f.readlines() # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音（読み、発音はないものも存在）


# 初期化
pattern=re.compile(r"(?P<surface>.+)\t(?P<pos>[^,]+),(?P<pos1>[^,]+),(?P<pos2>[^,]+),(?P<pos3>[^,]+),(?P<conjForm>[^,]+),(?P<conjType>[^,]+),(?P<base>[^,]+),?(.*)")
list=[]
dic={}

# list[dic[0],dic[1],dic[2],...]形式で形態素を収納
for i,line in enumerate(text):
    if line=="EOS\n":
        continue
    dic[i]={}
    surface,pos,pos1,base=pattern.match(line).group("surface","pos","pos1","base")
    dic[i]["surface"]=surface
    dic[i]["pos"]=pos
    dic[i]["pos1"]=pos1
    dic[i]["base"]=base
    list.append(dic[i])

print("隊長！　list に格納しました！")
