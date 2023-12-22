# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 08:11:55 2023

@author: asus
"""

word = input("Enter your input please").strip()

uppercount = 0
lowercount = 0
 
 
for i in word:
    
    if i.isupper():
        uppercount += 1
    else:
        lowercount ++ 1
        
if uppercount > lowercount:
    correct= word.upper()
    
else:
    correct = word.lower()
    
print(correct)