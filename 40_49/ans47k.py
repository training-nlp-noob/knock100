#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．
•「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
•述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
•述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
•述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
以下の出力が得られるはずである．
返事をする      と に は        及ばんさと 手紙に 主人は
'''

from ans41k import Chunk , ans41
import os
from datetime import datetime   #ファイル名に時刻を入れる
msentences = ans41()

wfilepath = os.path.abspath(os.path.dirname(__file__)+ "/../data/" + datetime.now().strftime('%Y%m%d%H%M%S') +".txt")

with open(wfilepath, mode = 'a', encoding = 'utf-8') as af:
    dousikaku = ""
    for sentence in msentences:
        for chunk in sentence:
            for morph in chunk.morphs:
                if morph.pos == "動詞":
                    josi = []
                    kakus = []
                    for srcs2 in chunk.srcs:
                        
                        for morph2 in sentence[srcs2].morphs:                            
                            if morph2.pos == "助詞":
                                josi.append(morph2.base)
                            else:
                                continue
                        for morph3 in sentence[srcs2].morphs:
                            kakustr = ''
                            if morph3.pos == "助詞":
                                for morph4 in sentence[srcs2].morphs:
                                    kakustr += morph4.surface
                                kakus.append(kakustr)
                                break
                            else:
                                continue
                    af.write(morph.base + "\t" + " ".join(josi) + "\t" + " ".join(kakus) + "\n")
                    break
                else:
                    continue


