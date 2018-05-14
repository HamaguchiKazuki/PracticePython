#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 17:19:40 2018

@author: hamaguchikazuki
"""

import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png')
plt.imshow(img)

plt.show()