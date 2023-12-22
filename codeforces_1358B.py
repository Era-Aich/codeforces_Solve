# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:09:08 2023

@author: asus
"""

def max_sum_after_swaps(n, k, a, b):
    a.sort()
    b.sort(reverse=True)

    for i in range(n):
        if k > 0 and b[i] > a[i]:
            a[i] = b[i]
            k -= 1

    return sum(a)

# Input reading
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Calculate and output the result
    result = max_sum_after_swaps(n, k, a, b)
    print(result)
