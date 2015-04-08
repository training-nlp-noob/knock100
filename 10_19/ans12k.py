import os
#自分のディレクトリに
#os.chdir("C:/data")

with open("./hightemp.txt", "r", encoding="UTF-8") as rfile:
    line = rfile.readlines()
    for i in range(0,2):
        fname = u"./col" + str(i+1) + u".txt"
        with open(fname, "w", encoding="UTF-8") as wfile:
            wfile.writelines(line[i])
