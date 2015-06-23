#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#40. 係り受け解析結果の読み込み（形態素）
#形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），
#品詞細分類1（pos1）をメンバ変数に持つこととする．
#さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
#各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

#MeCabの標準での形態素解析の結果は
#表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

class Morph:
    def __init__(self, item):
        item1 = item.split("\t")    #\tで表層形とそれ以降を分ける
        item2 = item1[1].split(",")    #後半部分を , で分ける。表層形とは分けたまま
        self.surface = item1[0]
        self.base = item2[6]
        self.pos = item2[0]
        self.pos1 = item2[1]

import os
def mainf():

    # /data/neko.txt.f1.cabocha を読み込む
    #　このスクリプト自体は/data/40_49/にあることが前提

    #filepath = os.path.abspath(os.path.dirname(__file__)+ "/../data/neko.txt.f1.cabocha")
    filepath = "C:/Users/owner/OneDrive/GitHub/knock100/data/neko.txt.f1.cabocha"

    neko_txt_cabocha = []   #リストに格納？なのかなぁ？
    temp_list = []  #EOSを文の区切りとする

    with open (filepath, encoding="utf8") as f:
        for line in f:
            if line.startswith("EOS"):
                neko_txt_cabocha.append(temp_list)
                temp_list = []
            elif line[:1] == "*":
                continue
            else:
                temp_list.append(Morph(line))

    #さて、3文目を表示、まずは素で表示
    print("print(neko_txt_cabocha[2])を実行")
    print(neko_txt_cabocha[2])

    #3文目の形態素列？とは何？とりあえずこんなのにしてみる
    for test in neko_txt_cabocha[2]:
        print([test.surface,test.base,test.pos,test.pos1])

if __name__ == '__main__':  # ここが最初に実行される
    mainf()  # main関数の呼び出し
