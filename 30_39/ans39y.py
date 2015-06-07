# -*- coding: utf-8 -*-

'''
39. Zipfの法則
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
'''

import MeCab,re
import collections
import matplotlib.pyplot as plt
'''
# neko.txt.mecabの作成
f = open("./data/neko.txt", encoding="utf8")
text = f.read()
f.close()
f = open('./data/neko.txt.mecab', 'w', encoding="utf8")
tagger = MeCab.Tagger()
result = tagger.parse(text)
f.write(result)
f.close()
'''


# neko.txt.mecabの読み込み
f = open("./data/neko.txt.mecab", encoding="utf8")
text = f.readlines() # 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音（読み、発音はないものも存在）
f.close()

# 初期化
pattern = re.compile(r"(?P<SURFACE_GROUPNO>.+)\t(?P<POS_GROUPNO>[^,]+),(?P<POS1_GROUPNO>[^,]+),(?P<POS2_GROUPNO>[^,]+),(?P<POS3_GROUPNO>[^,]+),(?P<CONJFORM_GROUPNO>[^,]+),(?P<CONJTYPE_GROUPNO>[^,]+),(?P<BASE_GROUPNO>[^,]+),?(.*)")
dic_list = []
dic = {}

# dic_list[dic[0],dic[1],dic[2],...]形式で形態素を収納
for i,line in enumerate(text):
    if line == "EOS\n":
        continue
    dic[i] = {}
    surface,pos,pos1,base = pattern.match(line).group("SURFACE_GROUPNO","POS_GROUPNO","POS1_GROUPNO","BASE_GROUPNO")
    dic[i]["surface"] = surface
    dic[i]["pos"] = pos
    dic[i]["pos1"] = pos1
    dic[i]["base"] = base
    dic_list.append(dic[i])
    
# MAIN
# 表層系一覧の作成
word_list = [item["surface"] for item in dic_list]
# 出現頻度順の単語とその出現回数の抽出 
count = [item[1] for item in collections.Counter(word_list).most_common()]
# matplotlibを使った棒グラフ作成
X = range(1,len(count)+1)
plt.loglog(X,count)
plt.show()
