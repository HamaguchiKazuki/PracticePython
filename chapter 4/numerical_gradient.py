#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 19:55:52 2018

@author: hamaguchikazuki
"""

import numpy as np
import matplotlib.pylab as plt

def numerical_diff(f, x):
    h = 1e-4
    return ( f(x+h) - f(x-h) ) / (2*h)

def function_2(x):
    return np.sum(x**2)

#勾配を実装
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) #xと同じ形状の配列を生成
    
    for idx in range(x.size):
        tmp_val = x[idx]
        # f(x+h)の計算
        x[idx] = tmp_val + h
        fxh1   = f(x)
         
         #f(x-h)の計算
        x[idx] = tmp_val - h
        fxh2   = f(x)
         
        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val #値を元に戻す
    return grad

                    #関数 初期値  学習率    勾配法の試行回数
def gradient_descent(f, init_x, lr=0.01, step_num=100):
    x = init_x
    
    for i in range(step_num):
        grad = numerical_gradient(f, x)
        x -= lr * grad
        
    return x

     