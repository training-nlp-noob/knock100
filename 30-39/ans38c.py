#!/usr/bin/env python3
#coding:utf-8


# mac だと pip3 install matplotlib と打つだけでインストール出来ました
# http://kiito.hatenablog.com/entry/2013/12/05/123522

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

import matplotlib.pyplot as plt
import collections
import ans30c
imput = ans30c.f30("../data/neko.txt.mecab")

#原型のリスト 品詞の区別はしなくていいかな
#http://docs.python.jp/3.3/library/collections.html

base_all = []
for i in imput:
    base_all.append(i["base"])

count_words = collections.Counter(base_all)
# Counterは 辞書のサブクラス

hindo = []
for key, value in count_words.most_common():
    hindo.append(value)

#頻度にCounterする
hindo_count= collections.Counter(hindo)

"""
hindo_count のkey 出現頻度 x軸
hindo_count のvalue その値をとる単語の数 y軸
"""

#お絵かき準備
freq_x = []
numwords_y = []
for key,value in hindo_count.most_common():
    freq_x.append(key)
    numwords_y.append(value)

plt.bar(freq_x,numwords_y)
plt.xlim([0,500])
plt.ylim([0,1000])
plt.show()

#軸の範囲を制限してみる
#あってんのかな？

