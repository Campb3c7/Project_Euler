currentNumber = 1
fPast = 1
sPast = 0
count = 0
while(currentNumber < 4000000):
    counted = currentNumber
    sPast = fPast
    fPast = currentNumber
    currentNumber = sPast + fPast
    if (counted % 2 == 0):
        count += counted
print(count)



