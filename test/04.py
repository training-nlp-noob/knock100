print("Q4")

hoge = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words= hoge.split( " ")

dic = {}
for i in range(len(words)):
    if i in (0, 4, 5, 6, 7, 8, 14, 15, 18):
        print(words[i],words[i][0:1])
        dic[words[i][0:1]] = i+1
    else:
        print (words[i], words[i][0:2])
        dic[words[i][0:2]] = i+1
print(dic)
