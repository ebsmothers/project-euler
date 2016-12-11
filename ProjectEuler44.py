# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:59:36 2015

@author: evansmothers
"""

pentagonal = [int(n*(3*n-1)/2) for n in range(1,5000)]


absans = 1000000000000000000000
for a in pentagonal:
    for b in pentagonal:
        if b < a:
            print(a,b)
            if a+b in pentagonal and a-b in pentagonal:
                if abs(a-b) < absans:
                    absans = abs(a-b)
                    aans = a
                    bans = b
                
print('yahi',absans)
