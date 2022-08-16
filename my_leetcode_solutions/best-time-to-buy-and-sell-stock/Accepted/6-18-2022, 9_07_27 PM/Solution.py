// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0
        prevMin = prices[0]
        res = 0
        for j in range(1, len(prices)):
            i = prices[j]
            res = max(res, i - prevMin)
            prevMin = min(prevMin, i)
        return res