# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:46:18 2023

@author: asus
"""



n = int(input())
s = list(map(int,input().split()))
bad_perfor = good_perfor = s[0]
count=0

for i in range(1,n):
    
    
    if(s[i]> good_perfor):
        count += good_perfor
    else:
        count= 0
        
print(count)
    
