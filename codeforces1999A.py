# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 09:58:01 2025

@author: asus
"""

t= int(input())
for _ in range(t):
    n=int(input())
    
    k= list(map(int,str(n)))
    print(sum(k))
