import unittest
import test

class TestSumBoy(unittest.TestCase):
    def test_sumBoy(self):
        self.assertEqual(test.sumBoy(1, 1), 2)
