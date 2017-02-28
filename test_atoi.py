import unittest
from atoi import *


class TestAtoi(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testAtoi(self):
        for i in range(10000):
            self.assertEqual(self.solution.myAtoi("2147483648"), 2147483647, "test failed")
            self.assertEqual(self.solution.myAtoi("010"), 10, "test failed")
            self.assertEqual(self.solution.myAtoi("-123a1"), -123, "test failed")
            self.assertEqual(self.solution.myAtoi(""), 0, "test failed")
            self.assertEqual(self.solution.myAtoi("+"), 0, "test failed")


if __name__ == '__main__':
    unittest.main()
