# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:03:02 2015

@author: evansmothers
"""

import math

digits = ['1','2','3','4','5','6','7','8','9']

def ispandigitalproduct(n,a,b):
    if ispandigital(str(n)+str(a)+str(b)):
        return True
    else:
        return False

def ispandigital(numstring):
    if len(numstring) != 9:
        return False
    else:
        isit = True
        for digit in digits:
            if digit not in numstring:
                isit = False
        return isit

answervec = []        
for n in range(1000,10001):
    factorlist = [[x,int(n/x)] for x in  \
    range(1,int(math.floor(math.sqrt(n)))+1) if n % x == 0 ]
    for i in range(0,len(factorlist)):
        if ispandigitalproduct(n,factorlist[i][0],factorlist[i][1]) \
        and n not in answervec:
            answervec.append(n)

print("The sum is ",sum(answervec))