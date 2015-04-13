#!/usr/bin/env python
# coding=utf-8

#15

import sys
arg = sys.argv
xx = int(arg[1])
f = open ("./data/hightemp.txt","r",encoding="utf-8")
ff = f.readlines()

for i in range(0, len(ff)):
    if i >= len(ff)-xx :
        print(ff[i], end="")
