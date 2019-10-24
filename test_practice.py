import unittest
from test import sumBoy

class TestSumBoy(unittest.TestCase):
    def test_sumBoy(self):
        self.assertEqual(sumBoy(1, 1), 2)

if __name__ == "__main__":
    unittest.main()