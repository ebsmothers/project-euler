# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:51:25 2015

@author: evansmothers
"""

import itertools


possiblevalues = range(1,10)
possibleanswers = []
for permutation in itertools.permutations(possiblevalues):
    vertices = [10] + [permutation[i] for i in range(0,9)]
    if vertices[5] <= 5 and vertices[6] <= 5:
        if 10 + vertices[5] == vertices[1] + vertices[7] and \
        vertices[1] + vertices[6] == vertices[2] + vertices[8] and \
        vertices[2] + vertices[7] == vertices[3] + vertices[9] and \
        vertices[3] + vertices[8] == vertices[4] + vertices[5] and \
        10 + vertices[6] == vertices[4] + vertices[9]:
            print(vertices)