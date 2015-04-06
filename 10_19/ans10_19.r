#hightemp.txtは，日本の最高気温の記録を
#「都道府県」「地点」「℃」「日」の
#タブ区切り形式で格納したファイルである．

x <- read.table("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt",
 sep = "\t", header=F, fileEncoding="utf-8")
colnames(x) <- c("都道府県","地点","℃","日")


#ふつーに、ファイルを読み込むだけというのもあるらしい
# 文字列の場合は引数に　what=""　か下記のを書くらしい
# http://d.hatena.ne.jp/yusap/20130515/1368564476
# http://munibus.hatenablog.com/entry/2013/10/19/044704
# http://cse.naro.affrc.go.jp/takezawa/r-tips/r/46.html
# 行単位でよみこみ
# でも、改行を無視はできないのだよなぁ
# blank.lines.skipをFとしたら、改行だけの行も読み込む
# 最後の行が本来は改行だけの行が必要らしい

v <- scan("http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt",
 what = character(), sep = "\n", blank.lines.skip = F,
 fileEncoding="utf-8")

