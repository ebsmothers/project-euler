# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 13:29:43 2015

@author: evansmothers
"""

import itertools

trinums = [int(n*(n+1)/2) for n in range(45,141)]
squarenums = [n**2 for n in range(34,100)]
pentnums = [int(n*(3*n-1)/2) for n in range(26,82)]
hexnums = [n*(2*n-1) for n in range(23,71)]
heptnums = [int(n*(5*n-3)/2) for n in range(21,64)]
octnums = [n*(3*n-2) for n in range(19,59)]

def parse(nums):
    numslist = [[] for x in range(100)]
    for num in nums:
        strnum = str(num)
        numslist[int(strnum[0]+strnum[1])].append(num)
    return numslist

triangle = parse(trinums)
square = parse(squarenums)
pentagon = parse(pentnums)
hexagon = parse(hexnums)
heptagon = parse(heptnums)
octagon = parse(octnums)

options = [triangle,square,pentagon,hexagon,heptagon]
permoptions = list(itertools.permutations(options))

for n in range(len(permoptions)):
    currentorder = permoptions[n]
    for number in octnums:
        strnum = str(number)
        if currentorder[0][int(strnum[2]+strnum[3])] != []:
            for secondnum in currentorder[0][int(strnum[2]+strnum[3])]:
                strnum2 = str(secondnum)
                if currentorder[1][int(strnum2[2]+strnum2[3])] != []:
                    for thirdnum in currentorder[1][int(strnum2[2]+strnum2[3])]:
                        strnum3 = str(thirdnum)
                        if currentorder[2][int(strnum3[2]+strnum3[3])] != []:
                            for fourthnum in currentorder[2][int(strnum3[2]+strnum3[3])]:
                                strnum4 = str(fourthnum)
                                if currentorder[3][int(strnum4[2]+strnum4[3])] != []:
                                    for fifthnum in currentorder[3][int(strnum4[2]+strnum4[3])]:
                                        strnum5 = str(fifthnum)
                                        if currentorder[4][int(strnum5[2]+strnum5[3])] != []:
                                            for sixthnum in currentorder[4][int(strnum5[2]+strnum5[3])]:
                                                strnum6 = str(sixthnum)
                                                if strnum6[2] == strnum[0] and strnum6[3] == strnum[1]:
                                                    print('yahi',number+secondnum+thirdnum\
                                                    +fourthnum+fifthnum+sixthnum)
                                        


