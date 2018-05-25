#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:34:45 2018

@author: hamaguchikazuki
"""

class Affine:
    def __init__(self, W, b):
        self.W  = W
        self.b  = b
        self.x  = None
        self.dW = None
        self.db = None
        
    def forward(self, x):
        self.x = x
        out = np.dot(x, self.W) + self.b
                    
        return out
    
    # T=転置
    def backward(self, dout):
        dx = np.dot(dout, self.W.T)
        self.dW = np.dot(self.x.T, dout)
        self.db = np.sum(dout, axis=0)
        
        return dx
    
