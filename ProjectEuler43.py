# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:56:02 2015

@author: evansmothers
"""
import math
digits = ['9','8','7','6','5','4','3','2','1','0']  
    
def permute(counter):
    number = ''
    availabledigits = ['9','8','7','6','5','4','3','2','1','0'] 
    for i in range(0,10):
        position = int(math.floor(counter/math.factorial(9-i)))
        number += availabledigits[position]
        counter -= (position*math.factorial(9-i))
        del availabledigits[position]
    return number

def doesitwork(n):
    if int(n[7:10]) % 17 == 0 and int(n[6:9]) % 13 == 0 \
    and int(n[5:8]) % 11 == 0 and int(n[4:7]) % 7 == 0 and int(n[5]) % 5 == 0 \
    and (int(n[2]) + int(n[3]) + int(n[4])) % 3 == 0 and int(n[3]) % 2 == 0:
        return True
    return False
    
counter = 0
ans = 0
while counter < math.factorial(10):
    currentnum = permute(counter)
    print(currentnum)
    if currentnum[0] != 0:
        if doesitwork(currentnum):
            ans += int(currentnum)
    counter += 1

print('i eat poop',ans)
        
    