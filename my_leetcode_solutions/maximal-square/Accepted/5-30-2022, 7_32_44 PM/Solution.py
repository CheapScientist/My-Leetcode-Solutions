// https://leetcode.com/problems/maximal-square

class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        hasOne = False
        # initialize dp
        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            if matrix[r][0] == '1':
                dp[r][0] = 1
                hasOne = True
        for c in range(cols):
            if matrix[0][c] == '1':
                dp[0][c] = 1
                hasOne = True
        if hasOne:
            maxSq = 1
        else:
            maxSq = 0
         # now update dp and get max at the same time
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == '1':
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                maxSq = max(maxSq, dp[r][c])
        return maxSq ** 2
        
        