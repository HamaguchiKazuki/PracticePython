#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:28:26 2018

@author: hamaguchikazuki
"""

class Relu:
    def __init__(self):
        self.mask = None
        
    def forward(self, x):
        self.mask = (x <= 0)
        out = x.copy()
        out[self.mask] = 0
        
        return out
    
    def backward(self, dout):
        dout[self.mask] = 0
        dx = dout
        
        return dx
    
    