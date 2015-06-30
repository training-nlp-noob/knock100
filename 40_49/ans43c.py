#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
43
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
"""

# クラスChunkもimport しないとダメなのかしら？？

from ans41c import f_41
input = f_41()
for sentence in input :
    for chunks in sentence :
        moto_pos_list = [m.pos for m in chunks.morphs]
        if "名詞" in moto_pos_list and chunks.dst != -1:
            saki_chunk = sentence[chunks.dst]
            saki_pos_list = [s.pos for s in saki_chunk.morphs]
            if "動詞" in saki_pos_list:
                print(  \
                "".join([m.surface for m in chunks.morphs if m.pos != "記号"]) +  \
                "\t"  + \
                "".join([s.surface for s in saki_chunk.morphs if s.pos != "記号"]) )

"""
                print(  \
                "".join([m.pos for m in chunks.morphs if m.pos != "記号"]) +  \
                "\t"  + \
                "".join([s.pos for s in saki_chunk.morphs if s.pos != "記号"]) )
                print (" ")
"""
