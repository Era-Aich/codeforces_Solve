# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:38:44 2023

@author: asus
"""

n, t = map(int,input().split())

s = list(input())

for _ in range(t):
    
    i = 0
    
    while i< n-1:
        if s[i] == 'B' and s[i+1] == 'G':
            s[i], s[i+1] = s[i+1],s[i]
            
            i +=2
        else:
            i+=1
    print("".join(s))
            

