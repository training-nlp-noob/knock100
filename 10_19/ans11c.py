#!/usr/bin/env python
# coding=utf-8

# http://www.yukun.info/blog/2008/06/python-file.html

import os
import re
print (os.getcwd())

os.chdir("../data")
print (os.getcwd())

f= open("hightemp.txt","r",encoding="utf-8")
with open("../rslt11.txt", "w") as r:
    line = f.readline()
    while line:
        str1 = re.sub("¥t"," aaa ",line)
        r.write(str1)
        line = f.readline()
f.close()
