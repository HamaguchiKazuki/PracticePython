#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:38:10 2018

@author: hamaguchikazuki
"""
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    perceptlon = np.sum(w*x) + b
    if perceptlon <= 0:
        return 0
    else:
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) #重みとバイアスだけがANDと違う 
    b = 0.7
    perceptlon = np.sum(w*x) + b
    if perceptlon <= 0:
        return 0
    else:
        return 1
    
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    perceptlon = np.sum(w*x) + b
    if perceptlon <= 0:
        return 0
    else:
        return 1
    
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 =   OR(x1, x2)
    y  =  AND(s1, s2)
    return y

