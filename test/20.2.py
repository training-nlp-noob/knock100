#coding:utf-8
import gzip
import json

with gzip.open("jawiki-country.json.gz", 'rb') as data1:
    with open(data1, "r",encoding="utf-8") as data2:
        jsonData = json.load(data2)
        print(jason.dumps(jasonData, intdent = 4))

# http://peaceandhilightandpython.hatenablog.com/entry/2013/12/06/082106
