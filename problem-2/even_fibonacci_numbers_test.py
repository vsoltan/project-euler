#!/usr/bin/env python

import unittest
from even_fibonacci_numbers import FibonacciError
from even_fibonacci_numbers import fibonacci_number
from even_fibonacci_numbers import fibonacci_numbers_below
from even_fibonacci_numbers import sum_of_even_fibonacci_numbers_below

class TestStringMethods(unittest.TestCase):
  def test_fib_0(self):
    self.assertRaises(FibonacciError, fibonacci_number, 0)

  def test_fib_negative(self):
    self.assertRaises(FibonacciError, fibonacci_number, -1)

  def test_fib_seeds_1(self):
    self.assertEqual(fibonacci_number(1), 1)

  def test_fib_seeds_2(self):
    self.assertEqual(fibonacci_number(2), 2)

  def test_fib_recursive_3(self):
    self.assertEqual(fibonacci_number(3), 3)

  def test_fib_recursive_4(self):
    self.assertEqual(fibonacci_number(4), 5)

  def test_fib_recursive_5(self):
    self.assertEqual(fibonacci_number(5), 8)

  def test_fib_recursive_10(self):
    self.assertEqual(fibonacci_numbers_below(10), [1, 2, 3, 5, 8])

  def test_fib_recursive_15(self):
    self.assertEqual(fibonacci_numbers_below(15), [1, 2, 3, 5, 8, 13])

  def test_fib_recursive_25(self):
    self.assertEqual(fibonacci_numbers_below(25), [1, 2, 3, 5, 8, 13, 21])

  def test_fib_recursive_35(self):
    self.assertEqual(fibonacci_numbers_below(35), [1, 2, 3, 5, 8, 13, 21, 34])

  def test_sum_of_even_fib_numbers_below_10(self):
    self.assertEqual(sum_of_even_fibonacci_numbers_below(10), 10)

  def test_sum_of_even_fib_numbers_below_35(self):
    self.assertEqual(sum_of_even_fibonacci_numbers_below(35), 44)

  def test_sum_of_even_fib_numbers_below_4M(self):
    self.assertEqual(sum_of_even_fibonacci_numbers_below(4000000), 4613732)

if __name__ == '__main__':
  unittest.main()
