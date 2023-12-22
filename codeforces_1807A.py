# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:15:29 2023

@author: asus
"""

t = int(input())


for i in range(t):
    
    a , b, c = map(int,input().split())
    sum = a+b
    if c == sum:
        print("+")
    else:
        print("-")
        