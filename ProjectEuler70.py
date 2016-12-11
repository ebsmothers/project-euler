# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:47:38 2015

@author: evansmothers
"""

import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True
    
'''primevec = [x for x in range(2,10000001) if isprime(x)]'''
otherprimevec = [x for x in range(2000,5001) if isprime(x)]

def isperm(x1,x2):
    str1 = str(x1)
    str2 = str(x2)
    digits1 = [0]*10
    digits2 = [0]*10
    if len(str1) == len(str2):
        for i in range(len(str1)):
            currentdigit1 = int(str1[i])
            currentdigit2 = int(str2[i])
            digits1[currentdigit1] += 1
            digits2[currentdigit2] += 1
        if digits1 == digits2:
            return True
    return False
    
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
currentmin = 50    
'''for n in range(1000000,10000000):
    print(n)
    if isperm(n,phi(n,primevec)):
        if n/phi(n,primevec) < currentmin:
            currentmin = n/phi(n,primevec)
            ans = n'''
for x in otherprimevec:
    print(x)
    for y in otherprimevec:
        if x*y < 10000000:
            if isperm(x*y,phi(x*y,primevec)):
                if x*y/phi(x*y,primevec) < currentmin:
                    currentmin = x*y/phi(x*y,primevec)
                    ans = x*y
            
print('ya hi', ans)