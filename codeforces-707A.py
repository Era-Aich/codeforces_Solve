# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 11:10:31 2023

@author: asus
"""

def is_color(n, m, matrix):
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] in ["C" or "W" or "G"]:
                return "#Color"
        
            return "#Black& White"        
    
n , m = map(int,input().split())

matrix = [input().split() for _ in range(n)]

result = is_color(n,m, matrix)

print(result)