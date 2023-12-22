# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 20:01:08 2023

@author: asus
"""

n = int(input( ))

s = input().strip()

anton_win = s.count('A')
danik_win = s.count('D')

if anton_win > danik_win:
    print ("Anton")
    
elif anton_win < danik_win:
    print("Danik")
    
else:
    print("Friendship")