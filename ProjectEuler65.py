# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 15:43:01 2015

@author: evansmothers
"""
from fractions import Fraction
sequence = [2]
for n in range(1,34):
    sequence.append(1)
    sequence.append(2*n)
    sequence.append(1)

convergents = [0]*100
convergents[0] = sequence[99]
for i in range(1,100):
    convergents[i] = sequence[99-i]+Fraction(1,convergents[i-1])
    print(convergents[i])
    