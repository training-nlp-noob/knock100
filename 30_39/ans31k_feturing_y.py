#coding:utf-8

import module30y_k
print("----------")
verb = set() #重複を省く集合として定義
# 品詞が動詞なら、表層形を表示
for item in module30y_k.listx:
    if item["pos"]=="動詞":
        verb.add(item["surface"]) #[]のappendが、setではadd

#重複を削除されているのでリストに変換
verb = list(verb)

print("サンプルで、100個ほど表示")
print(verb[:99])

#一応確認用に表層形と原型を格納してみる
verb2 = []
for item in module30y_k.listx:
    if item["pos"]=="動詞":
        verb2.append([item["surface"],item["base"]] )
print("----------")
print("サンプルで、原型とセットで50個ほど表示")
for i in verb2[:49]:
    print(i)

