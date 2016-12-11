# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 13:07:45 2015

@author: evansmothers
"""

f = open("Documents/cipher.txt","r")
cipherfile = f.read()
f.close()

newcipherfile = cipherfile.replace('\n','')

cipherlist = []
currentindex = 0
currentterm = ''

while currentindex < len(newcipherfile):
    if newcipherfile[currentindex] != ',':
        currentterm += newcipherfile[currentindex]
        currentindex += 1
    else:
        cipherlist.append(int(currentterm))
        currentindex += 1
        currentterm = ''
print(cipherlist)

        
plaintextfile = []
key = [103,111,100]
for i in range(len(cipherlist)):
    plaintextfile.append(cipherlist[i] ^ key[i % 3])

print(sum(plaintextfile))
'''for term in plaintextfile:
    print(chr(term),end='')'''

