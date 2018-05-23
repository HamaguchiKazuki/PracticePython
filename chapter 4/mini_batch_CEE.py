#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: hamaguchikazuki
"""
import numpy as np

#one-hot表現での交差エントロピー誤差
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
        
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y)) / batch_size

#普通のラベルでデータが渡されたとき
#def cross_entropy_error(y, t):
#    if y.ndim == 1:
#        t = t.reshape(1, t.size)
#        y = y.reshape(1, y.size)
#        
#    batch_size = y.shape[0]
#    return -np.sum(np.log(y[np.arange(batch_size), t])) / batch_size

                   