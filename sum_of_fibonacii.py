# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 16:37:48 2019

@author: Nitin

inspired by projecteuler Fibonacci series problem
"""
num = eval(input("Enter the maximum value to be reached: "))
a = 0
b = 1
l = [0,1]
j = 0
k=[]
while j<num:
    j = a+b
    l.append(j)
    a=b
    b=j
for j in range(len(l)):
    if l[j]>=num:
        l.remove(l[j])
for i in range(len(l)):
    if l[i]%2==0:
        k.append(l[i])
print(sum(k))
        

    
    

