import unittest
from two_sum import *


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1], "test failed")


if __name__ == '__main__':
    unittest.main()
