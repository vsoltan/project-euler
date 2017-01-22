#!/usr/bin/env python

import unittest

from lattice_paths import num_paths

class TestLatticePaths(unittest.TestCase):
  def test_paths_1(self):
    self.assertEquals(2, len(num_paths(1)))

  def test_paths_2(self):
    self.assertEquals(6, len(num_paths(2)))

  def test_paths_3(self):
    self.assertEquals(20, len(num_paths(3)))

if __name__ == '__main__':
    unittest.main()
