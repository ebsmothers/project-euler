# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:49:35 2015

@author: evansmothers
"""

import math
''' Find all numbers equalling their factorial digit sum'''
'''addme = []
for n in range(10,1000000):
    currentsum = 0
    for i in range(len(str(n))):
        currentsum += math.factorial(int(str(n)[i]))
    if currentsum == n:
       addme.append(n) 

loopvec = [1,2,169,363601,1454,871,45361,872,45362] + addme'''

ans = 0
for n in range(3,1000000):
    currentterm = n
    print(n)
    count = 1
    while currentterm not in loopvec and count <= 60:
        count += 1
        currentterm = sum([math.factorial(int(digit)) for digit in str(currentterm)])
        '''print('currentterm',currentterm,'count',count)'''
    if currentterm == 169 or currentterm == 363301 or currentterm == 1454:
        count += 2
    if currentterm == 871 or currentterm == 45361 or currentterm == 872 \
    or currentterm == 45362:
        count += 1
    print('returning',count)
    if count == 60:
        ans += 1
print('ieatpoop',ans)        