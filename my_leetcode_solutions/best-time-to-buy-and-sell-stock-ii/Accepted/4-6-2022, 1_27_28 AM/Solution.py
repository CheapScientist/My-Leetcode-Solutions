// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, prevMin = 0, float('inf')
        for i in prices:
            if i > prevMin:
                profit += i - prevMin
                prevMin = i
            else:
                prevMin = min(prevMin, i)
        return profit
        