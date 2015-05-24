#coding:utf-8
import gzip
import json


        
with gzip.open("./data/hightemp.txt.gz","rt",encoding="utf-8") as f:
    ff = f.readlines()
ls = []
for i in range(len(ff)):
    col1 = ff[i].split("\t")[0]
    ls.append(col1)
print(sorted(set(ls)))
# http://peaceandhilightandpython.hatenablog.com/entry/2013/12/06/082106
