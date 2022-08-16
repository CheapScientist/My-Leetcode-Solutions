// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        n = len(prices)
        dp = [[0]*(n + 1) for _ in range(2)]
        dp[1][1] = -prices[0]
        for i in range(2, n + 1):
            res1 = prices[i - 1] + dp[1][i - 1]
            res2 = dp[0][i - 1]
            dp[0][i] = max(res1, res2)
            res3 = - prices[i - 1] + dp[0][i - 2]
            res4 = dp[1][i - 1]
            dp[1][i] = max(res3, res4)
        # print(dp)
        return max(dp[0][-1], dp[1][-1])