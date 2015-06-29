#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）を
タブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．
•項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
•述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
始める  で      ここで
見る    は を   吾輩は ものを
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


