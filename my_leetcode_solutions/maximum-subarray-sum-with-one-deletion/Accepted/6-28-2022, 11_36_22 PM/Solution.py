// https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('-inf')] * 2 for _ in range(n)]
        res = float('-inf')
        for i, a in enumerate(arr):
            dp[i][0] = max(a, dp[i - 1][0] + a)
            dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + a)
            res = max(res, *dp[i])
        return res