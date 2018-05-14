#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:36:36 2018

@author: hamaguchikazuki
"""
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #yの範囲を指定
plt.show()

