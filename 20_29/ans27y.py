# -*- coding: utf-8 -*-

'''
27. 内部リンクの除去
Wikipediaの記事を以下のフォーマットで書き出したファイルjawiki-country.json.gzがある．
•1行に1記事の情報がJSON形式で格納される
•各行には記事名が"title"キーに，記事本文が"text"キーの辞書オブジェクトに格納され，そのオブジェクトがJSON形式で書き出される
•ファイル全体はgzipで圧縮される
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．

26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．


'''

import gzip,json,re

# jawiki-country.josn.gzからtitle=イギリスのtextをtextに収納
with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
       json_data=json.loads(line)
       #f.write(str(json_data["title"]))
       if json_data["title"] == "イギリス":
             text = json_data["text"]

# {{基礎情報 … }}を切り出し
# {{基礎情報 以降、最初に存在する行頭}}が終了の目安と想定している(基礎情報内の{{ }}は行をまたがないと想定している)
text = re.search(r"({{基礎情報[^\n]*)(\n.*)(\n}})",text,re.S).group(2)

# \n\|で分割
basic_informations = re.findall(r"\n\|(([^\n]|\n(?!\|))*)",text)

# 初期化
dic = {}
pattern = re.compile(r"(?P<KEY>[^=]+) = (?P<VALUE>.+)",re.S)
subpattern = re.compile(r"\[\[([^|]+?)(\|.*?)?\]\]")

# objのgroup(1)を返す
# subでマッチした部分の再利用のために使う
def func(obj):
    return obj.group(1)

for info in basic_informations:
    # key,valueをdicに追加
    key,value=pattern.match(info[0]).group("KEY","VALUE")
    
    # 改行、強調マークアップの除去
    value=value.replace("\n","").replace("'","")
    
    # 内部リンクの除去
    # 表示名・説明ではなく、実際の記事名・ファイル名を表記するようにしている
    value=subpattern.sub(func,value)
    dic[key]=value
