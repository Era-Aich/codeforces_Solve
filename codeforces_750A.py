# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:05:56 2024

@author: asus
"""

def solved_problem(n,k):
    
    total_time = 240
    remain = total_time - k
    
    problem1 = 0
    
    for i in range(1, n+1):
        taken = 5*i
        if remain >= taken:
            problem1 +=1
            remain -=taken
        else:
            break
    return problem1

n , k = map(int, input().split())

result = solved_problem(n, k)

print(result)