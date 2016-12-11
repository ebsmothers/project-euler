# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 19:08:44 2015

@author: evansmothers
"""
 
ansvec = []   
for i in range(2,101):
    for j in range(2,101):
        if i**j not in ansvec:
            ansvec.append(i**j)
            
print(len(ansvec))
        