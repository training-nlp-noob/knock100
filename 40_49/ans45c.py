#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Q45
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を

文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
"""

#srcs せっかくなので srcsでも使ってみようかな

from ans41c import f_41

essay = f_41()

# essay[5] が例文
#essay = essay[5:6]

forout = ""
for sentence in essay :
    for chunks in sentence :
        pos_list = [s.pos for s in chunks.morphs]
        if "動詞" in pos_list:
            zyutugo =[s.base for s in chunks.morphs if s.pos == "動詞"][0]
            kaku = []
            for src in chunks.srcs:
                moto = sentence[src]
                kaku.extend([m.base for m in moto.morphs if m.pos == "助詞"])
            #格は空リストのままのときもあるけどそのまま出力
            kaku.sort()
            print(zyutugo + "\t" +" ".join(kaku))
            forout += zyutugo + "\t" +" ".join(kaku) + "\n"


with open("ans45c_out.txt", "w") as w:
    w.write(forout)


"""
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

cat ans45c_out.txt | sort | uniq -c |sort -nr | head
grep -E "^する" ans45c_out.txt | sort |uniq -c | sort -nr
grep -E "^する|^見る|^与える" ans45c_out.txt | sort |uniq -c | sort -nr
"""
