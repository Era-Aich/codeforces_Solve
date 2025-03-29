# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 09:12:49 2025

@author: asus
"""
n=int(input())
a=list(map(int,input().strip().split()))
maxi = max(a)
s=[]

for i in range(n):
    sub = maxi-a[i]
    s.append(sub)
    count=max(s)
    
    
    
#print(maxi)
print(count)
    