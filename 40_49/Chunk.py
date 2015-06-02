#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#40. 係り受け解析結果の読み込み（形態素）
#形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），
#品詞細分類1（pos1）をメンバ変数に持つこととする．
#さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
#各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
#41. 係り受け解析結果の読み込み（文節・係り受け）
#40に加えて，文節を表すクラスChunkを実装せよ．
#このクラスは形態素（Morphオブジェクト）のリスト（morphs），
#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を
#メンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，
#１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．



#Morphを実装するMorph.pyが同じディレクトリにあることが前提

from Morph import Morph     #ほぉほぉ、単にインポートするとMorphはmoduleになってしまう。
                            #Classをインポートするとき、こうするみたい？
import os

# /data/neko.txt.f1.cabocha を読み込む
#　このスクリプト自体は/data/40_49/にあることが前提

filepath = os.path.abspath(os.path.dirname(__file__)+ "/../data/neko.txt.f1.cabocha")
