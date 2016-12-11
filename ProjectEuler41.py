# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:21:22 2015

@author: evansmothers
"""
import math
digits = ['9','8','7','6','5','4','3','2','1']  
    
def permute(counter):
    number = ''
    availabledigits = ['7','6','5','4','3','2','1'] 
    for i in range(0,7):
        position = int(math.floor(counter/math.factorial(6-i)))
        number += availabledigits[position]
        counter -= (position*math.factorial(6-i))
        del availabledigits[position]
    return number

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True
    
counter = 0
dowehaveans = False
while dowehaveans == False:
    print(permute(counter))
    if isprime(int(permute(counter))):
        dowehaveans = True
        print(int(permute(counter)))
    counter += 1
        