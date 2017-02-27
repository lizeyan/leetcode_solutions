import unittest
from longest_palindromic_substring import *


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testTwoSum(self):
        for i in range(10000):
            self.assertEqual(self.solution.longestPalindrome("aaaa"), "aaaa", "test failed")
            self.assertEqual(self.solution.longestPalindrome("abb"), "bb", "test failed")
            self.assertEqual(self.solution.longestPalindrome("abcabcbb"), "bcb", "test failed")
            self.assertEqual(self.solution.longestPalindrome("bbbbb"), "bbbbb", "test failed")
            self.assertEqual(self.solution.longestPalindrome("pwwkew"), "ww", "test failed")
            self.assertEqual(self.solution.longestPalindrome("c"), "c", "test failed")


if __name__ == '__main__':
    unittest.main()
