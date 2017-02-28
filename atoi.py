class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        int_max = (1 << 31) - 1
        int_min = -(1 << 31)
        import re
        str = re.match("\s*([^\s]*)", str).group(1)
        if len(str) == 0:
            return 0
        digit_start_index = 0
        sign = 1
        if str[digit_start_index] == "+":
            digit_start_index += 1
            pass
        elif str[digit_start_index] == "-":
            sign = -sign
            digit_start_index += 1
        digit_end_index = digit_start_index
        while digit_end_index < len(str) and str[digit_end_index] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            digit_end_index += 1
        value = 0
        if digit_end_index > digit_start_index:
            value = int(str[digit_start_index:digit_end_index])
        return max(min(sign * value, int_max), int_min)

