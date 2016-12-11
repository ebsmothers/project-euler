# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:46:48 2015

@author: evansmothers
"""

import math
import sys

def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True
    
primevec = [x for x in range(2,100000) if isprime(x)]
noans = True
while noans == True:
    for xone in primevec[45:len(primevec)]:
        print(xone)
        for xtwo in primevec[0:primevec.index(xone)+1]:
            if isprime(int(str(xone)+str(xtwo))) and \
            isprime(int(str(xtwo)+str(xone))):
                for xthree in primevec[0:primevec.index(xtwo)+1]:
                    if isprime(int(str(xtwo)+str(xthree))) and \
                    isprime(int(str(xthree)+str(xtwo))) and \
                    isprime(int(str(xone)+str(xthree))) and \
                    isprime(int(str(xthree)+str(xone))):
                        for xfour in primevec[0:primevec.index(xthree)+1]:
                            if isprime(int(str(xthree)+str(xfour))) and \
                            isprime(int(str(xfour)+str(xthree))) and \
                            isprime(int(str(xtwo)+str(xfour))) and \
                            isprime(int(str(xfour)+str(xtwo))) and \
                            isprime(int(str(xone)+str(xfour))) and \
                            isprime(int(str(xfour)+str(xone))):
                                for xfive in primevec[0:primevec.index(xfour)+1]:
                                    if isprime(int(str(xthree)+str(xfive))) and \
                                    isprime(int(str(xfive)+str(xthree))) and \
                                    isprime(int(str(xtwo)+str(xfive))) and \
                                    isprime(int(str(xfive)+str(xtwo))) and \
                                    isprime(int(str(xone)+str(xfive))) and \
                                    isprime(int(str(xfive)+str(xone))) and \
                                    isprime(int(str(xfive)+str(xfour))) and \
                                    isprime(int(str(xfour)+str(xfive))):
                                            print('sum equals',sum([xone,xtwo, \
                                            xthree, xfour,xfive]))
                                            sys.exit()
                        
    