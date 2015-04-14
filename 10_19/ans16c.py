#!/usr/bin/env python
# coding=utf-8

#Q16 つくりなおし

import sys

x = int (sys.argv[1])

f = open ("./data/hightemp.txt","r",encoding="utf-8")
fl = f.readlines()

x1 = len(fl) // x #商
x2 = len(fl) % x #あまり
for i in range (0,x2):
    with open ("rs16_%s"%i, "a") as out :
        num=0
        while num < x1+1:
            out.write(fl[i*(x1+1)+num])
            num += 1
for i in range (x2,x):
    with open ("rs16_%s"%i, "a") as out :
        num=0
        while num < x1:
            out.write(fl[i*x1+x2+num])
            num += 1
