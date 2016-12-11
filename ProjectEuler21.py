# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 16:54:26 2015

@author: evansmothers
"""
import math

def divisorsum(n):
    sum = 1
    for d in range(2,int(math.floor(math.sqrt(n)))):
        if n % d == 0:
            sum += d + int(n/d)
            if d**2 == n:
                sum -= d
    return sum

ans = 0
for n in range(1,10001):
    a = divisorsum(n)
    if divisorsum(a) == n and a != n:
        ans += a + n
ans = int(ans/2)
print(ans)

'''nvec = range(1,10000)   
divisorsumvec = []
for n in nvec:
    divisorsumvec.append(divisorsum(n))

ans = 0
for a in nvec:
    b = divisorsumvec[a]
    if b <= len(divisorsumvec) and divisorsumvec[b-1] == a+1 and a != b:
        ans += a+b+1
        
print(ans)'''
          

    