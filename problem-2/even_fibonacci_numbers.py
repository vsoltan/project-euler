#!/usr/bin/env python

class EulerError(Exception):
  """Base class for exceptions in project Euler."""
  pass

class FibonacciError(EulerError):
  """Base class for exceptions in Fibonacci module."""
  pass

FIBONACCI_CACHE = {}

def fibonacci_number(n):
  """Returns N-th Fibonacci number.
  
  For instance, fibonacci_numbers(5) -> 8
  """
  # Lookup Nth Fibonacci number in cache table
  if n in FIBONACCI_CACHE:
    return FIBONACCI_CACHE[n]

  if n < 1:
    raise FibonacciError('Fibonacci numbers are defined for natural numbers only.')
  elif n == 1 or n == 2:
    fib = n
  else:
    fib = fibonacci_number(n - 1) + fibonacci_number(n - 2)

  # Cache Nth Fibonacci number in lookup table
  FIBONACCI_CACHE[n] = fib
  return fib

def fibonacci_numbers_below(high_watermark):
  """Returns list of all Fibonacci numbers under given number.
  
  For instance, fibonacci_numbers_below(10) -> [1, 2, 3, 5, 8]
  """
  fib_nums = []
  fib_index = 1
  fib = fibonacci_number(fib_index)
  while fib < high_watermark:
    fib_nums.append(fib)
    fib_index += 1
    fib = fibonacci_number(fib_index)
  return fib_nums

def sum_of_even_fibonacci_numbers_below(high_watermark):
  """Returns list of all Fibonacci numbers under given number.
  
  For instance, sum_of_even_fibonacci_numbers_below(10) -> sum([2, 8]) -> 10.
  """
  fib_nums = fibonacci_numbers_below(high_watermark)
  return sum([x for x in fib_nums if x % 2 == 0])

if __name__ == '__main__':
  high_watermark = 4000000
  print 'Sum of Fibonacci numbers under {}: {}'.format(
    high_watermark, sum_of_even_fibonacci_numbers_below(high_watermark))
