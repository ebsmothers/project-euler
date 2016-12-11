# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 21:04:45 2015

@author: evansmothers
"""

def digitsum(num):
    numstrn = str(num)
    numlist = [int(digit) for digit in numstrn]
    return sum(numlist)

ans = 0
for a in range(1,100):
    for b in range(1,100):
        if digitsum(a**b) >= ans:
            ans = digitsum(a**b)
print(ans)
    
    