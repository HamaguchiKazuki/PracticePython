#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:16:48 2018

@author: hamaguchikazuki
"""
import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    
    return y

