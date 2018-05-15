#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 21:29:30 2018

@author: hamaguchikazuki
"""

import numpy as np

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum( t * np.log(y + delta) )

