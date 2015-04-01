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
 
text = "Yes, I am an NLPer."
print(text)

def N_gram_Character (input, N):
    """
    文字列 character　N-gramとして、この関数では記号をいったん抜いて、
    空白はアンダーバーで明示
    """
    ret=[]
    input =input.replace("  "," ")
    input =input.replace(",","")
    input =input.replace(".","")
    input =input.replace("?","")
    input =input.replace(";","")
    input =input.replace(":","")
    input =input.replace(" ","_")
    for i in range(len(input)-N+1):
        ret.append(input[i:i+N])
    return ret

def N_gram_Word (input, N):
    """
    単語 character　N-gramとして、この関数では記号をいったん抜いて、
    単語間を同じくアンダーバーで明示
    """
    ret=[]
    input =input.replace("  "," ")
    input =input.replace(",","")
    input =input.replace(".","")
    input =input.replace("?","")
    input =input.replace(";","")
    input =input.replace(":","")
    word = input.split(" ")
    for i in range(len(word)-N+1):
        append_words = word[i]
        for j in range(N-1):
            append_words = append_words + '_' + word[i+j+1]
        ret.append(append_words)
    return ret




ans5_1 = N_gram_Word (text,2)
print("単語bi-gram -> N_gram_Word (text,2)")
print(ans5_1)

ans5_2 = N_gram_Character (text,2)
print("文字bi-gram -> N_gram_Character (text,2)")
print(ans5_2)

#せっかく、Ngramなので

ans5_3 = N_gram_Word (text,3)
print("単語tri-gram -> N_gram_Word (text,3)")
print(ans5_3)

ans5_4 = N_gram_Character (text,3)
print("文字tri-gram -> N_gram_Character (text,3)")
print(ans5_4)



'''
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

def N_gram_Character (input, N):
    ret=[]
    input =input.replace("  "," ")
    input =input.replace(",","")
    input =input.replace(".","")
    input =input.replace("?","")
    input =input.replace(";","")
    input =input.replace(":","")
    input =input.replace(" ","_")
    for i in range(len(input)-N+1):
        ret.append(input[i:i+N])
    return ret

X = N_gram_Character (u"paraparaparadise", 2)

Y = N_gram_Character (u"paragraph", 2)

print("X= ;")
print(X)
print("Y= ;")
print(Y)
print("\n")

print("XとYの和集合; set(X)|set(Y)")
print(set(X)|set(Y))
print("\n")
print("XとYの和集合2; set(X).union(set(Y))")
print(set(X).union(set(Y)))
print("\n")

print("XとYの積集合; set(X)&set(Y)")
print(set(X)&set(Y))
print("\n")
print("XとYの積集合2; set(X).intersection(set(Y))")
print(set(X).intersection(set(Y)))
print("\n")

print("XとYの差集合 XにあるがYにない; set(X)-set(Y)")
print(set(X)-set(Y))
print("\n")
print("XとYの差集合2 XにあるがYにない; set(X).difference(set(Y))")
print(set(X).difference(set(Y)))
print("\n")
print("XとYの差集合 YにあるがXにない; set(Y)-set(X)")
print(set(Y)-set(X))
print("\n")
print("XとYの差集合2 YにあるがXにない; set(Y).difference(set(X))")
print(set(Y).difference(set(X)))
print("\n")
print("XとYの差集合? XかYどちらかにある; set(X)^set(Y)")
print(set(X)^set(Y))
print("\n")
print("XとYの差集合2? XかYどちらかにあ; set(X).symmetric_difference(set(Y))")
print(set(X).symmetric_difference(set(Y)))
print("\n")

# 'se' を探せ 2種類

if X.index('se') > 0:
    print ('隊長、ありました')
else:
    print ('悪魔の証明は困ります')
print("\n")
if Y.count('se') > 0:
    print ('隊長、ありました')
else:
    print ('悪魔の証明は困ります')

#Q7
print('Q7')
def func07(X,Y,Z):
    print(X,'時の', Y, 'は' , Z , sep='')

x= 12
y= '気温'
z= 22.4

func07(x,y,z)



