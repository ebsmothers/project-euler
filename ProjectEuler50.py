# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 10:54:37 2015

@author: evansmothers
"""
import math
def isprime(n):
    for i in range(2,int(math.floor(math.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True
    
'''primevec = [x for x in range(2,1000000) if isprime(x)]'''



'''ans = 0
currentbest = 0
for x in primevec[1:len(primevec)]:
    print(x)
    for i in range(0,primevec.index(x)-currentbest):
        startingterm = primevec[i]
        currentsum = startingterm
        j = primevec.index(startingterm) + 1
        while currentsum < x:
            currentsum += primevec[j]
            j += 1
        if currentsum == x:
            currentlength = j - i + 1
            if currentlength > currentbest:
                currentbest = currentlength
                ans = x
print(ans)'''

'''currentsum = 0
currentindex = 0
while currentsum <= primevec[len(primevec)-1]:
    currentsum += primevec[currentindex]
    currentindex += 1
maxlength = currentindex-1'''

def test(i,length):
    return isprime(sum(primevec[i:i+length]))

for length in range(maxlength,500,-1):
    print('length',length)
    i = 0
    while sum(primevec[i:i+length]) < 1000000:
        if test(i,length):
            print(sum(primevec[i:i+length]))
            sys.exit()
        else:
            i += 1
    
 

    
    