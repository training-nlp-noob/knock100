#!/usr/bin/env python 
# coding=utf-8 

#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

with open("./data/hightemp.txt","r",encoding="utf-8") as f:
    ff = f.readlines()
#ffに格納したらopenを終了できるwww closeの代わりにwith 終了、インデント解除
ls = []
for i in range(len(ff)):
    col1 = ff[i].split("\t")[0]
    ls.append(col1)
print(set(ls))

#ついでに、違う並びかたも
lsu = sorted(set(ls), key=ls.index)
#重複削除 set　に、出現順を追加 sorted
#http://d.hatena.ne.jp/t-fridge/20080323/1206217930
print(lsu)
print('1列目、一意の一覧（出現順）・個数；'+str(len(lsu))+'個')


#UNIXだと
# cut -d $'\t' -f 1 hightemp.txt | sort | uniq

#以上（笑）　uniq　が sort　と一緒でなくては使えない
