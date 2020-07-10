# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 05:39:34 2020

@author: Nitin
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
s = list(s)
m =[ ]
for i in range(len(s)):
    if s[i].islower():
        m.append(s[i])
m.sort()
u=[]
for i in range(len(s)):
    if s[i].isupper():
        u.append(s[i])
u.sort()
n = []
for i in range(len(s)):
    if s[i] in ['1','2','3','4','5','6','7','8','9','0']:
        n.append(int(s[i]))
o = []
e = []
for i in range(len(n)):
    if n[i]%2 !=0:
        o.append(n[i])
    else:
        e.append(n[i])
o.sort()
e.sort()
for i in range(len(o)):
    o[i] = str(o[i])
for i in range(len(e)):
    e[i] = str(e[i])
m = m+u+o+e
st = ''
for i in range(len(m)):
    st +=m[i]
print(st)