#!/bin/sh

sed -e s/$'\t'/' '/g ./data/hightemp.txt > rslt11e.txt
diff rslt11.txt rslt11e.txt

# 多分できたけど sed のかきかたもよくわからない
# sed -e 's/\t/ /g' ./data/hightemp.txt > rslt11e.txt
# ではできなかった
# http://takuya-1st.hatenablog.jp/entry/2014/08/04/152101
# http://hydrocul.github.io/wiki/commands/sed.html
