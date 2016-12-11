# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:41:04 2015

@author: evansmothers
"""

import math
ans = 0
for n in range(10,1000000):
    sum = 0
    for i in range(len(str(n))):
        sum += math.factorial(int(str(n)[i]))
    if sum == n:
        ans += n
print("The sum is",ans)