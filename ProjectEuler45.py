# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 16:22:50 2015

@author: evansmothers
"""

pentagons = [int(n*(3*n-1)/2) for n in range(166,100000)]
hexagons = [int(n*(2*n-1)) for n in range(144,100000)]



haveans = False
while haveans == False:
    for pentagon in pentagons:
        print(pentagon)
        if pentagon in hexagons:
            haveans = True
            break
print(pentagon)