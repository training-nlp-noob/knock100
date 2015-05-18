# -*- coding: utf-8 -*-

"""
32. 動詞の原形
動詞の原形をすべて抽出せよ．
"""

import ans30c

imput = ans30c.f30("../data/neko.txt.mecab")
verb_base = []
for keitaiso in imput:
    if keitaiso["pos"] == "動詞":
        verb_base.append(keitaiso["base"])

print(verb_base)
