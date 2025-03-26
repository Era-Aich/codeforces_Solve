# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 11:37:00 2025

@author: asus
"""

def cards(n,card):
    
    left , right =0,n-1
    turn = True
    siraj_card , dima_card = 0,0
    
    while left<=right:
        if card[left]> card[right]:
            chosen_card=card[left]
            left+=1
        else:
            chosen_card = card[right]
            right-=1
            
        if turn:
            siraj_card+=chosen_card
        else:
            dima_card+=chosen_card
            
        turn = not turn
    return siraj_card, dima_card


n = int(input())
card = list(map(int, input().split()))
sereja, dima = cards(n, card)
print(sereja, dima)
