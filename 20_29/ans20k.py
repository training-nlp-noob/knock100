#coding:utf-8

#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
#問題21-29では，ここで抽出した記事本文に対して実行せよ．

import gzip
import json

with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf-8") as wiki:
  print('ここからわからん・・')

# json.dumps
# json.loads とか使うんだろうけど
