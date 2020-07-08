# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 11:00:34 2020

@author: Nitin
"""

def split_and_join(line):
    line = line.split(" ")
    line ="-".join(line)
    return line
    # write your code here
print(split_and_join("Hello World"))