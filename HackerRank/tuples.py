# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 05:38:51 2020

@author: Nitin
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))