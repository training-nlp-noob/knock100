#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），
#品詞細分類1（pos1）をメンバ変数に持つこととする

#文節を表すクラスChunkを実装せよ．
#このクラスは形態素（Morphオブジェクト）のリスト（morphs），
#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を
#メンバ変数に持つこととする．

#複数行のデータが来ないとどうにもならないので来ると期待する。
#ていうか、そういうリストを渡すのを前提・・・こんなんでいいいんだろうか

#* 文節番号 係り先の文節番号(係り先なし:-1) 主辞の形態素番号/機能語の形態素番号 係り関係のスコア
#形態素
#形態素

#これで一塊と期待したい・・・こんなんでいいんかなぁ。

from Morph import Morph

class Chunk:
    def __init__(self, lines):
        morphs = []
        for line in lines:
            if line[0:1] == "*":    #文節情報の列だったらそれを処理
                bnsetuinfo = line.split(" ")
                dst = bunsetsuinfo[2]
                srcs = bunsetsuinfo[
            else 
                morphs.append(Morph(line))   #Morphで処理

    
