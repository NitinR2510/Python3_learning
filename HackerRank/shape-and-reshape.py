# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:55:00 2020

@author: Nitin
"""

import numpy
num = input()
num = num.split(" ")
for i in range(9):
    num[i] = int(num[i])
num = numpy.array(num)
num.shape = (3,3)
print(num)
