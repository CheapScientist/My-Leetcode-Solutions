// https://leetcode.com/problems/longest-palindromic-subsequence

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        ss = s[::-1]
        
        dp = [[0]*(n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1): 
                if s[i - 1] == ss[j - 1]: 
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else: 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]