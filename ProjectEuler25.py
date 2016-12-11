# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:51:30 2015

@author: evansmothers
"""


       
i = 1
fibonacci = []
dowehaveans = False
fibonacci.append(1)
fibonacci.append(1)
while dowehaveans == False:
    i += 1
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    if (len(str(fibonacci[i])) >= 1000):
        print(i+1)
        break
        dowehaveans == True