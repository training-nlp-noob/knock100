#coding:utf-8

'''
形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，
ここで作ったプログラムを活用せよ．

プログラムはmodule30y_k.py として保存している
listxというリストで表現

33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
'''

# module30y_k.py　にパスが通るか同じフォルダに置いてある場合のみ
import module30y_k
print("----------")
pre_sahen =[]
for item in module30y_k.listx:
    if item["pos1"]=="サ変接続" and item["pos"]=="名詞":
        pre_sahen.append(item["surface"])

#重複を削除？するのかなぁ
sahen = list(set(pre_sahen))

print(sahen)
