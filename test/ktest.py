#coding:utf-8
import json,gzip

f = gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") 

jsonData = json.load(f)

#print (json.dumps(jsonData, sort_keys = True, indent = 4))

f.close()
