#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．


文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
"""

"""
pydotはなんかうまくいかない
かわりに pygraphviz をつかう
http://networkx.lanl.gov/pygraphviz/tutorial.html
http://april.fool.jp/blogs/2013/12/graphviz%E3%81%A7%E3%82%AB%E3%83%83%E3%82%AF%E3%81%84%E3%81%84%E3%82%B0%E3%83%A9%E3%83%95%E3%82%92%E6%8F%8F%E3%81%93%E3%81%86/#PyGraphviz-2
"""

from ans41c import f_41
import pygraphviz as pgv

sentence = f_41()[8]

G = pgv.AGraph(directed=True)
for chunks in sentence :
    saki_chunk = sentence[chunks.dst]
    moto = "".join([m.surface for m in chunks.morphs if m.pos != "記号"])
    saki = "".join([s.surface for s in saki_chunk.morphs if s.pos != "記号"])
    print( moto + "\t" + saki)
    G.add_edge(moto,saki)


G.layout()
G.draw('ans44c.png')
