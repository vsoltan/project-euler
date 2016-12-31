#!/usr/bin/env python
import unittest
from squared_sequence import squaredSequence
from squared_sequence import squareofSum

class TestStringMethods(unittest.TestCase):
  def test_squared_sequence_1(self):
    self.assertEqual(1, squaredSequence(1))
    
  def test_squared_sequence_2(self):
    self.assertEqual(5, squaredSequence(2))
    
  def test_squared_sequence_3(self):
    self.assertEqual(14, squaredSequence(3))
    
  def test_squared_sequence_4(self):
    self.assertEqual(30, squaredSequence(4))
    
  def test_squared_sequence_5(self):
    self.assertEqual(55, squaredSequence(5))
  
  def test_squared_sequence_15(self):
    self.assertEqual(1240, squaredSequence(15))
  
  def test_squared_sequence_15(self):
    self.assertEqual(1240, squaredSequence(15))
    
  def test_squared_sequence_100(self):
    self.assertEqual(338350, squaredSequence(100))
  
  def test_squared_sequence_1000(self):
    self.assertEqual(333833500, squaredSequence(1000))
    
  def test_square_of_Sum_1(self):
    self.assertEqual(1, squareofSum(1))
    
  def test_square_of_Sum_2(self):
    self.assertEqual(9, squareofSum(2))
  
  def test_square_of_Sum_3(self):
    self.assertEqual(36, squareofSum(3))
    
  def test_square_of_Sum_4(self):
    self.assertEqual(100, squareofSum(4))
    
  def test_square_of_Sum_5(self):
    self.assertEqual(225, squareofSum(5))
    
  def test_square_of_Sum_15(self):
    self.assertEqual(14400, squareofSum(15))
    
  def test_square_of_Sum_100(self):
    self.assertEqual(25502500, squareofSum(100))
    
  def test_square_of_Sum_1000(self):
    self.assertEqual(250500250000, squareofSum(1000))
    
  
    
  
    
  
if __name__ == '__main__':
    unittest.main()