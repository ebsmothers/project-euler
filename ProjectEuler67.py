# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 21:11:50 2015

@author: evansmothers
"""

f = open("Documents/ieatpoop.txt","r")
triangle = f.read()
f.close()
triangle = triangle.replace('\n', ' ')

''' Convert string triangle into list of ints '''
def convert(triangle):
    trianglelist = []
    for i in range(0,len(triangle),3):
        tens = int(triangle[i])
        ones = int(triangle[i+1])
        number = 10*tens+ones
        trianglelist.append(number)             
    return trianglelist

inttriangle = convert(triangle)

''' Convert single list into rows and columns'''
def listoflists(inttriangle):
    newtriangle = [[] for j in range(0,100)]
    rowstart = 0
    for i in range(100):
        counter = 0
        row = newtriangle[i]
        if i > 0:
            rowstart = int((i*(i+1)/2))
        while counter <= i:
            row.append(inttriangle[rowstart+counter])
            counter += 1
        newtriangle[i] = row
    return newtriangle
            
newtriangle = listoflists(inttriangle)

print(newtriangle)
maxsum = [[0]*n for n in range(1,101)]
maxsum[0][0] = newtriangle[0][0]
for i in range(1,100):
    for j in range(i):
        if j == 0:
            maxsum[i][j] = maxsum[i-1][j] + newtriangle[i][j]
        if j == i-1:
            maxsum[i][j] = maxsum[i-1][j-1] + newtriangle[i][j]
        else:
            maxsum[i][j] = max(maxsum[i-1][j-1],maxsum[i-1][j]) \
            + newtriangle[i][j]
print('ya hi',max(maxsum[99]))
        


