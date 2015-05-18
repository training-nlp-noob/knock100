#!/usr/bin/env python3
#coding:utf-8

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ
"""

"""
1個めの要素から最後から2つ前までの要素をとってきて、
順にしらべて収納しよう
とっていきたい の はこれ
'pos1': '連体化', 'surface': 'の', 'pos': '助詞', 'base': 'の'
#http://www.python-izm.com/contents/application/index_and_value.shtml
"""

import ans30c
imput = ans30c.f30("../data/neko.txt.mecab")

"""
3つの要素をつかってlistをまわす方法がわかんないな
[[1,2,3],[2,3,4],[3,4,5],...] ってのをつくってそれでまわそっか
"""
checker_all = []
for i in range(len(imput)-2 ):
    checker = [i, i+1, i+2]
    checker_all.append(checker)

rslt = []
for ii in range(len(imput)-2):
    if imput[checker_all[ii][0]]["pos"]=="名詞" and imput[checker_all[ii][1]]["pos"] == "助詞" and imput[checker_all[ii][1]]["base"] == "の" and imput[checker_all[ii][2]]["pos"]=="名詞":
        rslt.append (imput[checker_all[ii][0]]["surface"] +imput[checker_all[ii][1]]["surface"] +imput[checker_all[ii][2]]["surface"])

print(rslt)
