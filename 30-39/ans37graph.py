#!/usr/bin/env python
# *-# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties
#fp = FontProperties(fname='C:\Windows\Fonts\meiryo.ttc')

X= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Xlab = ['の', '事', 'もの', '君', '主人', 'ん', 'よう', '人', '一', '何']
Y = [1611, 1207, 981, 973, 932, 704, 697, 602, 554, 539]

plt.bar(X,Y, align="center")  # 中央寄せ
plt.xticks(X, Xlab, fontproperties=FontProperties(fname='C:\Windows\Fonts\meiryo.ttc'))  #文字がぁ、文字があ・・・・
plt.show()
