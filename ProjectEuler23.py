# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:23:23 2015

@author: evansmothers
"""

import math

def sumdivisors(n):
    sum = 1
    for d in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % d == 0:
            sum += (d + int(n/d))
        if d*d == n:
            sum -= d
    return sum
print(sumdivisors(12))    
def isabundant(n):
    if sumdivisors(n) > n:
        return True
    else:
        return False

abundantvec = [x for x in range(1,28124) if isabundant(x)]        
            
def issumofabundant(n,abundantvec):
    isit = False
    for x in abundantvec:
        if n-x in abundantvec:
            isit = True
            break
    return isit
    
ans = 0   
for n in range(1,28124):
    if not issumofabundant(n,abundantvec):
        ans += n
        print(n)
        
print(ans)
    
    
    
    
