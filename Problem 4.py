
def flip(startingNum):
    j=6
    endNum = 0
    for i in range(1,7):
        endNum += ((((startingNum % 10**i) / 10 ** (i-1))*(10**j)) / 10)
        j -= 1
        startingNum -= (startingNum % 10**(i))
    
    return endNum

def ispalin(number):
    if number == flip(number):
        print(number)
    

for i in range(900,1000):
    for j in range(900,1000):
        number = i * j
        ispalin(number)

    



    

        

print("done")