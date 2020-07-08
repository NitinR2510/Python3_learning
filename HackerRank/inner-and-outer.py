# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:48:29 2020

@author: Nitin
"""

import numpy
a = input()
b = input()
a = a.split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
b = b.split(" ")
for i in range(len(b)):
    b[i] = int(b[i])
a = numpy.array(a)
b = numpy.array(b)
print (numpy.inner(a,b))
print (numpy.outer(a,b))



