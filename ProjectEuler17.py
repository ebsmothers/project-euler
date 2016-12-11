""" Lists of numbers 1-19 and all multiples of 10 under 100 """
numberslist = ['one','two','three','four','five','six','seven','eight','nine','ten'\
           ,'eleven','twelve','thirteen','fourteen','fifteen','sixteen',\
           'seventeen','eighteen','nineteen']
tenslist = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

""" Initialize lists for length of each word """
numberslength = []
tenslength = []

""" Populate word length lists """
for i in range(len(numberslist)):
    numberslength.append(len(numberslist[i]))
for j in range(len(tenslist)):
    tenslength.append(len(tenslist[j]))
print(numberslength)

""" Fill in lengths of first one hundred numbers """
ans = 0
numlength = 0
for num in range(1,100):
    if num < 20:
        ans += numberslength[num-1]
    else:
        ones = num % 10
        tens = int((num - ones)/10)
        if ones == 0:
            numlength = tenslength[tens-2]
            numberslength.append(numlength)
        else:    
            numlength = tenslength[tens-2] + numberslength[ones-1]
            numberslength.append(numlength)
        ans += numlength
       
""" Numbers from 100 to 999 """
pooplength = 0
for poop in range(100,1000):
    tensones = poop % 100
    hundreds = int((poop - tensones)/100)
    if tensones == 0:
        pooplength = 7 + numberslength[hundreds-1]
    else:
        pooplength = 10 + numberslength[hundreds-1] + numberslength[tensones-1]
    ans += pooplength
    
""" Dont forget 1000 """
ans += 11  
    
