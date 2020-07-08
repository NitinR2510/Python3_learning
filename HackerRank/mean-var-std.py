# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:17:54 2020

@author: Nitin
"""

import numpy
dim = input()
dim = dim.split(" ")
x = int(dim[0])
y = int(dim[1])
my_array = [ ]
for i in range(x):
    f = input()
    f = f.split(" ")
    for j in range(len(f)):
        f[j] = int(f[j])
    my_array.append(f)
my_array = numpy.array(my_array)
numpy.set_printoptions(legacy='1.13')
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
print(numpy.std(my_array))
    