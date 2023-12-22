# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 15:43:28 2023

@author: asus
"""


def valid_name(s):
    if len(s)!= 5 :
        return "NO"
    if s[0] == "T" and s[1:].islower():
        return "YES"
    if s[0]=="t" and s[1: ].isupper():
        return "yes"
    
    return "no"

n = int(input())
for _ in range(n):
    t = int(input())
    s = input()
    result = valid_name(s)
    print(result)