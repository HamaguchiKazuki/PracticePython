#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 17:18:20 2018

@author: hamaguchikazuki
"""
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) #yの範囲を指定
plt.show()


    
    