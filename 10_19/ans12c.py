#!/usr/bin/env python
# coding=utf-8

# Q13
# col1.txt と col2.txtの作成 Q12部分
f= open("./data/hightemp.txt","r",encoding="utf-8")
with open("col1.txt","w") as c1:
    with open ("col2.txt","w") as c2:
        for lines in f:
            cols = lines.split("\t")
            c1.write(cols[0])
            c1.write("\n")
            c2.write(cols[1])
            c2.write("\n")
f.close()

#同じですけど、with　を使っているのと、withで複数をできる、という例
#あと、エンコードも指定しました
with open("./data/hightemp.txt","r",encoding="utf-8") as f:
    with open("col1.txt","w",encoding="utf-8") as c1, \
         open ("col2.txt","w" ,encoding="utf-8") as c2:
        for lines in f:
            cols = lines.split("\t")
            c1.write(cols[0] + u"\n")
            c2.write(cols[1] + u"\n")
