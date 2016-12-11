# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 18:50:14 2015

@author: evansmothers
"""

def ispalindrome(strn):
    if strn == strn[::-1]:
        return True
    return False
 
ans = 0   
for n in range(1,1000000):
    nbin = bin(n)[2:]
    if ispalindrome(str(nbin)) and ispalindrome(str(n)):
        ans += n
print('ya hi',ans)

        
    