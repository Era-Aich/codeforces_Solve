# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 16:02:04 2025

@author: asus
"""

#x1,x2,x3,x4 = map(int,input().split())

li = list(map(int, input().split()))

li.sort()
s=li[3]

a = s - li[2]
b = s-li[1]
c = s - li[0]

print(a,b,c)