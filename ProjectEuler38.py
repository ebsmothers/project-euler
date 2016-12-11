# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 09:31:27 2015

@author: evansmothers
"""
import math

def ispandigitalproduct(ans):
    isit = False
    for i in range(1,5):
        substring = str(ans)[0:i]
        currentposition = i
        n = 2
        while currentposition < len(str(ans)):
            testsubstring = int(substring)*n
            length = len(str(testsubstring))
            if str(testsubstring) != str(ans)[currentposition:currentposition+length]:
                currentposition = 20
            else:
                n += 1
                currentposition += length
            if currentposition == 9:
                isit = True
    return isit
    
        
digits = ['9','8','7','6','5','4','3','2','1']  
    
def permute(counter):
    number = ''
    availabledigits = ['9','8','7','6','5','4','3','2','1'] 
    for i in range(0,9):
        print(availabledigits)
        position = int(math.floor(counter/math.factorial(8-i)))
        print(position)
        number += availabledigits[position]
        counter -= (position*math.factorial(8-i))
        del availabledigits[position]
    return number
        
    
    



ans = 987654321
counter = 0
arewedone = False

while arewedone == False:
    ans = permute(counter)
    arewedone = ispandigitalproduct(ans)
    counter += 1
print('ya hi',ans)
    
