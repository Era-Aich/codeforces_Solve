# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 08:33:46 2023

@author: asus
"""
n = int(input())  # Number of friends
gifts = list(map(int, input().split()))  # List of friends who received gifts

# Initialize an array to store the friend who gave a gift to each friend
givers = [0] * n

# Loop through the list of friends who received gifts
for i in range(n):
    givers[i] = gifts[i]

# Print the list of givers
print(*givers)
