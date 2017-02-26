import unittest
from length_of_longest_substring import *


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        for i in range(10000):
            self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3, "test failed")
            self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1, "test failed")
            self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3, "test failed")
            self.assertEqual(self.solution.lengthOfLongestSubstring("c"), 1, "test failed")


if __name__ == '__main__':
    unittest.main()
