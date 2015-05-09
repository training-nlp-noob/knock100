# -*- coding: utf-8 -*-

'''
31. 動詞
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

動詞の表層形をすべて抽出せよ．
'''

import MeCab,re

'''
# neko.txt.mecabの作成
f=open("./data/neko.txt", encoding="utf8")
text=f.read()
f.close()

f = open('./data/neko.txt.mecab', 'w', encoding="utf8")
tagger=MeCab.Tagger()
result=tagger.parse(text)
f.write(result)
f.close()
'''


# neko.txt.mecabの読み込み
f=open("./data/neko.txt.mecab", encoding="utf8")
text=f.readlines() # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音（読み、発音はないものも存在）
f.close()

# 初期化
pattern=re.compile(r"(?P<surface>.+)\t(?P<pos>[^,]+),(?P<pos1>[^,]+),(?P<pos2>[^,]+),(?P<pos3>[^,]+),(?P<conjForm>[^,]+),(?P<conjType>[^,]+),(?P<base>[^,]+),?(.*)")
list=[]
dic={}

# list[dic[0],dic[1],dic[2],...]形式で形態素を収納
for i,line in enumerate(text):
    if line=="EOS\n":
        break
    dic[i]={}
    surface,pos,pos1,base=pattern.match(line).group("surface","pos","pos1","base")
    dic[i]["surface"]=surface
    dic[i]["pos"]=pos
    dic[i]["pos1"]=pos1
    dic[i]["base"]=base
    list.append(dic[i])
    
# 品詞が動詞なら、表層形を表示
for item in list:
    if item["pos"]=="動詞":
        print(item["surface"])
