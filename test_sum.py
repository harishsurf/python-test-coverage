import unittest
from sample_add import addition


class MyTestCase(unittest.TestCase):
    def test_addition(self):
        assert addition(3, 4) == 7
