# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 13:10:27 2015

@author: evansmothers
"""

'''Find out if x and y are permutations of one another'''
def isperm(x,y):
    if len(str(x)) == len(str(y)):
        strnx = str(x)
        strny = str(y)
        xdigits = [0]*10
        ydigits = [0]*10
        for digit in strnx:
            xdigits[int(digit)] += 1
        for digit in strny:
            ydigits[int(digit)] += 1
        if xdigits == ydigits:
            return True
    return False


currentorder = 5
noans = True
x = 10**currentorder
while noans:
    if x > int((10**(currentorder+1))/6):
        currentorder += 1
        x = 10**currentorder
    else:
        if isperm(x,2*x) and isperm(x,3*x) and isperm(x,4*x) \
        and isperm(x,5*x) and isperm(x,6*x):
            noans = False
            print(x)
        x += 1
        