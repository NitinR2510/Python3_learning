# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:48:41 2020

@author: Nitin
"""

import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    for i in range(len(arr)):
        arr[i] = float(arr[i])
    arr = numpy.array(arr)
    arr = arr[::-1]
    return arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)