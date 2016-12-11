# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:57:04 2015

@author: evansmothers
"""

def islychrel(n):
    currentnum = n
    for i in range(1,50):
        currentnum += int(str(currentnum)[::-1])
        if currentnum == int(str(currentnum)[::-1]):
            return False
    return True
        
    
ans = 0
for n in range(1,10000):
    if islychrel(n):
        ans += 1
print(ans)