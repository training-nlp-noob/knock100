#coding:utf-8

import module30y_k

# 品詞が動詞なら、表層形を表示
for item in module30y_k.listx:
    if item["pos"]=="動詞":
        print(item["surface"])
