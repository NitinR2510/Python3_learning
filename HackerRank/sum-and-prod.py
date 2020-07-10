# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 05:56:27 2020

@author: Nitin
"""

import numpy
num = input()
num = num.split(" ")
for i in range(len(num)):
    num[i] = int(num[i])
N = num[0]
M = [ ]
for i in range(N):
    f = input()
    f = f.split(" ")
    for j in range(len(f)):
        f[j] = int(f[j])
    M.append(f)
M = numpy.array(M)
s = numpy.sum(M,axis = 0 )
s = numpy.array(s)
p = numpy.prod(s)
print(p)



