# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:42:09 2024

@author: asus
"""

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    
    
    # Iterate through the array to find the outlier
    for i in range(n):
        if i == 0:
            if a[i] != a[i + 1] and a[i] != a[i + 2]:
                print(i + 1)  # index in the problem statement is 1-based
                break
        elif i == n - 1:
            if a[i] != a[i - 1] and a[i] != a[i - 2]:
                print(i + 1)  # index in the problem statement is 1-based
                break
        else:
            if a[i] != a[i - 1] and a[i] != a[i + 1]:
                print(i + 1)  # index in the problem statement is 1-based
                break
