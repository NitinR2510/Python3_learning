# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:19:19 2020

@author: Nitin
"""
import numpy
num = int(input())
a =[]
b =[]
for i in range(num):
    f = input()
    f = f.split(" ")
    for j in range(len(f)):
        f[j] = int(f[j])
    a.append(f)
for i in range(num):
    f = input()
    f = f.split(" ")
    for j in range(len(f)):
        f[j] = int(f[j])
    b.append(f)
a = numpy.array(a)
b = numpy.array(b)
print(a.dot(b))
       




