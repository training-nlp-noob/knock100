#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#形態素を表すクラスMorphを実装せよ．
#このクラスは表層形（surface），基本形（base），品詞（pos），
#品詞細分類1（pos1）をメンバ変数に持つこととする

#文節を表すクラスChunkを実装せよ．
#このクラスは形態素（Morphオブジェクト）のリスト（morphs），
#係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）を
#メンバ変数に持つこととする．

#さらに，入力テキストのCaboChaの解析結果を読み込み，
#１文をChunkオブジェクトのリストとして表現し，
#8文目の文節の文字列と係り先を表示せよ．

#複数行のデータが来ないとどうにもならないので来ると期待する。
#ていうか、そういうリストを渡すのを前提・・・こんなんでいいいんだろうか

#* 文節番号 係り先の文節番号(係り先なし:-1) 主辞の形態素番号/機能語の形態素番号 係り関係のスコア
#形態素
#形態素


from ans40k_with_Morph import Morph
import os

class Chunk:
    
    ###### 入力 ###### chunkをあつらえて渡すだけ
    # chunk :[morphs, 係り先文節インデックス番号（dst），
    #          係り元文節インデックス番号のリスト（srcs）] 

    def __init__(self, chunk):
        self.morphs, dst, srcs = chunk

def f_sentence(sentence):
    i=-1
    chunks = []
    for line in sentence:
        if line.startswith("* "):
            chunks.append([[],line.split(" ")[2][:-1],[]])
            #Morphを入れる器と、かかり元を入れる器を用意する
            i += 1
        else:
            chunks[i][0].append(Morph(line))
    #次にかかり元を地道に処理する、もう一周回す
    j=-1
    for line2 in sentence:
        if line.startswith("*"):
            j += 1
            saki = int(line.split(" ")[2][:-1])
            chunks[saki][2].append(j)
        else:
            continue
    #これで、ようやくChunkに渡せる。どっちで処理してもいいのだけど、こっちで処理
    c_sentence = []
    for chunk in chunks:
        c_sentence.append(Chunk(chunk))
    return c_sentence

# MAIN
if __name__ == '__main__':
    
    # /data/neko.txt.f1.cabocha を読み込む
    #　このスクリプト自体は/data/40_49/にあることが前提
    
    filepath = os.path.abspath(os.path.dirname(__file__)+ "/../data/neko.txt.f1.cabocha")
    sentences = []

    with open(filepath, encoding="utf8") as text:
    
        # sentenceに1文を入れて、それをsentencesに渡す
        sentence = []
        for line in text:
            line = line.strip() # 改行(\n)や空白を落とす
            if line == 'EOS':
                if len(sentence)>0:
                    sentences.append(f_sentence(sentence))
                else:
                    sentences.append([])
                sentence = []
            else:
                sentence.append(line)

    print(sentences[1])
    

