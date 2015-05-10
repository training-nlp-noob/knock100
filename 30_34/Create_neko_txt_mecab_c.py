#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create neko.txt.mecab

#問題文では、どうもデフォルトのmecabrcで読み込む必要がありそうよ。品詞細分類1とかがいるから。


import MeCab #,sys

with open ("../data/neko.txt","r",encoding="utf-8") as neko, \
     open ("../data/neko.txt.mecab","w",encoding="utf-8") as out: #モードをaからwに変更
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


# parse ではうまくいったけど、parseToNodeではうまくいかないな
# http://shogo82148.github.io/blog/2012/12/15/mecab-python/
#http://aidiary.hatenablog.com/entry/20101121/1290339360
