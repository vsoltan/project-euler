import unittest
from largest_prime_factor import prime_factorization

class testLargestPrimeFactorTest(unittest.TestCase):

    def test_solution(self):
        self.assertEquals(6857, prime_factorization(600851475143))

    def test_zero(self):
        self.assertEqual(None, prime_factorization(0))

    def test_between_neg2and2(self):
        self.assertEqual(None, prime_factorization(-1))

    def test_one_factor1(self):
        self.assertEqual(2, prime_factorization(4))

    def test_one_factor2(self):
        self.assertEqual(3, prime_factorization(9))

    def test_more_complex(self):
        self.assertEqual(7, prime_factorization(14))

    def test_(self):
        self.assertEqual(17, prime_factorization(68))

if __name__ == '__main__':
    unittest.main()
