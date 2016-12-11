# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 14:42:33 2015

@author: evansmothers
"""
import math
perimetervec = [0] * 750000
for m in range(866,1,-1):
    print(m)
    for n in range((m % 2) + 1,m,2):
        if math.gcd(m,n) == 1:
            primitivea = m**2 - n**2
            primitiveb = 2*m*n
            primitivec = m**2 + n**2
            perimeter = primitivea + primitiveb + primitivec
            k = 1
            while k*perimeter <= 1500000:
                perimetervec[int(k*perimeter/2)-1] += 1                 
                k += 1

ans = 0
for poop in perimetervec:
    if poop == 1:
        ans += 1
print('ya hi', ans)
    
                
            
                
            
        