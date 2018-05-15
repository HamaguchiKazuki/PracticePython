#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 20:15:33 2018

@author: hamaguchikazuki
"""

import numpy as np

def mean_squared_error(y, t):
    return 0.5 * np.sum( (y-t)**2 )
