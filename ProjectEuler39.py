# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:53:11 2015

@author: evansmothers
"""
import math

def numtriangles(p):
    num = 0
    for a in range(1,int(math.floor(p/2)+1)):
        for b in range(1,a):
            c = p - a - b
            if a**2 + b**2 == c**2:
                num += 1
    return num

pmax = 0
maxnum = 0
for p in range(15,1001):
    print(p)
    print(numtriangles(p))
    if numtriangles(p) > maxnum:
        maxnum = numtriangles(p)
        pmax = p
        
print('i eat poop',pmax)
    
                