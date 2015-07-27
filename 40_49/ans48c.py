#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Q48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
"""

from ans41c import f_41
essay = f_41()

#essay = essay[5:6]
"""
構文木の根ってのは最後のことなのね。
"""

for sentence in essay :
    for chunks in sentence :
        if "名詞" in [s.pos for s in chunks.morphs]:
            path = ["".join([s.surface for s in chunks.morphs])]
            while chunks.dst != -1:
                chunks = sentence[chunks.dst]
                path.append("".join([m.surface for m in chunks.morphs]))
            print( "->".join(path))
