# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 08:07:27 2015

@author: evansmothers
"""

import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

'''primevec = [x for x in range(2,1000001) if isprime(x)]'''
 
def phi(n,primevec):
    totient = n
    i = 0
    stillleft = n
    while i < len(primevec) and primevec[i] <= stillleft:
        if n % primevec[i] == 0:
            totient = int(totient*(1-(1/primevec[i])))
            while stillleft % primevec[i] == 0:
                stillleft /= primevec[i]
        i += 1
    return totient

ans = 0    
currentmax = 0  
for n in range(500000,600000):
    print(n)
    if n/phi(n,primevec) >= currentmax:
        currentmax = n/phi(n,primevec)
        ans = n
print('ya hi', ans)
    