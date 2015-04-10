# -*- coding: utf-8 -*-
import sys

parm = sys.argv
#「sys.argv」に起動時のパラメータが格納されます。
#リストで値が返されますが、最初の値には実行ファイル名が入りますので注意しましょう。
#http://www.python-izm.com/contents/basis/command_line_arguments.shtml

print("渡されたパラメーターを一応確認表示です")
print(parm) 
#エラー処理を入れておきます
#http://symfoware.blog68.fc2.com/blog-entry-873.html

#なんと、先日考察した、readlinesがNULLになるのがここで生きます
#行数をとるのと読むのと、二つを回します
try:
    x = int(parm[1])
    f1 = open ("./data/hightemp.txt","r",encoding="utf-8")
    f2 = open ("./data/hightemp.txt","r",encoding="utf-8")
    with f1, f2:
        linen = len(f1.readlines())
        print("全部で" + str(linen) + "行。" + str(parm[1]) + "行前からから末まで表示")
        lines = f2.readlines()
        for y in range(0,x):
            print(lines[linen-x+y])
except ValueError:
    print ("整数を入力してください")


#Windows ではコマンドラインで　python ans14k.py 3 で実行します
