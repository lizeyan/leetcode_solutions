import unittest
from hamming_distance import *


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        self.assertEqual(self.solution.hammingDistance(1, 4), 2, "test failed")
        self.assertEqual(self.solution.hammingDistance(54, 20), 2, "test failed")


if __name__ == '__main__':
    unittest.main()
