// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        @cache
        def dfs(i, have): # index, have a stock or not
            if i >= n: return 0
            # if have a stock: 
            if have: 
                # I have 2 decisions with a stock: 
                # 1. sell it and wait two days
                a1 = prices[i] + dfs(i + 2, False)
                # 2. do not act at all
                a2 = dfs(i + 1, True)
                return max(a1, a2)
            # If I do not have a stock at hand, again I have 2 decisions:
            # 1. buy a stock
            # 2. do not act today
            else:
                a3 = -prices[i] + dfs(i + 1, True)
                a4 = dfs(i + 1, False)
                return max(a3, a4)
        return dfs(0, False)