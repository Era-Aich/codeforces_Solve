# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 09:12:03 2025

@author: asus
"""

def spy(n,a):
    #a.sort()
   majority=a[0] if a[0]==a[1] else a[2]
   for i in range(n):
       if a[i]!=majority:
           return i+1
                
                
            
t=int(input())  
for _ in range(t):        
    n= int(input())
    a=list(map(int,input().strip().split()))
    print(spy(n,a))
                