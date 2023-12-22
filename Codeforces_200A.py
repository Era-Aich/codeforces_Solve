# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 07:59:08 2023

@author: asus
"""

n = int(input())  # Number of drinks
pi_values = list(map(int, input().split()))  # List of volume fractions

# Calculate the proportions of each drink as decimals
proportions = [pi / 100 for pi in pi_values]

# Calculate the total proportion of orange juice in the cocktail
total_proportion = sum(proportions) / n

# Convert the total proportion back to a percentage
cocktail_percentage = total_proportion * 100

# Print the result with 4 decimal places
print("{:.4f}".format(cocktail_percentage))
