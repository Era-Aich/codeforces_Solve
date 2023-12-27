# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 11:28:34 2023

@author: asus
"""


def dragon_count(k,l,m,n,d):
    count = 0
    for i in range(1,d+1):
        if i%k == 0 or i%l == 0 or i%m == 0 or i%n == 0:
            count +=1
            
    return count




k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
result = dragon_count(k, l, m, n, d)

print(result)