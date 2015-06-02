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

#とりあえず文を読み込むのを使う
import module30y_k as myk
print("----------")

#単語に修正　変数はmeisiのままだけど・・・

meisi = []
for item in myk.listx:
    meisi.append(item["surface"])

#エクセルのcountifみたいな感じにする

#重複を削除したリストを作成
smeisi = list(set(meisi))

#重複を削除したリスト一つ一つでカウントする
clist = []
for item2 in smeisi:
    clist.append([item2, meisi.count(item2)])

#ならべかえ 2個目の「数字」で、逆順に並べ替え
clist.sort(key=lambda x:(x[1]), reverse=True)

for ten in clist[:10]: #clist[0:10]の省略
    print(ten)

#さて、グラフを描きます
# http://yubais.net/doc/matplotlib/bar.html
#棒グラフの描写は plt.bar() で行います。 引数には2つのリストが必要です。
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#フォントを設定。Windowsようなので、あしからず
fp = FontProperties(fname='C:\Windows\Fonts\meiryo.ttc')

'''
zipを使って書き換え
X = list(range(1, 11)) #1から10まで
Xlab = []
Y = []

for item3 in clist[0:10]:
    Xlab.append(item3[0])
    Y.append(item3[1])
'''
Xlab, Y = zip(*clist[0:10])

plt.bar(X,Y, align="center")  # 中央寄せ
plt.xticks(X, Xlab, fontproperties=fp)
plt.show()

