#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を"->"で連結して表現する
文節iとjに含まれる名詞句はそれぞれ，XとYに置換する #???名詞句 ??名詞
また，係り受けパスの形状は，以下の2通りが考えられる．

case_a:文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
case_b:上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

#case_b
Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
#case_a
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
"""

"""
組み合わせを考えないといけないっぽい
http://docs.python.jp/3/library/itertools.html
http://momijiame.tumblr.com/post/68655902597/python-%E3%81%A7%E7%B5%84%E3%81%BF%E5%90%88%E3%82%8F%E3%81%9B%E3%82%84%E9%A0%86%E5%88%97%E3%82%92%E5%BE%97%E3%82%8B%E3%81%A8%E3%81%8D%E3%81%AF-itertools-%E3%82%92%E4%BD%BF%E3%81%86

リストの何番目かを保持するために class Chunkを編集した
"""

import itertools
from ans41c import f_41
essay = f_41()

#essay = essay[5:6]


def create_kakari_path(start_idx, input_sentence):
    kakari_path = [start_idx]
    chunk = input_sentence[start_idx]
    while chunk.dst != -1:
        chunk = input_sentence[chunk.dst]
        kakari_path.append(chunk.index)
    return(kakari_path)

def create_chunk_surface_all(input_sentence):
    chunk_surface_all = []
    for chunks in input_sentence:
         chunk_surface_all.append("".join([s.surface for s in chunks.morphs]))
    return(chunk_surface_all)

for sentence in essay:
    chunk_surface_all = create_chunk_surface_all(sentence)
    chunk_list = [c.index for c in sentence]
    for xx, yy in itertools.combinations(chunk_list,2):
            if "名詞" in [x.pos for x in sentence[xx].morphs] and \
            "名詞" in [y.pos for y in sentence[yy].morphs] :
                path_x = create_kakari_path(xx, sentence)
                path_y = create_kakari_path(yy, sentence)
                rep_x = ["X"]
                rep_x.extend([s.surface for s in sentence[xx].morphs if s.pos !="記号"][1:])
                surface_x = "".join(rep_x)
                rep_y = ["Y"]
                rep_y.extend([s.surface for s in sentence[yy].morphs if s.pos !="記号"][1:])
                surface_y = "".join(rep_y)

                #print(xx,surface_x,path_x,yy,surface_y,path_y) #確認
                #caes_a
                if set(path_x).issuperset(set(path_y)):
                    mid_idx_list = list(set(path_x)-set(path_y))[1:]
                    rslt =[surface_x]
                    for mid_idx in mid_idx_list:
                        rslt.append(chunk_surface_all[mid_idx])
                    rslt.append(surface_y)
                    print("->".join(rslt))
                #case_b
                else:
                    crossing = list(set(path_x) & set(path_y))
                    diff_x = list(set(path_x)-set(crossing))
                    diff_y = list(set(path_y)-set(crossing))
                    rslt_x =[surface_x]
                    rslt_y =[surface_y]
                    crossing_chunk = chunk_surface_all[crossing[0]]
                    ##crossingは必ず長さ1かな
                    if len(diff_x) >= 2:
                        for mid_x in diff_x[1:]:
                            rslt_x.append(chunk_surface_all[mid_x])
                    if len(diff_y) >= 2:
                        for mid_y in diff_y[1:]:
                            rslt_y.append(chunk_surface_all[mid_y])
                    forout = "->".join(rslt_x) + "|" + "->".join(rslt_y) + "|" + crossing_chunk
                    print(forout)


"""
なんかちょっと変なのがある気がするけどまあいいか
ignore_symbols とかで関数定義しとくべきだったかな
"""
