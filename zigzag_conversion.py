class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = []
        for i in range(numRows):
            rows.append([])
        direction = 1
        current_row = 0
        for char in s:
            rows[current_row].append(char)
            if current_row == 0:
                direction = 1
            elif current_row == numRows - 1:
                direction = -1
            current_row += direction
        return ''.join(''.join(item) for item in rows)

