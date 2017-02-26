class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        previous_character = {}
        current_longest = 0
        substring_start = 0
        for i in range(0, len(s)):
            if s[i] in previous_character and previous_character[s[i]] >= substring_start:
                current_longest = max(current_longest, i - substring_start)
                substring_start = previous_character[s[i]] + 1
                previous_character[s[i]] = i
            else:
                previous_character[s[i]] = i
        current_longest = max(current_longest, len(s) - substring_start)
        return current_longest
