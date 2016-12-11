# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 20:02:49 2015

@author: evansmothers
"""

import math

ans = 0
currentbest = 0
for d in range(8,1000001):
    numerator = math.floor(3/7*d)
    if math.gcd(numerator,d) == 1:
        if numerator/d > currentbest:
            currentbest = numerator/d
            ans = numerator
print('poop',ans)
    