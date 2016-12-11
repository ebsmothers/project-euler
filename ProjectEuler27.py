# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 15:55:41 2015

@author: evansmothers
"""

import math

def isprime(x):
    if x <= 1:
        return False
    else:    
        for i in range(2,int(math.floor(math.sqrt(x)+1))):
            if x % i == 0:
                return False
    return True

primevec = [x for x in range(2,1000) if isprime(x)]


def maxprimelength(a,b):
    n = 1
    while isprime(n**2 + a*n + b):
        n += 1
    return n
    


maxlength = 0   
for a in range(-200,1000):
    for b in primevec:
        print(a)
        print(b)
        if maxprimelength(a,b) > maxlength:
            maxlength = maxprimelength(a,b)
            ans = a*b
    
print(ans)