#!/usr/bin/env python

import unittest

from multiples_3_and_5 import multiples_of_3_and_5_below
from multiples_3_and_5 import sum_of_multiples_of_3_and_5_below


class TestStringMethods(unittest.TestCase):
    def test_below_1(self):
        self.assertSetEqual(multiples_of_3_and_5_below(1), set())

    def test_below_3(self):
        self.assertSetEqual(multiples_of_3_and_5_below(3), set())

    def test_below_4(self):
        self.assertSetEqual(multiples_of_3_and_5_below(4), {3})

    def test_below_7(self):
        self.assertSetEqual(multiples_of_3_and_5_below(7), {3, 5, 6})

    def test_below_10(self):
        self.assertSetEqual(multiples_of_3_and_5_below(10), {3, 5, 6, 9})

    def test_sum_below_10(self):
        self.assertEqual(sum_of_multiples_of_3_and_5_below(10), 23)

    def test_below_16(self):
        self.assertSetEqual(multiples_of_3_and_5_below(16), {3, 5, 6, 9, 10, 12, 15})

    def test_sum_below_1000(self):
        self.assertEqual(sum_of_multiples_of_3_and_5_below(1000), 233168)


if __name__ == '__main__':
    unittest.main()
