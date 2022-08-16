// https://leetcode.com/problems/longest-string-chain

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        ans = 1
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
            ans = max(ans, dp[w])
        return ans