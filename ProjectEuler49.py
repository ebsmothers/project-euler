# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 19:47:38 2015

@author: evansmothers
"""
from itertools import permutations
from collections import OrderedDict
import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

def permute(strn):
    perms = [''.join(p) for p in permutations(strn)]
    perms = list(OrderedDict.fromkeys(perms))
    return perms

def isarithmeticsequence(permvec):
    sortedpermvec = sorted(permvec)
    for i in range(len(permvec)-2):
        currentdiff = sortedpermvec[i+1] - sortedpermvec[i]
        nextdiff = sortedpermvec[i+2] - sortedpermvec[i+1]
        doublediff = sortedpermvec[i+2] - sortedpermvec[i]
        if currentdiff == nextdiff and doublediff == 2*currentdiff:
            return (sortedpermvec[i],sortedpermvec[i+1],sortedpermvec[i+2])
    return False
        
def removecomposites(permvec):
    primevec = [x for x in permvec if isprime(x)]
    return primevec


for n in range(1000,10000):
    permvec = permute(str(n))
    permvec = [int(i) for i in permvec]
    primevec = removecomposites(permvec)
    if isarithmeticsequence(primevec) != False:
        print(isarithmeticsequence(primevec))
        
    
            
            
        
                
    