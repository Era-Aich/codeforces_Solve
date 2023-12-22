# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 08:18:05 2023

@author: asus
"""

t = int(input())  # Number of test cases

moves = 0
for i in range(t):
    a, b = map(int, input().split())
    remainder = a % b  # Calculate the remainder

    if remainder == 0:
        moves = 0  # No moves needed if remainder is 0
    else:
        moves = b- remainder  # Calculate the number of moves needed

    print(moves)
