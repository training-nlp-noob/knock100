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
