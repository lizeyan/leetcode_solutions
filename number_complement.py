class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(''.join(list('0' if i == '1' else '1' for i in bin(num)[2:])), 2)
