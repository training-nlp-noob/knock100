#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

'''
第4章: 形態素解析
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，
以下の問に対応するプログラムを実装せよ．
なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．

37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

'''

#とりあえず文を読み込むのを使う、こっちはもう本質的ではないとして
import module30y_k as myk
print("----------")



#リストの内包を使う
meisi = [item["surface"] for item in myk.listx if item["pos"] == "名詞"]

#で、カウントは36cを使う

import collections
count_words = collections.Counter(meisi)

d_count_words = count_words.most_common()

#一応確認
for ten in d_count_words[0:10]:
    print(ten)

#さて、グラフを描きます
# http://yubais.net/doc/matplotlib/bar.html
#棒グラフの描写は plt.bar() で行います。 引数には2つのリストが必要です。
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#フォントを設定。Windowsようなので、あしからず
fp = FontProperties(fname='C:\Windows\Fonts\meiryo.ttc')

X = list(range(1, 11)) #1から10まで
Xlab = []
Y = []

for item3 in d_count_words[0:10]:
    Xlab.append(item3[0])
    Y.append(item3[1])

plt.bar(X,Y, align="center")  # 中央寄せ
plt.xticks(X, Xlab, fontproperties=fp)
plt.show()
