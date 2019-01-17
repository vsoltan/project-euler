#!/usr/bin/env python

import unittest

from lattice_paths import num_paths


class TestLatticePaths(unittest.TestCase):
    def test_paths_1(self):
        self.assertEquals(2, num_paths(1))

    def test_paths_2(self):
        self.assertEquals(6, num_paths(2))

    def test_paths_3(self):
        self.assertEquals(20, num_paths(3))

    def test_paths_4(self):
        self.assertEquals(70, num_paths(4))

    def test_paths_5(self):
        self.assertEquals(252, num_paths(5))

    def test_paths_10(self):
        self.assertEquals(184756, num_paths(10))


if __name__ == '__main__':
    unittest.main()
