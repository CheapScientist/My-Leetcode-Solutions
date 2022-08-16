// https://leetcode.com/problems/maximum-length-of-pair-chain

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        dp = [1]*n
        for i in range(n):
            start, end = pairs[i]
            for j in range(i):
                prevSt, prevEnd = pairs[j]
                if start > prevEnd:
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[-1]                