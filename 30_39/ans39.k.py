#!/usr/bin/env python3
#coding:utf-8

"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

import collections
import ans30c
import os
imput = ans30c.f30(os.path.abspath(os.path.dirname(__file__))+ "/../data/neko.txt.mecab")

#原型のリスト 品詞の区別はしなくていいかな
#http://docs.python.jp/3.3/library/collections.html

surface_all = []
for i in imput:
    surface_all.append(i["surface"])

count_words = collections.Counter(surface_all)
# Counterは 辞書のサブクラス 並べ替えも終了かな most_common() も入れたほうがいいか？

#お絵かき準備

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#フォントを設定。Windowsようなので、あしからず
fp = FontProperties(fname='C:\Windows\Fonts\meiryo.ttc')

v_x = []
v_y = []
juni = 0
for item in count_words.most_common(): #一応並べ替えてみる
    juni = juni + 1
    v_x.append(juni)
    v_y.append(item[1])

plt.scatter(v_x, v_y)
plt.xscale('log')
plt.yscale('log')
plt.xlim([0,100000])
plt.ylim([0,10000])
plt.title("出現単語", fontproperties=fp)
plt.xlabel("出現順（対数表示）", fontproperties=fp)
plt.ylabel("出現順回数（対数表示）", fontproperties=fp)
plt.show()
