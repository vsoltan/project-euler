#!/usr/bin/env python
import unittest

from squared_sequence import squared_sequence
from squared_sequence import square_of_sum


class TestStringMethods(unittest.TestCase):
    def test_squared_sequence_1(self):
        self.assertEqual(1, squared_sequence(1))

    def test_squared_sequence_2(self):
        self.assertEqual(5, squared_sequence(2))

    def test_squared_sequence_3(self):
        self.assertEqual(14, squared_sequence(3))

    def test_squared_sequence_4(self):
        self.assertEqual(30, squared_sequence(4))

    def test_squared_sequence_5(self):
        self.assertEqual(55, squared_sequence(5))

    def test_squared_sequence_15(self):
        self.assertEqual(1240, squared_sequence(15))

    def test_squared_sequence_100(self):
        self.assertEqual(338350, squared_sequence(100))

    def test_squared_sequence_1000(self):
        self.assertEqual(333833500, squared_sequence(1000))

    def test_square_of_Sum_1(self):
        self.assertEqual(1, square_of_sum(1))

    def test_square_of_Sum_2(self):
        self.assertEqual(9, square_of_sum(2))

    def test_square_of_Sum_3(self):
        self.assertEqual(36, square_of_sum(3))

    def test_square_of_Sum_4(self):
        self.assertEqual(100, square_of_sum(4))

    def test_square_of_Sum_5(self):
        self.assertEqual(225, square_of_sum(5))

    def test_square_of_Sum_15(self):
        self.assertEqual(14400, square_of_sum(15))

    def test_square_of_Sum_100(self):
        self.assertEqual(25502500, square_of_sum(100))

    def test_square_of_Sum_1000(self):
        self.assertEqual(250500250000, square_of_sum(1000))


if __name__ == '__main__':
    unittest.main()
