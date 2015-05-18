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

rslt = []
for ii in range(len(imput)-2):
    if imput[ii]["pos"]=="名詞" and imput[ii+1]["pos"] == "助詞" and imput[ii+1]["base"] == "の" and imput[ii+2]["pos"]=="名詞":
        rslt.append (imput[ii]["surface"] +imput[ii+1]["surface"] +imput[ii+2]["surface"])

print(rslt)
