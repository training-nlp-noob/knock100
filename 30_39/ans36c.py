#!/usr/bin/env python3
#coding:utf-8

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
http://www.lifewithpython.com/2014/05/python-count-elements-in-lists.html
http://docs.python.jp/2/library/collections.html
"""
# knock100/ のディレクトリで実行してね

import collections
import ans30c
imput = ans30c.f30("./data/neko.txt.mecab")

#原型のリスト 品詞の区別はしなくていいかな
base_all = []
for i in imput:
    base_all.append(i["base"])

count_words = collections.Counter(base_all)
print(count_words.most_common())

# print (count_words)
# most_commonしなくても並べ替えられている気がするな
