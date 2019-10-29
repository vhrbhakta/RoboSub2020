import unittest
from gateMachine import check

class TestCheck(unittest.TestCase):

    def setUp(self):
        self.checker = check()


    def test_checkInputs(self):
        self.assertEqual(self.checker.checkInputs(["sys","1","1","1","False"]), False)
        self.assertEqual(self.checker.checkInputs(["sys","1","1","1","True"]), True)
        # self.assertEqual(self.checker.checkInputs(["sys",1,1,1,False]), False)

if (__name__ == '__main__'):
    unittest.main()

