#!/usr/bin/env python

import unittest

from lattice_paths import num_paths

class TestLatticePaths(unittest.TestCase):
  def test_paths_1(self):
    self.assertEquals(2, num_paths(1))

if __name__ == '__main__':
    unittest.main()
