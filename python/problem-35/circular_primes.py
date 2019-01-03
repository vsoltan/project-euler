import math
from collections import deque


# works
def isPrime(num):
    if num == 0:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


# works
def getDigitList(num):
    x = num
    l = list()
    while (len(l) < len(str(x))):
        digit = num % 10
        l.append(digit)
        num /= 10
    l = [str(x) for x in l]
    return l[::-1]

    # "list isn't callable" because interfered, now ""'NoneType' object is not iterable""


def shift(l):
    x = deque(l)
    drotated = list(x.rotate(1))
    return drotated


# works
def combine(list):
    return int(''.join(list))


def function(num):
    for i in len(str(num)):
        if (isPrime(num) == True):
            num = shift(num)
        else:
            break


def checkCircularPrimeUnder(num):
    count = 0
    for i in range():
        count += 1
