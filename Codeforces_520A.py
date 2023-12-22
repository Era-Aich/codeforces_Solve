# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:01:13 2023

@author: asus
"""

def is_pangram(string):
    # Create a set of all lowercase letters in the alphabet
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    # Convert the input string to lowercase
    string = string.lower()

    # Check if all letters in the alphabet are present in the string
    for letter in alphabet:
        if letter not in string:
            return "NO"

    return "YES"

# Read input
n = int(input())
string = input()

# Check if it's a pangram and print the result
result = is_pangram(string)
print(result)
