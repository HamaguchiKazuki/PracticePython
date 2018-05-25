#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:36:32 2018

@author: hamaguchikazuki
"""

class Sigmoid:
    def __init__(self):
        self.out = None
        
    def forward(self, x):
        out = 1 / (1 + np.exp(-x))
        self.out = out
        
        return out
    
    def backward(self, dout):
        dx = dout * (1.0 - self.out) * self.out
                    
        return dx
    