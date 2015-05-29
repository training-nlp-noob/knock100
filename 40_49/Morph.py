#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），
#品詞細分類1（pos1）をメンバ変数に持つこととする

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
        
    
