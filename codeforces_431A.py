# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 10:15:32 2023

@author: asus
"""

# Reading input
calories = list(map(int, input().split()))
s = input()

# Calculating total calories
total_calories = sum(calories[int(strip) - 1] for strip in s)

# Outputting the result
print(total_calories)
