# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:59:11 2020

@author: Nitin
"""

N = int(input(''))
if N in range(0,101):
    if N%2 != 0:
        print('Weird')
    elif N%2 == 0 and N in range(0,6):
        print('Not Weird')
    elif N%2 == 0 and N in range(6,21):
        print('Weird')
    elif N%2 == 0 and N in range(21,101):
        print('Not Weird')
else:
    print('invalid')

