#coding:utf-8

#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
#問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

with gzip.open("jawiki-country.json.gz", 'rt',encoding="utf-8") as wiki:
#    wiki_json = json.load(wiki, encoding="utf-8")
#   print(wiki_json)
#    print(json.dumps(wiki))
    f1 = wiki.readlines()
print(type(f1))
encode_json = json.dumps(f1)
print(type(encode_json))
decode_json = json.loads(encode_json)
print(type(decode_json))
