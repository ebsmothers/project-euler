# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 13:37:35 2015

@author: evansmothers
"""

days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
months = [31,28,31,30,31,30,31,31,30,31,30,31]
counter = 0
currentday = 2
dayofmonth = 1
currentmonth = 1
currentyear = 1901

while currentyear <= 2000:
    currentday += 1
    currentday %= 7
    if currentyear % 4 == 0:
        isleapyear = True
    else:
        isleapyear = False
        
    if isleapyear and currentmonth == 2 and currentday == 28:
        currentday -= 1
    
    if dayofmonth < months[currentmonth-1]:
        dayofmonth += 1
    elif currentmonth < 12:
        currentmonth += 1
        dayofmonth = 1
    else:
        currentyear += 1
        dayofmonth = 1
        currentmonth = 1
        
    if dayofmonth == 1 and currentday == 0:
        counter += 1
        
print(counter)
    
    


