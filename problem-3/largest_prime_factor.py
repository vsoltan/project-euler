#!/usr/bin/env python

import math

def all_primes_up_to(n):
  """Returns all primes up to the given number.
  
  Made after pseudocode in Wikipedia:
  https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
  
  For instance, all_primes_up_to(6) -> [2, 3, 5]
  """
  A = [True] * (n-1)
  for i in list(range(2, int(math.floor(math.sqrt(n))) + 1)):
    if A[i-2]:
      i2 = i**2
      for j in list(range(0, (n - i2)/i + 1)):
        A[i2 + j*i - 2] = False  # Convert number to its index in A by subtracting "2"
  # Convert Eratosthenes' sieve into primes
  primes = []
  for i in list(range(n-1)):
    if A[i]:
      primes.append(i + 2)  # Convert index i into number it represents by adding "2"
  return primes

def prime_factors(n):
  """Returns all prime factors of the given number.
  
  For instance, prime_factors(6) -> [2, 3]
  """
  print "finding primes up to {}".format(n)
  primes = all_primes_up_to(n)
  print "primes up to {}; {}".format(n, primes)
  factors = []
  quotient = n
  for p in primes:
    while quotient % p == 0:
      quotient /= p
      factors.append(p)
  return factors

if __name__ == '__main__':
  large_number = 600851475143
  print 'Prime factors of {}: {}'.format(
    large_number, prime_factors(large_number))
