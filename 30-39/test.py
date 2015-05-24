#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create neko.txt.mecab

#問題文では、どうもデフォルトのmecabrcで読み込む必要がありそうよ。品詞細分類1とかがいるから。


import MeCab #,sys

with open ("../data/neko.txt","r",encoding="utf-8") as neko, \
     open ("../data/neko.txt.mecab","w",encoding="utf-8") as out: #モードをaからwに変更
        f = neko.read()
        m = MeCab.Tagger() #デフォルト("mecabrc")、茶筅は("-Ochasen")
#        print(m.parse(f))
        out.write(m.parse(f))
