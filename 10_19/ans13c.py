
#Q13 の部分
# 繰り返すので関数を定義してみる

def func13(x,y,z) :
    with  open(x,"r") as y:
        z=[]
        for lines in y:
            z.append(lines.split("\n")[0])
        return(z)


r1 = func13 ("col1.txt","c1" ,"cc1")
r2 = func13 ("col2.txt","c2" ,"cc2")

if len(r1) == len(r2):
    with open("col12.txt","w") as c12:
        for i in range(len(r1)):
            c12.write(r1[i])
            c12.write("\t")
            c12.write(r2[i])
            c12.write("\n")
