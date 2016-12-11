# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:34:55 2015

@author: evansmothers
"""
import math
def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

def truncateleft(strn,i):
    strn = strn[i:len(strn)]
    return strn
    
def truncateright(strn,i):
    strn = strn[0:len(strn)-i]
    return strn

def isit(n):
    if not isprime(n):
        return False
    for i in range(1,len(str(n))):
        if not isprime(int(truncateleft(str(n),i))):
            return False
        if not isprime(int(truncateright(str(n),i))):
            return False
    return True

counter = 0
ans = 0
n = 11
while counter < 11:
    if isit(n):
        ans += n
        counter += 1
    n += 2

print('ya hi',ans)
                

    
    
    
    