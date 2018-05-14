#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:10:50 2018

@author: hamaguchikazuki
"""

import numpy as np
import matplotlib.pyplot as plt

#データの作成
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#グラフの描画
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle = "--", label="cos") #破線で描画
plt.xlabel("x")                                #x軸ラベル
plt.ylabel("y")                                #y軸ラベル
plt.title('sin & cos')                         #タイトル
plt.legend()
plt.show()