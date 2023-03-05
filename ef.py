
def isPrime(number): #1 for prime, 0 for not prime
    stopNum = number
    i=2
    while (i < stopNum):
        if number % i == 0:
            return 0
        stopNum = number / i
        i += 1
    return 1

def stringToElements(string): #Takes a string and individually breaks every element to list
    print("finish")