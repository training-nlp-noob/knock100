import gzip
import json

"""
with gzip.open("./data/jawiki-country.json.gz",'rt',encoding="utf-8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        print(json.dumps(json_data,sort_keys = True, indent = 4, ensure_ascii=False))
"""

# http://peaceandhilightandpython.hatenablog.com/entry/2013/12/06/082106
# json.dump すると文字化けする
# http://d.hatena.ne.jp/tatz_tsuchiya/20120227/1330325015 既知の問題
# 読み込むところまでは出来た

with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        if json_data["title"] == "イギリス":
            print (json_data["title"])



with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        if json_data["title"] == "イギリス":
            print(json_data)
        else:
            print("aaa")

###json.dump すると イギリス以外もでちゃうな dumpしなければ解決っぽい
