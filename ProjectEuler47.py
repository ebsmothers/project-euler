# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:27:17 2015

@author: evansmothers
"""

import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True
    
primes = [x for x in range(2,10000) if isprime(x)]

def primefactors(n,primes):
    numfactors = 0
    smallerprimes = [prime for prime in primes if prime < n]
    for prime in smallerprimes:
        if n % prime == 0:
            numfactors += 1
    return numfactors
    

noansyet = True
n = 644
while noansyet:
    if primefactors(n,primes) >= 4:
        if primefactors(n+1,primes) >= 4:
            if primefactors(n+2,primes) >= 4:
                if primefactors(n+3,primes) >= 4:
                    noansyet = False
                    print('yayayaya',n)
    n += 1
    
    