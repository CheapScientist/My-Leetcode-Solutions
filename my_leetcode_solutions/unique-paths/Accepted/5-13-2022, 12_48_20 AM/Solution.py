// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        # print(dp)
        for i in range(m):
            for j in range(n):
                if (i, j) != (0, 0):
                    a1 = dp[i - 1][j] if i > 0 else 0
                    a2 = dp[i][j - 1] if j > 0 else 0
                    dp[i][j] = a1 + a2
        return dp[-1][-1]
        