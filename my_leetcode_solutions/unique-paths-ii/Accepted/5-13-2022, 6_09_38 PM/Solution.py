// https://leetcode.com/problems/unique-paths-ii

class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        if not A: return 0
        rows, cols = len(A), len(A[0])
        if A[0][0] == 1 or A[-1][-1] == 1:
            return 0
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1
        for i in range(1, rows):
            if dp[i - 1][0] == 1 and A[i][0] != 1:
                dp[i][0] = 1
            else:
                dp[i][0] = 0
        for j in range(1, cols):
            if dp[0][j - 1] == 1 and A[0][j] != 1:
                dp[0][j] = 1
            else:
                dp[0][j] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if A[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]