# -*- coding: utf-8 -*-

'''
45. 動詞の格パターンの抽出
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

    動詞を含む文節において，最左の動詞の基本形を述語とする
    述語に係る助詞を格とする
    述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

    コーパス中で頻出する述語と格パターンの組み合わせ
    「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''

import re
import collections

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
    # 出力ファイルcorpus.txtの設定
    corpus = open('corpus.txt', 'w', encoding="utf8")
    
    # コーパスの作成、書き込み
    for sentence in sentence_list:
        for chunk in sentence.chunks:
            for morph in chunk.morphs:
                if morph.pos == "動詞": #形態素の品詞が動詞の場合
                    particle_list = [] #助詞の格納リスト
                    for src in chunk.srcs:
                        for src_morph in sentence.chunks[src].morphs: #係り元の文節の形態素でループ
                            if src_morph.pos == "助詞": #係り元の文節内形態素の品詞が助詞の場合
                                particle_list.append(src_morph.base) #助詞の格納リストに基本形を格納
                    corpus.write(morph.base+"\t"+" ".join(particle_list)+"\n") #動詞の基本形(tab)(スペース区切りの助詞格納リスト内の助詞の基本形たち) を書き込み
                                                                           #助詞がなくても、動詞の基本形(tab)という書き込みは行う
                    break #文節内最左の動詞のみ参照のため
    
    corpus.close()
    
    # コーパスリストの作成
    corpus_list = [] #[(動詞,助詞),(動詞,助詞),…]
    with open("corpus.txt", encoding="utf8") as corpus:
        for line in corpus:
            line = line.rstrip() #行末の改行やスペース等を削除
            if line.find("\t") > -1: #助詞がひとつ以上存在するものに限る
                verb, particles = line.split("\t") #verb:動詞
                particles = particles.split(" ")   #particles:助詞のリスト
                corpus_list.extend([(verb,particle) for particle in particles]) #コーパスリストへの格納
    
    # コーパスリストを頻出順にする
    corpus_counts = collections.Counter(corpus_list).most_common()
    
    # コーパス中で頻出する述語と格パターンの組み合わせ(10個)を表示
    print([corpus_count[0] for corpus_count in corpus_counts[:10]])

    #「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順）を表示
    print("する："+",".join([corpus_count[0][1] for corpus_count in corpus_counts if corpus_count[0][0]=="する"])+"\n")
    print("見る："+",".join([corpus_count[0][1] for corpus_count in corpus_counts if corpus_count[0][0]=="見る"])+"\n")
    print("与える："+",".join([corpus_count[0][1] for corpus_count in corpus_counts if corpus_count[0][0]=="与える"])+"\n")
