import ef

#output every prime and count
count = 0
i = 2
while count < 10002:
    if ef.isPrime(i) == 1:
        count += 1
        print("{} is the {} prime".format(i,count))
    i += 1
