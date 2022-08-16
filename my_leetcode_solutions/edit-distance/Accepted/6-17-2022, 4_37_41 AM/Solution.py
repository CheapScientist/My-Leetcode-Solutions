// https://leetcode.com/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word1), len(word2)
        dp = [[0]*(cols + 1) for _ in range(rows + 1)]
        for r in range(1, rows + 1): 
            dp[r][0] = r
        for c in range(1, cols + 1): 
            dp[0][c] = c
        for r in range(1, rows + 1): 
            for c in range(1, cols + 1): 
                if word1[r - 1] == word2[c - 1]: 
                    dp[r][c] = min(dp[r - 1][c - 1], 1 + dp[r - 1][c], 1 + dp[r][c - 1])
                else:
                    dp[r][c] = min(1 + dp[r - 1][c - 1], 1 + dp[r - 1][c], 1 + dp[r][c - 1])
        return dp[-1][-1]