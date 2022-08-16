// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = -prices[0]
        for i in range(1, n): 
            dp[0][i] = max(-prices[i] + dp[1][i - 1], dp[0][i - 1])
            dp[1][i] = max(prices[i] + dp[0][i - 1], dp[1][i - 1])

        return dp[1][-1]
        