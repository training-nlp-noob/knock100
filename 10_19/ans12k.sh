#作業ディレクトリにファイルがあるとします
# 区切りタブは省略可（初期値）、1番目、2番目
cut -d $'\t' -f 1 hightemp.txt
cut -d $'\t' -f 2 hightemp.txt

#　ファイルに保存するときは
cut -d $'\t' -f 1 hightemp.txt >col1.txt
