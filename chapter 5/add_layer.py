#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 10:17:36 2018

@author: hamaguchikazuki
"""

class AddLayer:
    def __init__(self):
        pass
    
    def forward(self, x, y):
        out = x + y
        return out
    
    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1
        return dx, dy
    