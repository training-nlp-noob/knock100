#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Q46
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．

項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で      ここで
見る    は を   吾輩は ものを

文節を表すクラスChunk．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
"""


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
            #dicは 1述語にひとつ
            print(zyutugo, "\t", end="")
            dic = {}
            for src in chunks.srcs:
                moto = sentence[src]
                if "助詞" in [m.pos for m in moto.morphs]:
                    #key=項 value = 格
                    dic["".join([m.surface for m in moto.morphs])] = [m.base for m in moto.morphs if m.pos =="助詞"][-1]
            for k, v in sorted(dic.items(), key=lambda x:x[1]):
                print(v, " ", end="")
            for k, v in sorted(dic.items(), key=lambda x:x[1]):
                print(k, " ", end ="")
            print("\n", end="")


"""
http://blog.livedoor.jp/yawamen/archives/51492355.html
lambda ってなんだ？？
"""

#with open("ans45c_out.txt", "w") as w:
#    w.write(forout)


"""
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）

cat ans45c_out.txt | sort | uniq -c |sort -nr | head
grep -E "^する" ans45c_out.txt | sort |uniq -c | sort -nr
grep -E "^する|^見る|^与える" ans45c_out.txt | sort |uniq -c | sort -nr
"""

"""
#kakuの長さとkouの長さは同じはず
if len(kaku) - len(kou) != 0:
    print(len(kaku))
    print(len(kou))
"""
