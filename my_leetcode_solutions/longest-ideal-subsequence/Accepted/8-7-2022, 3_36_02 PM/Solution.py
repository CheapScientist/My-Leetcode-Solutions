// https://leetcode.com/problems/longest-ideal-subsequence

class Solution:
    def longestIdealString(self, s, k):
        dp = [[0] * 26 for _ in range(len(s) + 1)]
        ans = 0
        for i in range(1, len(s) + 1):
            x = ord(s[i - 1]) - ord('a')
            temp = 0
            for j in range(26):
                dp[i][j] = dp[i - 1][j]
                if abs(x - j) <= k:
                    temp = max(1 + dp[i - 1][j], temp)
            dp[i][x] = temp

        # print(dp)
        # print([ord(i) - ord('a') for i in s])
        return max(dp[-1])