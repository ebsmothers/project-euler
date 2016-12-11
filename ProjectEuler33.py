# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:19:01 2015

@author: evansmothers
"""

for j in range(11,100):
    for i in range(10,j):
        i1 = int(str(i)[0])
        i2 = int(str(i)[1])
        j1 = int(str(j)[0])
        j2 = int(str(j)[1])
        if i1 == j1 and j2 != 0 and i2/j2 == i/j:
            print(str(i),str(j))
        if i1 == j2 and j1 != 0 and i2/j1 == i/j:
            print(str(i),str(j))
        if i2 == j1 and j2 != 0 and i1/j2 == i/j:
            print(str(i),str(j))
        if i2 == j2 and j1 != 0 and i1/j1 == i/j:
            print(str(i),str(j))
        