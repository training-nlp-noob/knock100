#coding:utf-8

import module30y_k
print("----------")
verb = []
# 品詞が動詞なら、表層形を表示
for item in module30y_k.listx:
    if item["pos"]=="動詞":
        verb.append(item["surface"])

num1 = len(verb)
#重複を削除
verb = list(set(verb))

num2 = len(verb)

print(str(num1)+"のリストから重複を削除して残り"+str(num2))

print("サンプルで、100個ほど表示")
print(verb[:99])

#一応確認用に表層形と原型を格納してみる
verb2 = []
for item in module30y_k.listx:
    if item["pos"]=="動詞":
        verb2.append([item["surface"],item["base"]] )
print("----------")
print("サンプルで、原型とセットで100個ほど表示")
for i in verb2[:99]:
    print(i)
