#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:54:08 2018

@author: hamaguchikazuki
"""

class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
        
    def hello(self):
        print("Hello " + self.name + "!")
        
    def goodbye(self):
        print("Good-bye " + self.name + "!")
        
m = Man("David")
m.hello()
m.goodbye()
    