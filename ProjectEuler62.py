# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:30:32 2015

@author: evansmothers
"""

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
            
            
                

cubes = [x**3 for x in range(345,10000)]


for i in range(len(cubes)):
    x = cubes[i]
    print(i)
    numperms = 0
    for j in range(i,len(cubes)):
        if isperm(x,cubes[j]):
            numperms += 1
    if numperms == 5:
        print('poop',x)
        break
        