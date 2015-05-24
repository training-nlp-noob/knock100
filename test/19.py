#!/usr/bin/env python
# coding=utf-8

# http://qiita.com/hatchinee/items/a904c1f8d732a4686c9d

from collections import Counter

f = open ("./data/hightemp.txt","r",encoding="utf-8")
fl = f.readlines()
f.close()

words = []
for i in fl:
    words.append(i.split("\t")[0])

counter= Counter(words)
for word, cnt in counter.most_common():
    print (word, cnt)
