# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 15:12:49 2023

@author: asus
"""

s = input()

number = [int(x) for x in s.split('+')]

number.sort()

result = '+'.join(map(str,number))

print(result)