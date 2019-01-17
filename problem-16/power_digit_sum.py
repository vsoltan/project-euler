def Power(num, power):
    return (num ** power)


def getSumDigits(num):
    x = num
    l = list()
    while (len(l) < len(str(x))):
        digit = num % 10
        l.append(digit)
        num //= 10
    return sum(l)
