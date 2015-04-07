#!/usr/bin/env python
# coding=utf-8

# http://www.yukun.info/blog/2008/06/python-file.html

import re

f= open("./data/hightemp.txt","r",encoding="utf-8")
with open("./rslt11.txt", "w") as r:
    line = f.readline()
    while line:
        str1=re.sub("\t"," ",line)
        print(line) #確認
        print(str1) #確認
        r.write(str1)
        line = f.readline()
f.close()


## 置換が出来ないぞなんでだ raw文字列がなんかよくわかんないな
# http://likealunatic.jp/2008/01/10_unicode.php
# http://docs.python.jp/3.3/library/re.html

#ん？　ちゃんと動いているよ。
#そっちはいいかもしれないけど、エンコードを指定しないと、こちらは
#windowsデフォルトで保存されていたよ。

#やっぱり、単純な関数が用意されているので別海

# ディレクトリをルートじゃないところへ変更、これは環境に併せて
import os
# os.chdir("C:/data")
print (os.getcwd())

fk1 = open("./hightemp.txt", "r", encoding="UTF-8")
# fk1wに書きだす
fk1w = open("./fk1w.txt", "w")
# タブをスペース「1文字は（１）」に変換
# http://www.mwsoft.jp/programming/python/str.html#trim
fk1w.writelines(fk1.read().expandtabs(1))
fk1w.close()
fk1.close()

# どうやらこれはレガシーなようなので同じものをwithで


with open("./hightemp.txt", "r", encoding="UTF-8") as rfile:
    with open("./fk1w.txt", "w", encoding="UTF-8") as wfile:
        wfile.writelines(rfile.read().expandtabs(1))

#うーん、美しいwww    
    
