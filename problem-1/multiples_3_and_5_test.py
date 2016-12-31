#!/usr/bin/env python

import unittest
from multiples_3_and_5 import MultiplesOf3And5

class TestStringMethods(unittest.TestCase):
  def test_below_1(self):
    self.assertSetEqual(MultiplesOf3And5(1).multiples(), set())

  def test_below_3(self):
    self.assertSetEqual(MultiplesOf3And5(3).multiples(), set())

  def test_below_4(self):
    self.assertSetEqual(MultiplesOf3And5(4).multiples(), {3})

  def test_below_7(self):
    self.assertSetEqual(MultiplesOf3And5(7).multiples(), {3, 5, 6})

  def test_below_10(self):
    self.assertSetEqual(MultiplesOf3And5(10).multiples(), {3, 5, 6, 9})

  def test_sum_below_10(self):
    self.assertEqual(MultiplesOf3And5(10).sum_of_multiples(), 23)

  def test_below_16(self):
    self.assertSetEqual(MultiplesOf3And5(16).multiples(), {3, 5, 6, 9, 10, 12, 15})

  def test_sum_below_1000(self):
    self.assertEqual(MultiplesOf3And5(1000).sum_of_multiples(), 233168)

if __name__ == '__main__':
  unittest.main()
