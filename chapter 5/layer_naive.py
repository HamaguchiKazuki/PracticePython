#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 09:55:26 2018

@author: hamaguchikazuki
"""

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None
        
def forward(self, x, y):
    self.x = x
    self.y = y
    out = x * y
    
    return out

#xとyをひっくり返す
def backward(self, dout):
    dx = dout * self.y
    dy = dout * self.x
    
    return dx, dy