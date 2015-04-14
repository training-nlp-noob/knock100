# -*- coding: utf-8 -*-

#16. ファイルをN分割する

## まちがえてた、これだとN行ごとに分割だった。

"""
思考の流れ
標準出力に出力? ファイルに出力しよう
繰り返しの回数をとっておかないとダメだよね
knock100でコマンド実行したら、./に出力されるようにしようかな
ファイルの行数を確認
行数を parm で割り算 して切り上げ個の出力用ファイルが必要
N行ずつファイルに書いて 書き込み終わったら次のファイルへ
Q10で行数数えたな
"""
import sys
import math
parm = sys.argv
x = int(parm[1])

f = open ("./data/hightemp.txt","r",encoding="utf-8")
fl = f.readlines()
for i in range(1,len(fl)+1):
    r = math.ceil ( i / x )
    with open ("rs16_%s"%r, "a") as out :
        out.write(fl[i-1])
