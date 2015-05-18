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

35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
'''

#とりあえず文を読み込むのを使う
import module30y_k
print("----------")

listy = module30y_k.listx
#名前が長いから付け替えるつもりで書いてみたけど、これだとメモリを2倍使うのかな？

#さて、まずは、名詞だけを引っ張ってこよう。ただし、連続しているものは連続していると明示しよう
meisi_list = [] #これに名詞を入れる。ただし連続しているものはリストとして保存！

tmp_lst = [] #こちらに名詞の「塊」を入れていこう。塊が「連続」！

for item in listy:
    if item["pos"] == "名詞":
        tmp_lst.append(item["surface"]) #名詞である限りtmpにため込む
    else: #名詞でなかったら、meisi_listにtmp_lstを吐き出す
        if len(tmp_lst) > 0: #空は除く
            meisi_list.append(tmp_lst)
            tmp_lst = []
            
#少しだけプリントして、確認
print("20個くらいmeisi_listを表示")
for i in meisi_list[0:20]:
    print(i)

#さて、仕上げは、複数続いている名詞だけなので、それを格納
#格納の仕方は、どうなんだろう、あまり本質的ではないので、
#名詞を続けて表示して、続けた数を振るくらいにしてみた

ans35k = []
for item2 in meisi_list:
    if len(item2) > 1:
        renzoku = "" #いったん空の文字列を定義
        for word in item2:
            renzoku = renzoku + word
        renzoku = renzoku + "(" + str(len(item2)) + ")"
        ans35k.append(renzoku)

print("答えを20個くらい確認")
for j in ans35k[0:20]:
    print(j)

   
