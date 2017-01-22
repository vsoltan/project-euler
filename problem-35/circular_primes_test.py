
import unittest

from circular_primes import isPrime
from circular_primes import getDigitList
from circular_primes import combine

class TestStringMethods(unittest.TestCase):
  def test_isPrime_0(self):
    self.assertFalse(isPrime(0))
  def test_isPrime_1(self):
    self.assertFalse(isPrime(1))
  def test_isPrime_2(self):
    self.assertTrue(isPrime(2))
  def test_isPrime_3(self):
    self.assertTrue(isPrime(3))
  def test_isPrime_9(self):
    self.assertFalse(isPrime(9))
  def test_isPrime_179425711(self):
    self.assertTrue(isPrime(179425711))
  def test_getDigitList_100(self):
    self.assertListEqual(['1', '0', '0'], getDigitList(100))
  def test_getDigitList_123(self):
    self.assertListEqual(['1', '2', '3'], getDigitList(123))
  def test_getDigitList_12874289(self):
    self.assertListEqual(['1', '2', '8', '7', '4', '2', '8', '9'], getDigitList(12874289))
  def test_combine(self):
    self.assertEqual(123, combine(['1', '2', '3']))

if __name__ == '__main__':
      unittest.main()
    
    