# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 17:49:24 2025

@author: asus
"""

def coin(k,r):
    x=1
    while True:
       total = x*k
       if total%10==0 or total%10==r:
            return x
       x+=1
   


k,r= map(int,input().strip().split())
result = coin(k,r)
print(result)