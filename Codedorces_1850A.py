# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 20:40:27 2023

@author: asus
"""

n = int(input())

for _ in range(n):
    a,b,c = map(int,input().split())
    if a+b>=10 or a+c>=10 or b+c>=10:
        print("YES")
    else:
        print("NO")
    
    
