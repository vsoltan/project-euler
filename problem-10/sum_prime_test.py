#!/usr/bin/env python

import unittest
from sum_prime import isPrime
from sum_prime import generatePrimeSumUnder

class TestStringMethods(unittest.TestCase):
  def test_is_Prime_0(self):
    self.assertFalse(isPrime(0))
  def test_isPrime_1(self):
    self.assertFalse(isPrime(1))
  def test_isPrime_2(self):
    self.assertTrue(isPrime(2))
  def test_is_Prime_3(self):
    self.assertTrue(isPrime(3))
  def test_is_Prime_8(self):
    self.assertFalse(isPrime(8))
  def test_is_Prime_9(self):
    self.assertFalse(isPrime(9))
  def test_is_Prime_10(self):
    self.assertFalse(isPrime(10))
  def test_is_Prime_233(self):
    self.assertTrue(isPrime(233))
  def test_is_Prime_179425711(self):
    self.assertTrue(isPrime(179425711))
  def test_prime_sum_under_1(self):
    self.assertEqual(0, generatePrimeSumUnder(1))
  def test_prime_sum_under_2(self):
    self.assertEqual(0, generatePrimeSumUnder(2))
  def test_prime_sum_under_3(self):
    self.assertEqual(2, generatePrimeSumUnder(3))
  def test_prime_sum_under_10(self):
    self.assertEqual(17, generatePrimeSumUnder(10))
  def test_prime_sum_under_20(self):
    self.assertEqual(77, generatePrimeSumUnder(20))
  def test_prime_sum_under_1000(self):
    self.assertEqual(76127, generatePrimeSumUnder(1000))
  def test_prime_sum_under_1000(self):
    self.assertEqual(76127, generatePrimeSumUnder(1000))
  def test_prime_sum_under_10000(self):
    self.assertEqual(5736396, generatePrimeSumUnder(10000))
  def test_prime_sum_under_10000(self):
    self.assertEqual(37550402023, generatePrimeSumUnder(1000000))
  def test_prime_sum_under_10000(self):
    self.assertEqual(142913828922, generatePrimeSumUnder(2000000))
  

    
    

  
    

  
if __name__ == '__main__':
  unittest.main()

