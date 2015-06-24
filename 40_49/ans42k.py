#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''

from ans41k import Chunk , ans41
import os
from datetime import datetime   #ファイル名に時刻を入れる
#from ans40k_with_Morph import Morph
msentences = ans41()

wfilepath = os.path.abspath(os.path.dirname(__file__)+ "/../data/" + datetime.now().strftime('%Y%m%d%H%M%S') +".txt")

with open(wfilepath, mode = 'a', encoding = 'utf-8') as af:
    c_chunk = ""
    for sentence in msentences:
        for chunk in sentence:
            if int(chunk.dst) > -1:
                for morph in chunk.morphs:
                    if morph.pos == "記号":
                        continue
                    else:
                        c_chunk += morph.surface
                c_chunk += "\t"
                for morph2 in sentence[int(chunk.dst)].morphs:
                    if morph2.pos == "記号":
                        continue
                    else:
                        c_chunk += morph2.surface
                c_chunk += "\n"
                af.write(c_chunk)
                c_chunk = ""

