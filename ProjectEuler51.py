# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 22:36:01 2015

@author: evansmothers
"""

''' Find the smallest prime that is part of an eight prime value family'''

import math

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True

'''Replace i,j,k elements of strnx with each of digits 0 through 9, test \
primality and return results'''
def replace(i,j,k,strnx):
    counter = 0
    for newdigit in range(0,10):
        newstrnx = strnx[:i] + str(newdigit) + strnx[i+1:j] + str(newdigit) \
        + strnx[j+1:k] + str(newdigit) + strnx[k+1:]
        if isprime(int(newstrnx)) and newstrnx[0] != '0':
            counter += 1
    if counter >= 8:
        print(counter)
        return True
        
'''def replace(i,j,strnx):
    counter = 0
    for newdigit in range(0,10):
        newstrnx = strnx[:i] + str(newdigit) + strnx[i+1:j] + str(newdigit) \
        + strnx[j+1:]
        if isprime(int(newstrnx)):
            counter += 1
    if counter >= 7:
        return True
    return False'''

 
x = 56000
ans = False   
while not ans:
    x += 1
    if isprime(x):
        strnx = str(x)
        numdigits = len(strnx)
        for k in range(0,numdigits-1):
            for j in range(k):
                for i in range(j):
                    if replace(i,j,k,strnx):
                        print('ans',i,j,k,strnx)
                        ans = True
                        break

                        
                        
                        
        
        


       
        
        
        