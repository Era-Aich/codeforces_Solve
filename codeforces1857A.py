# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 19:08:18 2025

@author: asus
"""


def arrray(n,arr):
    odd_list=[]
    even_list=[]
    
    for i in range(len(arr)):
        if arr[i]%2==0:
            even_list.append(arr[i])
        else:
            odd_list.append(arr[i])
    
    e = sum(even_list)
    o = sum(odd_list)
    
    if e%2==0 and o%2==0 or e%2!=0 and o%2!=0:
        return "YES"
    else:
        return "NO"
    

t= int(input())
for _ in range(t):
    
    n= int(input())
    arr= list(map(int,input().strip().split()))
    re = arrray(n, arr)
    print(re)
    