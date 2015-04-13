#!/usr/bin/env python
# coding=utf-8

#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．


#http://www.yukun.info/blog/2008/07/python-command-line-arguments.html


import sys # モジュール属性 argv を取得するため

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
#「sys.argv」に起動時のパラメータが格納されます。
#リストで値が返されますが、最初の値には実行ファイル名が入りますので注意しましょう。
#http://www.python-izm.com/contents/basis/command_line_arguments.shtml


arg = sys.argv
xx = int(arg[1])
f = open ("./data/hightemp.txt","r",encoding="utf-8")
ff = f.readlines()

for i in range(0, len(ff)):
    if i >= len(ff)-xx :
        print(ff[i], end="")

f.close()


























# デバッグプリント
print("渡されたパラメーターを一応確認表示です")
print (argvs)
print("引数の個数")
argc = len(argvs) # 引数の個数
print (argc)

#エラー処理を入れておきます
#http://symfoware.blog68.fc2.com/blog-entry-873.html

#なんと、先日考察した、readlinesがNULLになるのがここで生きます
#行数をとるのと読むのと、二つを回します
try:
    x = int(argvs[1])
    f1 = open ("./data/hightemp.txt","r",encoding="utf-8")
    f2 = open ("./data/hightemp.txt","r",encoding="utf-8")
    with f1, f2:
        linen = len(f1.readlines())
        if x <= linen:
            lines = f2.readlines()
            for y in range(0,x):
                print(lines[linen-x+y].replace('\n', ''))
        else:
            print(str(linen) + "までの自然数を入れてください")
except ValueError:
    print ("整数を入力してください")


#Windows ではコマンドラインで　python ans15c.py 3 で実行します

#　UNIXでは、　tail -n N hightemp.txt で確認できます。はい。
