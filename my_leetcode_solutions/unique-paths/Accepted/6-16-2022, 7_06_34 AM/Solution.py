// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if not m or not n: return 0
        dp = [[1]*n for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n): 
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]