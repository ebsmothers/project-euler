# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:55:46 2015

@author: evansmothers
"""

import math
from fractions import Fraction

def issquare(n):
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        return True
    return False
    
def continuedfraction(n,sequencelength):
    termnum = [[0,0]]*sequencelength
    termden = [0]*sequencelength
    x = [0]*sequencelength
    x[0] = int(math.sqrt(n))
    termnum[0] = [1,x[0]]
    termden[0] = n - x[0]**2
    

    for i in range(1,sequencelength):
        x[i] = int((math.sqrt(n)*termnum[i-1][0] + termnum[i-1][1]) \
        /termden[i-1])
        termnum[i] = [termden[i-1],termden[i-1]*(x[i]*termden[i-1] \
        -termnum[i-1][1])]
        termden[i] = n - (termnum[i-1][1]-x[i]*termden[i-1])**2
        
        
        gcdi0 = math.gcd(termnum[i][0],termden[i])
        gcdi1 = math.gcd(termnum[i][1],termden[i])
        gcdi = math.gcd(gcdi0,gcdi1)
        termnum[i][0] = int(termnum[i][0]/gcdi)
        termnum[i][1] = int(termnum[i][1]/gcdi)
        termden[i] = int(termden[i]/gcdi)
    return x

Dvec = [D for D in range(2,1001) if not issquare(D)]
print(Dvec)
minsolution = [0]*len(Dvec)
for i in range(len(Dvec)):
    print('i',i)
    nosolution = True
    sequencelength = 1
    while nosolution:
        sequence = continuedfraction(Dvec[i],sequencelength)
        convergents = [0]*len(sequence)
        convergents[0] = sequence[len(sequence)-1]
        for j in range(1,len(sequence)):
            convergents[j] = sequence[len(sequence)-1-j]+Fraction(1,convergents[j-1])
        x = int(convergents[len(sequence)-1].numerator)
        y = int(convergents[len(sequence)-1].denominator)
        print('numerator',x)
        print('denominator',y)
        if x**2 == 1 + Dvec[i]*(y**2):
            nosolution = False
            minsolution[i] = x
        sequencelength += 1
        
ans = Dvec[minsolution.index(max(minsolution))]
print('poop',ans)
        

        