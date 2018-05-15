#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 10:21:40 2018

@author: hamaguchikazuki
"""

import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

#最初の呼び出しには数分かかる
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

#それぞれのデータの形状を出力
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)
