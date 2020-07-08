# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:25:17 2020

@author: Nitin
"""

import numpy
dim = input()
dim = dim.split(" ")
N = int(dim[0])
M = int(dim[1])
my_array = [ ]
for i in range(N):
    f = input()
    f = f.split(" ")
    for j in range(len(f)):
        f[j] = int(f[j])
    my_array.append(f)
my_array = numpy.array(my_array)
print(numpy.transpose(my_array))
print(my_array.flatten())


