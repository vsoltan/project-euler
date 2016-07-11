#!/usr/bin/env python

import unittest
from largest_prime_factor import all_primes_up_to
from largest_prime_factor import prime_factors

class TestStringMethods(unittest.TestCase):
  def test_all_primes_1(self):
    self.assertEqual(all_primes_up_to(1), [])

  def test_all_primes_2(self):
    self.assertEqual(all_primes_up_to(2), [2])

  def test_all_primes_3(self):
    self.assertEqual(all_primes_up_to(3), [2, 3])

  def test_all_primes_4(self):
    self.assertEqual(all_primes_up_to(4), [2, 3])

  def test_all_primes_5(self):
    self.assertEqual(all_primes_up_to(5), [2, 3, 5])

  def test_all_primes_6(self):
    self.assertEqual(all_primes_up_to(6), [2, 3, 5])

  def test_all_primes_30(self):
    self.assertEqual(all_primes_up_to(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

  def test_factors_of_2(self):
    self.assertEqual(prime_factors(2), [2])

  def test_factors_of_3(self):
    self.assertEqual(prime_factors(3), [3])

  def test_factors_of_4(self):
    self.assertEqual(prime_factors(4), [2, 2])

  def test_factors_of_6(self):
    self.assertEqual(prime_factors(6), [2, 3])

  def test_factors_of_7(self):
    self.assertEqual(prime_factors(7), [7])

  def test_factors_of_8(self):
    self.assertEqual(prime_factors(8), [2, 2, 2])

  def test_factors_of_13195(self):
    self.assertEqual(prime_factors(13195), [5, 7, 13, 29])

if __name__ == '__main__':
  unittest.main()
