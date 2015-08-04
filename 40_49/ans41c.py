#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import re

# クラスの定義
class Morph:
    def __init__(self, line): #lineは入力の1行
        self.surface, morph_elems = line.split("\t")
        self.base = morph_elems.split(",")[6]
        self.pos = morph_elems.split(",")[0]
        self.pos1 = morph_elems.split(",")[1]

chunk_pattern = re.compile(r"(?P<INDEX>\d+)\s(?P<DST>((-1)|\d+))D[^\n]+\n(?P<MORPHS>.+)",re.S)
#うまいなー 複数行をまとめてchunk_patternとして処理しようって戦略なのね

##Q49のためにindexを保持

class Chunk:
    def __init__(self, chunk):
        #indexの保持
        self.index = chunk_pattern.match(chunk).group("INDEX")
        self.index = int(self.index)
        # dstの代入
        self.dst, morphs = chunk_pattern.match(chunk).group("DST","MORPHS")
        self.dst = int(self.dst)
        # Morphのリスト生成
        morphs = morphs.split("\n")
        self.morphs = [Morph(morph) for morph in morphs if morph != ""]
        # srcsの初期化
        self.srcs = []

#処理を書こう
"""
1文に相当するinputを受け取って Chunkオブジェクトのリストとして表現
1文はこんな感じ
* 0 2D 0/1 -1.911675
名前	名詞,一般,*,*,*,*,名前,ナマエ,ナマエ
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
* 1 2D 0/0 -1.911675
まだ	副詞,助詞類接続,*,*,*,*,まだ,マダ,マダ
* 2 -1D 0/0 0.000000
無い	形容詞,自立,*,*,形容詞・アウオ段,基本形,無い,ナイ,ナイ
。	記号,句点,*,*,*,*,。,。,。
EOS

srcs も評価する
"""
def create_sentence_from_input(input) :
    pre_chunks = input.split("* ")   #リスト
    chunks = [Chunk(i) for i in pre_chunks if i != ""]
    # Chunk.srcsの計算
    # すべてのchunksについて dstが負でなければ
    #自分のINDEXを indexga がdst の 文節の srcsに追加する
    chunks_length = len(chunks)

    for i,chunk in enumerate(chunks):
        dst = chunk.dst
        if dst >= 0 and dst < chunks_length:
            chunks[dst].srcs.append(i)
    return chunks


"""
構造のイメージ
essey 以下の senntence をリストでまとめる
sentence chunk のあつまり
"""

def f_41() :
    essey = []
    with open("./data/neko.txt.f1.cabocha", "r") as f:
        buffer = ""
        for line in f:
            if line.strip() == 'EOS':
                if len(buffer) > 1:
                    essey.append(create_sentence_from_input(buffer))
                buffer = ''
            else:
                buffer += line
    return(essey)

# f_41 は 全体を 文のりすと
# 文は Chunkオブジェクトのリストで返してくる


if __name__ == '__main__':
    for chunk in f_41()[8]:
        surface_list = [morph.surface for morph in chunk.morphs]
        print(str(chunk.dst)+" "+str("".join(surface_list)))
