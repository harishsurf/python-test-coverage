import unittest
from sample_calc import addition, multiplication


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        assert addition(3, 4) == 7

    def test_multiply(self):
        assert multiplication(3,4) == 12
