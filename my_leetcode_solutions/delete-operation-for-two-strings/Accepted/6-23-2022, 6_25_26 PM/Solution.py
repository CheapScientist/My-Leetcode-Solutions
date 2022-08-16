// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        # word1 = "sea"; word2 = "eat"
        # rows: word2, cols: word1
        # dp = [[0, 0, 0, 0],
        #       [0, 0, 0, 0],
        #       [0, 0, 0, 0],
        #       [0, 0, 0, 0]]
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for c in range(1, n + 1): 
            dp[0][c] = c
        for r in range(1, m + 1): 
            dp[r][0] = r
        for r in range(1, m + 1):
            for c in range(1, n + 1): 
                # 2 cases: if word1[c] == word2[r]: dp[r][c] = dp[r - 1][c - 1]
                if word1[c - 1] == word2[r - 1]: 
                    dp[r][c] = dp[r - 1][c - 1]
                else:   
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1])
        return dp[-1][-1]
        