// https://leetcode.com/problems/longest-ideal-subsequence

class Solution:
    def longestIdealString(self, s, k):
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(dp[i], max(dp[max(0, i - k) : min(26, i + k + 1)]) + 1)
        return max(dp)