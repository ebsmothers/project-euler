# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 21:10:33 2015

@author: evansmothers
"""
import numpy as np
triangle = \
[[75],\
[95,64],\
[17,47,82],\
[18,35,87,10],\
[20,4,82,47,65],\
[19,1,23,75,3,34],\
[88,2,77,73,7,63,67],\
[99,65,4,28,6,16,70,92],\
[41,41,26,56,83,40,80,70,33],\
[41,48,72,33,47,32,37,16,94,29],\
[53,71,44,65,25,43,91,52,97,51,14],\
[70,11,33,28,77,73,17,78,39,68,17,57],\
[91,71,52,38,17,14,91,43,58,50,27,29,48],\
[63,66,4,68,89,53,67,30,73,16,69,87,40,31],\
[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

""" Find the maximum sum traversing triangle having n rows ending at index j """
def maxsum(triangle,n,j):
    currentrow = triangle[n-1]
    if n == 1:
        return triangle[0][0]
    else:
        smallertriangle = triangle[0:n-1]
        if j == 0:
            return maxsum(smallertriangle,n-1,0)+currentrow[0]
        elif j == len(currentrow)-1:
            return maxsum(smallertriangle,n-1,j-1)+currentrow[j]
        else:
            route1 = maxsum(smallertriangle,n-1,j-1)
            route2 = maxsum(smallertriangle,n-1,j)
            return max(route1,route2)+currentrow[j]
            
for i in range(15):
    print(maxsum(triangle,15,i))
                               