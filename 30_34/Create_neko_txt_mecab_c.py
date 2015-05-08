#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create neko.txt.mecab


import sys,MeCab

with open ("./data/neko.txt","r",encoding="utf-8") as neko:
    with open ("./data/neko.txt.c.mecab","a") as out:
        f = neko.read()
        m = MeCab.Tagger ("-Ochasen")
        node = m.parseToNode(f)
        while node:
            out.write(node.surface)
            out.write(",")
            out.write(node.feature)
            out.write("\n")
            node = node.next


# parse ではうまくいったけど、parseToNodeではうまくいかないな
# http://shogo82148.github.io/blog/2012/12/15/mecab-python/
#http://aidiary.hatenablog.com/entry/20101121/1290339360
