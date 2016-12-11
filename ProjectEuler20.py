# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:17:31 2015

@author: evansmothers
"""

import math
bigguy = math.factorial(100)

def sumdigits(number):
    sum = 0
    listofints = [int(i) for i in str(number)]
    for digit in listofints:
        sum += int(digit)
    return sum

print(sumdigits(bigguy))