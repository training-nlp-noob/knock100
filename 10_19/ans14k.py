# -*- coding: utf-8 -*-

#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

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
        print("全部で" + str(linen) + "行。" + str(parm[1]) + "行まで表示")
        if x <= linen:
            lines = f2.readlines()
            for y in range(0,x): #最初は含む 最後は含まない・・・わかりにくい
                #http://atkonn.blogspot.jp/2008/02/python-python21-range.html
                print(lines[y].replace('\n', ''))
        else:
            print(str(linen) + "までの自然数を入れてください")
except ValueError:
    print ("自然数を入力してください")


#Windows ではコマンドラインで　python ans14k.py 3 で実行します

#　UNIXでは、　head -n N hightemp.txt で確認できます。はい。
