import math


def isPrime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def generatePrimeSumUnder(num):
    primeSum = 0
    for i in range(1, num):
        if (isPrime(i) == True):
            primeSum += i
            print(primeSum)
        else:
            pass

    return primeSum
