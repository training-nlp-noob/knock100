#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''

from ans41k import Chunk , ans41
import os

msentences = ans41()

for chunk in msentences[8]:
    surface_list = [morph.surface for morph in chunk.morphs]
    print(str(chunk.dst)+" "+str(surface_list))

#DOTで示すのに、全文じゃないようなきがするので、41で使った8番目だけ
#pydotがどうしても動かないので、普通にDOT言語をはいて、GVEditで動くことだけ確認

c_chunk = ""
sentence = msentences[8]
print("digraph DIRECTED {node[fontname=\"meiryo\"];")
for chunk in sentence:
    if int(chunk.dst) > -1:
        for morph in chunk.morphs:
            if morph.pos == "記号":
                continue
            else:
                c_chunk += morph.surface
        c_chunk += "->"
        for morph2 in sentence[int(chunk.dst)].morphs:
            if morph2.pos == "記号":
                continue
            else:
                c_chunk += morph2.surface
        c_chunk += ";"
        print(c_chunk)
        c_chunk = ""
print("}")
    
