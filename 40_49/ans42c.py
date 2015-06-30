#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

from ans41c import f_41,Chunk, Morph

#戦略 1文のなかで行う処理を書いてそれを全体で繰り返そう

# sentence をうけとって 元先の1行をかく関数をつくる
def write_moto_saki_lines(sentence) :
    with open ("output.tsv", "a") as w:
        for chunk in sentence:
            moto_chunk = [morph.surface for morph in chunk.morphs if morph.pos != "記号"]
            saki_chunk = [morph.surface for morph in sentence[chunk.dst].morphs if morph.pos != "記号" and chunk.dst >= 0]
            j_moto_chunk = "".join(moto_chunk)
            j_saki_chunk = "".join(saki_chunk)
            gyo= j_moto_chunk + "\t" + j_saki_chunk + "\n"
            w.write(gyo)

"""
#一文ならOK
test = f_41()[8]
write_moto_saki_lines(test)
"""


if __name__ == '__main__':
    input = f_41()
    rep = len(f_41())
    for i in range(rep):
        sentence = input[i]
        write_moto_saki_lines(sentence)
