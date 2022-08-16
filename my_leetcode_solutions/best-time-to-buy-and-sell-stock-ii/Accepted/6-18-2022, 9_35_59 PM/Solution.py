// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1: return 0
        have, Nhave = 0, 0 
        have = -prices[0]
        for i in range(1, n): 
            have = max(-prices[i] + Nhave, have)
            Nhave = max(prices[i] + have, Nhave)
        return Nhave
        