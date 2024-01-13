# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 10:17:39 2024

@author: asus
"""


def round_number_representation(n):
    
    round = []
    power = 0
    
    while n > 0:
       digit =  n % 10
       if digit != 0:
           round.append(digit * (10**power))
           
       n//= 10
        
       power +=1
       
       return round[::-1]
       
       
t = int(input())

n = [int(input) for _ in range(t)]

roundnumber = round_number_representation(n)
print(len(roundnumber))
print(" ".join(map(str, roundnumber)))
