# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:04:47 2015

@author: evansmothers
"""
import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

noans = True
k = 3
numberofprimes = 8
possibleprimes = 13
while noans:
    k += 1
    possibleprimes += 4
    n = 2*k+1
    for i in range(2,7,2):
        if isprime((n**2)-(i*k)):
            numberofprimes += 1
    if numberofprimes/possibleprimes < 0.1:
        noans = False
        print(n)
    