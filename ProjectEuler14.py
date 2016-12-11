import math
def collatzlength(num):
    length = 1
    currentterm = num
    while currentterm != 1:
        if currentterm %2 == 0:
            currentterm /= 2
        else:
            currentterm = (3*currentterm) + 1
        length = length + 1
    return length

maxlength = 0
maxnum = 0
for num in range(1,1000000):
    if collatzlength(num) > maxlength:
        maxlength = collatzlength(num)
        maxnum = num
print(maxnum)
