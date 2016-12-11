# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:23:52 2015

@author: evansmothers
"""

ans = 0
i = 1
while len(str(9**i)) >= i:
    for j in range(1,10):
        if len(str(j**i)) == i:
            ans += 1
    i += 1
print('i eat my own shit',ans)
    