#!/usr/bin/env python

import unittest
from power_digit_sum import Power
from power_digit_sum import getSumDigits

class TestStringMethods(unittest.TestCase):
  def test_power_2_0(self):
    self.assertEqual(1, Power(2,0))
  def test_Power_2_3(self):
    self.assertEqual(8, Power(2,3))
  def test_power_2_4(self):
    self.assertEqual(16, Power(2,4))
  def test_power_2_15(self):
    self.assertEqual(32768, Power(2,15))
  def test_get_Sum_Digits_0(self):
    self.assertEquals(0, getSumDigits(0))
  def test_get_Sum_Digits_1(self):
    self.assertEquals(1, getSumDigits(1))
  def test_get_Sum_Digits_9(self):
    self.assertEquals(9, getSumDigits(9))
  def test_get_Sum_Digits_12(self):
    self.assertEquals(3, getSumDigits(12))
  def test_get_Sum_Digits_129(self):
    self.assertEquals(12, getSumDigits(129))
  def test_get_Sum_Digits_1290(self):
    self.assertEquals(12, getSumDigits(1290))
  def test_get_Sum_Digits_7584738475938475834534853495348534(self):
    self.assertEquals(182, getSumDigits(7584738475938475834534853495348534))
  def test_get_Sum_Digits_7584738475938475834534853495348534(self):
    self.assertEquals(1366, getSumDigits(Power(2,1000)))

if __name__ == '__main__':
    unittest.main()