import unittest
from numseq.fib import fib
from numseq.geo import *
from numseq.prime import *


class TestKatas(unittest.TestCase):

    def test_fib(self):
        self.assertEqual(fib(8), 21)

    def test_square(self):
        self.assertEqual(square(5), 25)

    def test_triangle(self):
        self.assertEqual(triangle(4), 10)

    def test_cube(self):    
        self.assertEqual(cube(3), 18)

    def test_cube(self):    
        self.assertEqual(is_prime(999981), False)
        self.assertEqual(is_prime(999983), True)


if __name__ == '__main__':
    unittest.main()    
