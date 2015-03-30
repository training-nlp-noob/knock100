# -*- coding: utf-8 -*- 

#00. 文字列の逆順
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

'stressed' [::-1]



#01. 「パタトクカシーー」
#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ


hoge=u"パタトクカシーー"
print(u"元の状態")
print(hoge)
print(u"解答")
print(hoge[0]+hoge[2]+hoge[4]+hoge[6])


#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str1 = u"パトカー"
str2 = u"タクシー"
print(u"str1 <-" + str1)
print(u"str2 <-" + str2)
str3 = str1[0]+str2[0]+str1[1]+str2[1]+\
 str1[2]+str2[2]+str1[3]+str2[3]
print(u"解答 ;str1[0]+str2[0]+str1[1]+str2[1]+\
 str1[2]+str2[2]+str1[3]+str2[3]\n -> " + str3)

#うーん、力技だなぁ。ま、初めだしいいか。
#やっぱり、あまりにひどいので、forで処理

str1 = u"パトカー"
str2 = u"タクシー"
print(u"str1 <-" + str1)
print(u"str2 <-" + str2)
str3=u""
for (i) in range(0,4):
    str3 = str3 + str1[i]+str2[i]
print(u"結合表示 ;\n\
      for (i) in range(0,4):\n\
      str3 = str3 + str1[i]+str2[i]\n\
       -->> " + str3)   

#追記してみる


#03. 円周率

print(u"第3問 ")

hoge = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print(hoge)
hoge = hoge.replace(",","")
hoge = hoge.replace(".","")
words = hoge.split(" ")
print(hoge)
print(words)

list = []
for i in  range(len(words)) :
    list.append(len(words[i]))
print(list)

for i in  range(len(words)) :
     print(i,words[i], len(words[i]))


#4 
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


#05. n-gram

print("第5問")
 
text = "I am an NLPer"
print(text)
text =text.replace( " ","")
print(text)

def ngram (input , N ):
    """ make empty list then slice the imput
    if there exists space, you need del spaces before applying function
    """
    ret=[]
    for i in range(len(input)-N+1):
        ret.append(input[i:i+N])
    return ret


ans5_1 = ngram(text,2)
print(ans5_1)
ans5_2 = ngram (text,1)
print(ans5_2)







