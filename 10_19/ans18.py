# -*- coding: utf-8 -*-


# 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

import codecs
import sys

f = codecs.open("../data/hightemp.txt","r","utf-8")
# 一行の文字列が要素の配列を生成
raw = f.readlines()
f.close()

r_elem = []
for rws in raw :
    # split すると配列ができる。
    r_elem.append(rws.split("\t"))

# 気温のカラムを参照し、列毎、全体配列内の要素を入れ替える。(ソート)
i = 0
while i < len(r_elem) - 1 :
    j = len(r_elem) - 1
    while j > i :
        if float(r_elem[j][2]) <= float(r_elem[j-1][2]) :
            t = r_elem[j]
            r_elem[j] = r_elem[j-1]
            r_elem[j-1] = t
        j -= 1
    i += 1


r_str = []
for rws in r_elem :
    r_str.append(" ".join(rws))

f = codecs.open('text.txt','w',"utf-8") # 書き込みモードで開く
f.writelines(r_str) # シーケンスが引数。
f.close()

# unix コマンドはこちら(参考URL:http://codezine.jp/unixdic/w/sort)
# sort -k3,3 hightemp.txt
