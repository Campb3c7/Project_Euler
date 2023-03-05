
def numdiv(number):
    count = 0
    for i in range(1,21):
        if ((number % i) == 0):
            count += 1
    if count == 20:
        print(number)

isTrue = False
number = 1
countn = 0
times = 0

while(isTrue == False):

    numdiv(number)
    number += 1
    countn += 1
    if countn == 1000000:
        print(countn*times)
        countn = 0
        times += 1
        
    
#This took a long time lmao

