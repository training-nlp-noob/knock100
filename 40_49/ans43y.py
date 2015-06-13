# -*- coding: utf-8 -*-

'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

'''

import re

# Morph(形態素/品詞)の定義
class Morph:
    
    ###### 入力 ######
    # morph :表層形(tab)品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
    
    ### メンバ変数 ###
    #.surface :表層形
    #.base    :基本形
    #.pos     :品詞
    #.pos1    :品詞細分類1
    
    def __init__(self, morph):
        self.surface, featurea = morph.split("\t")
        featurea = featurea.split(",")
        self.base = featurea[6]
        self.pos = featurea[0]
        self.pos1 = featurea[1]

# Chunk(文節)の定義

chunk_pattern = re.compile(r"(?P<INDEX>\d+)\s(?P<DST>((-1)|\d+))D[^\n]+\n(?P<MORPHS>.+)",re.S)

class Chunk:
    
    ###### 入力 ######
    # chunk :インデックス番号 係り先番号D 主辞の形態素番号/機能語の形態素番号 係り関係のスコア(大きい方が係りやすい)(改行)
    #        表層形(tab)品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音(改行)
    #        表層形(tab)品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音(改行)
    #                                                 :
    
    ### メンバ変数 ###
    #.morphs :形態素(Morphオブジェクト)のリスト
    #.dst    :係り先文節インデックス番号
    #.srcs   :係り元文節インデックス番号のリスト
    #インデックス番号はSentence内の順番に一致しているため設定しない
    
    def __init__(self, chunk):
        # dstの代入
        self.dst, morphs = chunk_pattern.match(chunk).group("DST","MORPHS")
        self.dst = int(self.dst)
        
        # Morphのリスト生成
        morphs = morphs.split("\n")
        self.morphs = [Morph(morph) for morph in morphs if morph != ""]
        
        # srcsの初期化
        # Sentence classで計算
        self.srcs = []

# Sentence(文)の定義
class Sentence:
    
    ###### 入力 ######
    # line :EOSでsplitしたtext（上記Chunkの入力値chunkが１つ以上連なった形）
    
    ### メンバ変数 ###
    #.chunks :文節(Chunkオブジェクト)のリスト
    
    def __init__(self, line):        
        # Chunkのリスト生成
        sentence = line.split("* ")
        self.chunks = [Chunk(chunk) for chunk in sentence if chunk != ""]
        
        # Chunk.srcsの計算
        # chunkごとに係り先Chunkのsrcsに自分のインデックスを追加
        chunks_length = len(self.chunks)
        
        for i,chunk in enumerate(self.chunks):
            dst = chunk.dst
            if dst >= 0 and dst < chunks_length:
                self.chunks[dst].srcs.append(i)

if __name__ == '__main__':
    
    # neko.txt.f1.cabochaの読み込み
    text = open("./data/neko.txt.f1.cabocha", encoding="utf8").read().split("EOS\n")
    
    # sentence_listにSentenceのリストを生成
    sentence_list = []
    for line in text:
        if line.startswith("*"):
            sentence_list.append(Sentence(line))
            
    # MAIN
    for sentence in sentence_list:
        # 下記リストの作成
        chunk_pos_list_list = [] #文節内品詞リストを一文ごとにまとめたリスト : [ [品詞,品詞,品詞,…], [品詞,品詞,品詞,…], … ] 
        chunk_dst_list = []      #係り先番号リスト                           : [ 係り先番号, 係り先番号, … ]
        chunk_surface_list = []  #記号を除いた文節のリスト                   : [ 文節, 文節, … ]
        for chunk in sentence.chunks:
            chunk_pos_list_list.append([morph.pos for morph in chunk.morphs])
            chunk_dst_list.append(chunk.dst)
            chunk_surface_list.append("".join(morph.surface for morph in chunk.morphs if morph.pos!="記号"))
            
        for i,pos_list in enumerate(chunk_pos_list_list):
            if "名詞" in pos_list: #名詞がpos_listに含まれていた場合
                dst = chunk_dst_list[i]
                if "動詞" in chunk_pos_list_list[dst]: #係り先のpos_listに動詞が含まれている場合
                    print(chunk_surface_list[i]+"\t"+chunk_surface_list[dst]) #係り元文節(tab)係り先文節の表示
