#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

"""
http://qiita.com/nezuq/items/f481f07fc0576b38e81d
1行目
* 文節番号 係り先の文節番号(係り先なし:-1) 主辞の形態素番号/機能語の形態素番号 係り関係のスコア(大きい方が係りやすい)
2行目
表層形 （Tab区切り）品詞 品詞細分類1 品詞細分類2 品詞細分類3 活用形 活用型 原形 読み 発音
"""


# クラスの定義
class Morph:
    def __init__(self, line): #lineは入力の1行
        self.surface, morph_elems = line.split("\t")
        self.base = morph_elems[6]
        self.pos = morph_elems[0]
        self.pos1 = morph_elems[1]


#使ってみよう
def f_40 (input_file, line_no) : #ファイル名を入力する関数
    """
    all_lists が全体をしまうリスト
    bun_lists が文をしまうリスト。リストの要素は形態素。
    * 0 が文のはじめの 文節
    EOSは空白行の時に連続するので使わない文の評価に使わない予定
    """
    all_list = []
    bun_list = []
    with open(input_file, "r") as f:
        for line in f:
            if line[:3] =="EOS":    #改行マー
                continue
            elif line[:3] ==  "* 0":
                all_list.append(bun_list)
                bun_list = []
            elif line[:1] == "*":
                continue
            else :
                bun_list.append(Morph(line))
    return(all_list[line_no])
    #一文 がリストで帰ってくる 各形態素がリストの各要素


# 一番上に章番号がはいっているから それは除くよ
if __name__ == '__main__':
    rslt = f_40("./data/neko.txt.f1.cabocha",4)
    for i in rslt:
        print( i.surface, i.base, i.pos, i.pos1)
