#!/usr/bin/env python

def generate_all_multiples_of(below, base):
  """Returns all mutiples of 'base' below given number.
  
  For instance, generate_all_multiples_of(10, 3) -> [3, 6, 9]
  """
  result = []
  multiple = base
  while multiple < below:
    result.append(multiple)
    multiple += base
  return result

def multiples_of_3_and_5_below(below):
  """Returns all mutiples of 3 and 5 below given number.
  
  For instance, multiples_of_3_and_5_below(10) -> [3, 5, 6, 9]
  """
  result = generate_all_multiples_of(below, 3)
  result.extend(generate_all_multiples_of(below, 5))
  # Return set() to remove duplicate entries, e.g.
  # result for below == 16 would contain two 15s: one generated by
  # multiples of 3, and the other - by multiples of 5.
  return set(result)

def sum_of_multiples_of_3_and_5_below(below):
  """Returns sum of all mutiples of 3 and 5 below given number.
  
  For instance, sum_of_multiples_of_3_and_5_below(10) -> sum([3, 5, 6, 9]) -> 23
  """
  return sum(multiples_of_3_and_5_below(below))

if __name__ == '__main__':
  print ('Sum of all the multiples of 3 or 5 below 1000: {}'.format(
      sum_of_multiples_of_3_and_5_below(1000)))
