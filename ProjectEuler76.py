# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 15:41:22 2015

@author: evansmothers
"""

p = [0]*100
p[0] = 1
p[1] = 2
for i in range(2,100):
    p[i] = sum([p[j] for j in range(int(i/2)+1)])+1

    
