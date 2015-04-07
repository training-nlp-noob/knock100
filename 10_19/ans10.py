#いったんローカル保存したものを扱ってみる
import os
print (os.getcwd())

os.chdir("C:/data")
print (os.getcwd())

#よみこむ
f = open("hightemp.txt", "r", encoding="UTF-8")
print (len(f.readlines()))
f.close()


#次に、URLから直接取ってくるのをやってみる
#例によって、Verの２と３でかなりライブラリが違う

import urllib.request
f = urllib.request.urlopen("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt")
print (len(f.readlines()))
f.close()
