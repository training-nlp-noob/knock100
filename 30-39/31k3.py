#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create neko.txt.mecab

#問題文では、どうもデフォルトのmecabrcで読み込む必要がありそうよ。品詞細分類1とかがいるから。


import MeCab #,sys

with open ("../data/neko.txt","r",encoding="utf-8") as neko, \
     open ("../data/neko.txt.c.mecab","w",encoding="utf-8") as out:
        f = neko.read()
        m = MeCab.Tagger() #デフォルト("mecabrc")、茶筅は("-Ochasen")
        out.write(m.parse(f))
        '''
        要素分けは次の問題
        node = m.parseToNode(f)
        while node:
            out.write(node.surface)
            out.write(",")
            out.write(node.feature)
            out.write("\n")
            node = node.next
        '''
