import math


def is_prime(num):
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num < 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def generate_prime_sum_under(num):
    prime_sum = 0
    for i in range(1, num):
        if is_prime(i) is True:
            prime_sum += i
            print('...')
        else:
            pass

    return prime_sum

if __name__ == '__main__':
    print("sum of all primes below two million", generate_prime_sum_under(2000000))
