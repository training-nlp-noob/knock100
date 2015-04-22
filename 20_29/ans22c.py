import gzip
import json

def f_20 () :
    with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
        for line in wiki:
            json_data=json.loads(line)
            if json_data["title"] == "イギリス":
                        return(json_data["text"])

honbun = f_20()
print(type(honbun))
#本文 は文字列

honbun_row = honbun.split("\n")
a_22_1 = []
for rows in honbun_row:
    if rows.find("Category") >= 0:
        a_22_1.append(rows)


print(len(a_22_1))
print(a_22_1)

#こっから文字列を綺麗にすればいいのかな。
