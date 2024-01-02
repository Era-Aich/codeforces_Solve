# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 11:02:15 2023

@author: asus
"""


n = int(input())
magnets = [input() for _ in range(n)]

groups = 1  # Initialize with 1 group since there is at least one magnet
for i in range(1, n):
    if magnets[i] != magnets[i - 1]:
        groups += 1

print(groups)
