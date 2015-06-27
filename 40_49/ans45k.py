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
    dousikaku = ""
    for sentence in msentences:
        for chunk in sentence:
            for morph in chunk.morphs:
                if morph.pos == "動詞":
                    dousikaku += morph.base
                    for srcs2 in chunk.srcs:
                        for morph2 in sentence[srcs2].morphs:
                            if morph2.pos == "助詞":
                                dousikaku += " " + morph2.base
                            else:
                                continue
                    af.write(dousikaku + "\n")
                    dousikaku = ""
                    break
                else:
                    continue


