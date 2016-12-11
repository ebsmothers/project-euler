# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:09:37 2015

@author: evansmothers
"""

dvec = [1,10,100,1000,10000,100000,1000000]
i = 1
d = 1
ansvec = []
while d <= 1000000:
    for j in range(0,len(str(i))):
        if d in dvec:
            ansvec.append(str(i)[j])
        d += 1
    i += 1
        
print(ansvec)
    