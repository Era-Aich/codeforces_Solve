# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 09:42:22 2025

@author: asus
"""

def subsegment(n,k,arr):
    
    count_k = arr.count(k)
    
    if count_k == 0:
        return "No"
    
    if n==1:
        return "YES" if arr[0]==k else "NO"

     
    for i in range(n-1):
        if arr[i]==k:
            
            if arr[i+1]==k or (i+2<n and arr[i+2]==k):
                return "YES"
    return "YES"




t = int(input())

for _ in range(t):
    n,k = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    
    re = subsegment(n,k,arr)
    print(re)