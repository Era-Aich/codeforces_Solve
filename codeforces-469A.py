# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 07:36:56 2023

@author: asus
"""

n = int(input())

p_info = list(map(int,input().split()))

q_info = list(map(int, input().split()))

p = set(p_info[1:])
q = set(q_info[1:])

all_level = set(range(1 , n+1))

if p.union (q) == all_level:
    print("I am the guys")
else:
    print("oh,  my keyboard")
