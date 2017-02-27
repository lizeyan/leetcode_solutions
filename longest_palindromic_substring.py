class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(s) + '#'
        center = 0
        max_right = 0
        length_right = []
        for i in range(len(s)):
            if i < max_right:
                count = min(length_right[(center << 1) - i], max_right - i)
            else:
                count = 1
            while i + count < len(s) and i - count >= 0 and s[i + count] == s[i - count]:
                count += 1
            count -= 1
            if i + count > max_right:
                max_right = i + count
                center = i
            length_right.append(count)
        longest_index = 0
        longest_length = 0
        for index in range(len(length_right)):
            if length_right[index] > longest_length:
                longest_length = length_right[index]
                longest_index = index
        return s[longest_index - longest_length:longest_index + longest_length].replace('#', '')
