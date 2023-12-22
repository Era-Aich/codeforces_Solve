# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 07:45:46 2023

@author: asus
"""

n = int(input())

s = input()

removal_count = 0

for i in range(1,n):
    if s[i] == s[i-1]:
        removal_count +=1
        
print(removal_count)