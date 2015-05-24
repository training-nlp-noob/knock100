#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# create neko.txt.cabocha
# このスクリプト自体は40_49においてある必要がある

import CaboCha, os

nekotxt = os.path.dirname(__file__) + "/../data/neko.txt"
nekocabocha = os.path.dirname(__file__)+ "/../data/neko.txt.cabocha"

with open (nekotxt,"r",encoding="utf-8") as neko, \
     open (nekocabocha,"w",encoding="utf-8") as out: 
        f = neko.read()
        c = CaboCha.Parser() 
#        out.write(c.parseToString(f))
        print(c.parseToString(f))
