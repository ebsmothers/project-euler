# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:35:20 2015

@author: evansmothers
"""
    

def cyclelength(x):
    cycle = 1
    for i in range(1,10000):
        if 10**i % x == 1:
            cycle = i
            break
    return cycle+1

ans = 0
xvec = [x for x in range(2,999) if x % 2 != 0 and x% 5 != 0]
for x in xvec:
    cycle = cyclelength(x)
    if cycle > ans:
        ans = cycle

print(ans)
    