# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:09:16 2015

@author: evansmothers
"""
import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

def isgoldbach(n):
    i = 1
    while 2*i**2 < n - 3:
        if isprime(n-(2*i**2)):
                return True
        else:
            i += 1
    return False

isans = False
n = 3
while not isans:
    n += 2
    if not isprime(n):
        isans = not(isgoldbach(n))
print(n)
        
        
        

    
                