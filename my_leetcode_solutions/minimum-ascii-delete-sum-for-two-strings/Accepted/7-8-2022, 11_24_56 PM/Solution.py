// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        # dp[i][j] means lowest cost for s1[:i] (inclusive, exclusive) and s2[:j]
        # e.g s1 =  s e a
        #           ord(i)
        #        e   
        #        a
        #        t
        
        dp = [[0]*(n + 1) for _ in range(m + 1)]
        for i in range(1, n + 1):
            dp[0][i] = ord(s1[i - 1]) + dp[0][i - 1]
        for j in range(1, m + 1):
            dp[j][0] = ord(s2[j - 1]) + dp[j - 1][0]
        for r in range(1, m + 1): 
            for c in range(1, n + 1): 
                if s1[c - 1] == s2[r - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(ord(s2[r - 1]) + dp[r - 1][c], ord(s1[c - 1]) + dp[r][c - 1])
        # print(dp)
        return dp[-1][-1]
        
