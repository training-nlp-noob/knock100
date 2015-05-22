# -*- coding: utf-8 -*-

"""
 # Q30
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
→ 日本語の意味が？？？
1形態素が 1辞書
全体で1個のlist
listの各要素は辞書

"""

import re

def f30(mecab_file) : # 引数にファイルを与える
    f=open( mecab_file, encoding="utf8")
    text=f.readlines() # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音（読み、発音はないものも存在）
    f.close()
    pattern=re.compile(r"(?P<surface>.+)\t(?P<pos>[^,]+),(?P<pos1>[^,]+),(?P<pos2>[^,]+),(?P<pos3>[^,]+),(?P<conjForm>[^,]+),(?P<conjType>[^,]+),(?P<base>[^,]+),?(.*)")
    dic_list=[]
# dic_list[dic,dic,dic,...]形式で形態素を収納
    for line in text:
        if line=="EOS\n":
            continue
        dic={} #各要素を初期化
        surface,pos,pos1,base=pattern.match(line).group("surface","pos","pos1","base")
        dic["surface"]=surface
        dic["pos"]=pos
        dic["pos1"]=pos1
        dic["base"]=base
        dic_list.append(dic)
    return(dic_list)

if __name__ == '__main__':
    rslt = f30 ("./data/neko.txt.mecab")
    for i in rslt:
        print(i)
