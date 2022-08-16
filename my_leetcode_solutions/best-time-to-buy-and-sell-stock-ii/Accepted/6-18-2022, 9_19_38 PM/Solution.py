// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @cache
        def dfs(i, have): 
            if i == len(prices): 
                return 0 
            if have: 
                a1 = prices[i] + dfs(i + 1, False)
                a2 = dfs(i + 1, True)
                return max(a1, a2)
            else:
                a3 = -prices[i] + dfs(i + 1, True)
                a4 = dfs(i + 1, False)
                return max(a3, a4)
        return dfs(0, False)