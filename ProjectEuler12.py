import math
n = 0
solution = False

def isperfectsquare(poop):
    if math.sqrt(poop) == math.floor(math.sqrt(poop)):
        return True
    else:
        return False

def numdivisors(poop):
    divisors = 0
    for n in range(1,int(math.sqrt(poop))+1):
        if poop % n == 0:
            divisors += 2
    if isperfectsquare(poop):
        divisors -= 1
    return divisors

while solution == False:
    n = n+1
    triangle = sum(range(1,n))
    divisors = numdivisors(triangle)
    if divisors > 500:
        solution == True
        break
print(triangle)

            
