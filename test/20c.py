import gzip
import json


with gzip.open("./data/jawiki-country.json.gz", 'rt',encoding="utf8") as wiki:
    for line in wiki:
        json_data=json.loads(line)
        if json_data["title"] == "イギリス":
            print (json_data)

