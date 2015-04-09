#!/usr/bin/env python
# coding=utf-8


#http://www.yukun.info/blog/2008/07/python-command-line-arguments.html


import sys # モジュール属性 argv を取得するため

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数
# デバッグプリント
print argvs
print argc
