# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 05:51:21 2020

@author: Nitin
"""

import numpy
numpy.set_printoptions(legacy='1.13')
a = input()
a = a.split(" ")
for i in range(len(a)):
    a[i] = float(a[i])
a = numpy.array(a)
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))


