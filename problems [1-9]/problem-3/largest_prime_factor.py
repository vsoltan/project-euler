import math

"""script that finds the largest prime factor of a given number"""


def prime_factorization(num):
    if -2 < num < 2:  # no prime factors in this range
        return None

    num = abs(num)

    # initializations
    largest_factor = 1
    counter = math.sqrt(num)

    for i in range(2, num + 1):
        if num is 1 or counter is 0:  # early termination
            break
        if num % i != 0:
            continue
        else:
            counter = counter - 1
            while num % i is 0:
                num = num // i
                largest_factor = i

    return largest_factor


if __name__ == '__main__':
    print("the largest prime factor of the number 600851475143 is:", prime_factorization(600851475143))
