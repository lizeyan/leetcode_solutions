class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        target = x ^ y
        return Solution.count_ones(target)

    @staticmethod
    def round(num, mask, c):
        return (num & mask) + (num >> (1 << c) & mask)

    @staticmethod
    def count_ones(num):
        num = Solution.round(num, 0x55555555, 0)
        num = Solution.round(num, 0x33333333, 1)
        num = Solution.round(num, 0x0f0f0f0f, 2)
        num = Solution.round(num, 0x00ff00ff, 3)
        num = Solution.round(num, 0x0000ffff, 4)
        return num
