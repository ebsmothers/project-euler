# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 11:23:24 2015

@author: evansmothers
"""

sequence = [[3,2]]
for i in range(1,1000):
    sequence.append([2*sequence[i-1][1]+sequence[i-1][0],\
    sequence[i-1][1]+sequence[i-1][0]])

ans = 0
for poop in sequence:
    if len(str(poop[0])) > len(str(poop[1])):
        ans += 1
print(ans)