import unittest
from median import *


class TestMedian(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def testMedian(self):
        for i in range(10000):
            # self.assertEqual(self.solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8, 9]), 5, "test failed")
            self.assertEqual(self.solution.findMedianSortedArrays([1, 2, 5, 6], [3, 4, 7, 8, 9, 10]), 5.5, "test failed")
            # self.assertEqual(self.solution.findMedianSortedArrays([1, 2], [3, 4]), 2.5, "test failed")
            # self.assertEqual(self.solution.findMedianSortedArrays([1, 2, 3, 4, 5, 6, 7, 9, 10], [8]), 5.5, "test failed")
            # self.assertEqual(self.solution.findMedianSortedArrays([1, 3], [2]), 2.0, "test failed")


if __name__ == '__main__':
    unittest.main()
    # solution = Solution()
    # print (solution.findMedianSortedArrays([1, 2], [3, 4]))
