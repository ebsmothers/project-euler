# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:28:16 2015

@author: evansmothers
"""

def fifthpower(num):
    digitsum = 0
    for digit in str(num):
        digitsum += int(digit)**5
    return digitsum
  
ans = 0      
for num in range(2,1000000):
    if num == fifthpower(num):
        print(num)
        ans += num
print(ans)
    