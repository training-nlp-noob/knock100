#coding:utf-8

#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
#問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

#with gzip.open("./data/jawiki-country.json.gz", 'r') as wiki:
#    for line in wiki :
#        print(wiki.readlines())
### json.dumps
## json.loads とか使うんだろうけど

with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf-8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        print(json.dumps(json_data,sort_keys = True, indent = 4, ensure_ascii=False))


# http://peaceandhilightandpython.hatenablog.com/entry/2013/12/06/082106
# json.dump すると文字化けする
# http://d.hatena.ne.jp/tatz_tsuchiya/20120227/1330325015 既知の問題
# 読み込むところまでは出来た

with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf-8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        if json_data["title"] == "イギリス":
            print(json.dumps(json_data,sort_keys = True, indent = 4, ensure_ascii=False))
        else:
            print("aaa")
