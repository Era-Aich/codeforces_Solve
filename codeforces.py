# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 07:54:26 2023

@author: asus
"""

n = int(input())
gifts = list(map(int, input().split()))

# Initialize an empty list to store the result
result = [0] * n

# Iterate through the friends and determine who gave them a gift
for i in range(n):
    result[i] = gifts.index(i+1)+1

# Print the results
print(result)
