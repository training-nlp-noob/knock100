#coding:utf-8
import MeCab
m = MeCab.Tagger() #デフォルト("mecabrc")、茶筅は("-Ochasen")

#読み込みファイルと書き込みファイルを指定
neko_open = open("../data/neko.txt", "r", encoding="utf-8")
mecab_write = open("../data/neko.txt.mecab", "w", encoding="utf-8")

#読み込みます
with neko_open as f1:
    neko_text = f1.read()

#書き込みます
with mecab_write as f2:
    f2.write(m.parse(neko_text))

