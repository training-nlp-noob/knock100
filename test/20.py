import gzip
with gzip.open("jawiki-country.json.gz", 'rt',encoding="utf-8") as wiki:
    wiki_content = wiki.readline()
while wiki_content:
    print(wiki_content)
    wiki_content = wiki.readline()

