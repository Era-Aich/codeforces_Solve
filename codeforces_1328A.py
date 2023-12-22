# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:09:01 2023

@author: asus
"""

n = int(input())
count = 0

for i in range(n):
    
    a,b = map(int, input().split())

    remainder = a%b
    if remainder != 0:
        count = b- remainder
    else: 
         
            count = 0
        
    print(count)