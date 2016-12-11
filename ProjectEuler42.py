# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:41:21 2015

@author: evansmothers
"""

triangularnumbers = [int(x*(x+1)/2) for x in range(1,50) if x*(x+1)/2 <= 500]
f = open("Documents/bunchofshit.txt","r")
wordfile = f.read()
f.close()

def purify(wordfile):
    words = []
    i = 1
    while i < len(wordfile):
        currentword = ''
        while wordfile[i] != '"': 
            currentword += wordfile[i]
            i += 1
        else:
            i += 3
            words.append(currentword)
    return words
wordslist = purify(wordfile)

def wordscore(word):
    alphabet = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N', \
    'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    score = 0
    for char in word:
        score += alphabet.index(char)
    return score

ans = 0
for word in wordslist:
    if wordscore(word) in triangularnumbers:
        ans += 1

print('you\'re stupid', ans)