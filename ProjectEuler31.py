# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:36:41 2015

@author: evansmothers
"""
target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print("Ways to make change =", ways[target])

            
    