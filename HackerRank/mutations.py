# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:02:25 2020

@author: Nitin
"""

def mutate_string(string, position, character):
    l = list(string)
    l[position]=character
    string = "".join(l)
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)