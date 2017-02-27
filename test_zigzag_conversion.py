import unittest
from zigzag_conversion import *


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        for i in range(10000):
            self.assertEqual(self.solution.convert("A", 2), "A", "test failed")
            self.assertEqual(self.solution.convert("AB", 1), "AB", "test failed")
            self.assertEqual(self.solution.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR", "test failed")


if __name__ == '__main__':
    unittest.main()
