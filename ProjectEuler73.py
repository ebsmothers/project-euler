# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 08:02:41 2015

@author: evansmothers
"""

import math

ans = 0

for d in range(4,12001):
    lowerbound = math.floor(d/3)+1
    upperbound = math.floor(d/2)
    for i in range(lowerbound,upperbound+1):
        if math.gcd(i,d) == 1:
            ans += 1
print('poop',ans)