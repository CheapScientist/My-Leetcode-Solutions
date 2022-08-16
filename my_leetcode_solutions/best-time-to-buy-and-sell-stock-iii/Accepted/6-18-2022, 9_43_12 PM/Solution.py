// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @cache
        def dfs(i, have, trans_remain): 
            if trans_remain == 0 or i == n: 
                return 0
            if have: 
                # currently holding a stock, have 2 decisions: 
                # 1. sell it and have one less trans_remain
                a1 = prices[i] + dfs(i + 1, False, trans_remain - 1)
                # 2. do not sell it and hold it till tomorrow
                a2 = dfs(i + 1, True, trans_remain)
                return max(a1, a2)
            else: 
                # currently not having a stock, have 2 decisions: 
                # 1. buy one 
                a3 = -prices[i] + dfs(i + 1, True, trans_remain)
                a4 = dfs(i + 1, False, trans_remain)
                return max(a3, a4)
        return dfs(0, False, 2)