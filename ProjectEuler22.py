# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:41:46 2015

@author: evansmothers
"""

f = open("Documents/names.txt","r")
namefile = f.read()
f.close()


def purify(namefile):
    names = []
    i = 1
    while i < len(namefile):
        currentname = ''
        while namefile[i] != '"': 
            currentname += namefile[i]
            i += 1
        else:
            i += 3
            names.append(currentname)
    return names

namelist = purify(namefile)
sortednames = sorted(namelist)

def namescore(name):
    alphabet = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N', \
    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    score = 0
    for char in name:
        score += alphabet.index(char)
    return score

ans = 0
for name in sortednames:
    ans += (sortednames.index(name)+1)*namescore(name)
print(sortednames)
print(ans)
    
        
        

        
