#hightemp.txtは，日本の最高気温の記録を
#「都道府県」「地点」「℃」「日」の
#タブ区切り形式で格納したファイルである．

x <- read.table("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt",
 sep = "\t", header=F, fileEncoding="utf-8")
colnames(x) <- c("都道府県","地点","℃","日")
