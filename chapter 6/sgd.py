#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 13:34:38 2018

@author: hamaguchikazuki
"""

class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
        
    def update(self, params, grads):
        for key in params.keys():
            prams[key] -= self.lr * grads[key]
            
