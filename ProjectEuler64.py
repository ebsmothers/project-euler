# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:12:21 2015

@author: evansmothers
"""

import math

def continuedfraction(n,sequencelength):
    ''' Initialize lists for numerators, denominators, terms in continued \
    fraction expansion '''
    termnum = [[0,0]]*sequencelength
    termden = [0]*sequencelength
    x = [0]*sequencelength
    x[0] = int(math.sqrt(n))
    termnum[0] = [1,x[0]]
    termden[0] = n - x[0]**2
    if termden[0] == 1:
        return 1
    
    ''' Loop through length of sequence filling continued fraction \
    expansion lists'''
    for i in range(1,sequencelength):
        x[i] = int((math.sqrt(n)*termnum[i-1][0] + termnum[i-1][1]) \
        /termden[i-1])
        termnum[i] = [termden[i-1],termden[i-1]*(x[i]*termden[i-1] \
        -termnum[i-1][1])]
        termden[i] = n - (termnum[i-1][1]-x[i]*termden[i-1])**2
        
        ''' Reduce fraction'''
        gcdi0 = math.gcd(termnum[i][0],termden[i])
        gcdi1 = math.gcd(termnum[i][1],termden[i])
        gcdi = math.gcd(gcdi0,gcdi1)
        termnum[i][0] = int(termnum[i][0]/gcdi)
        termnum[i][1] = int(termnum[i][1]/gcdi)
        termden[i] = int(termden[i]/gcdi)
        if termden[i] == 1:
            return i+1
        
    print(termnum)
    print(termden)
    print(x)

def issquare(n):
    if math.sqrt(n) - int(math.sqrt(n)) == 0:
        return True
    return False
    
nvec = [n for n in range(2,10001) if not issquare(n)]
ans = 0    
for n in nvec:
    if continuedfraction(n,10000) % 2 == 1:
        ans += 1
print('poop',ans)


        