# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:04:26 2020

@author: Nitin
"""

if __name__ == '__main__':
    l = []
    m = []
    for i in range(int(input())):
        name = input()
        m.append(name)
        score = float(input())
        m.append(score)
        l.append(m)
        m = [] 
    for i in range(len(l)):
        m.append(l[i][1])
    m = set(m)
    m = list(m)
    m.sort()
    n = []
    for i in range(len(l)):
        if m[1] == l[i][1]:
            n.append(l[i][0])
    n.sort()
    for i in n:
        print(i)