# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:04:22 2015

@author: evansmothers
"""
import math
def permute(stringnum,k):
    newstringnum = ''
    for i in range(len(stringnum)):
        newstringnum += stringnum[(i-k) % len(stringnum)]
    return newstringnum
    
def isprime(n):
    
    for d in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % d == 0:
            return False
    return True
    
ans = 0
for n in range(2,1000000):
    addit = True
    for k in range(len(str(n))):
        if not isprime(int(permute(str(n),k))):
            addit = False
    if addit:
        ans += 1
        print(n)

print("Number of circular primes is",ans)

    
    