dick = 2**1000
stringdick = str(dick)
poop = []

for char in range(0,len(stringdick)):
    poop.append(int(stringdick[char]))

ans = sum(poop)
print(ans)
