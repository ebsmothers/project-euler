# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:22:22 2015

@author: evansmothers
"""

import math

def choose(n,k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

ans = 0    
for n in range(23,101):
    for k in range(1,n+1):
        if choose(n,k) >= 1000000:
            ans += 1
                
print(ans)