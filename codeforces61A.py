# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 10:39:50 2023

@author: asus
"""

# Read input numbers
number1 = input().strip()
number2 = input().strip()

# Initialize an empty string to store the result
result = ""

# Iterate through the digits of the two numbers and perform XOR
for digit1, digit2 in zip(number1, number2):
    result += '1' if digit1 != digit2 else '0'

# Print the result
print(result)

    