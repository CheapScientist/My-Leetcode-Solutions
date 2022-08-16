// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #       prices = [7,1,5,3,6,4]
        #               [[],   have a stock
        #                [] ]  do not have one
        n = len(prices)
        if n == 1: return 0
        dp = [[0]*n for _ in range(2)]
        dp[0][0] = -prices[0]
        for i in range(1, n): 
            dp[0][i] = max(-prices[i] + dp[1][i - 1], dp[0][i - 1])
            dp[1][i] = max(prices[i] + dp[0][i - 1], dp[1][i - 1])

        return dp[1][-1]
        
        # memo = {}
        # def dfs(i, have): 
        #     if (i, have) in memo: 
        #         return memo[(i, have)]
        #     if i == len(prices): 
        #         return 0 
        #     if have: 
        #         a1 = prices[i] + dfs(i + 1, False)
        #         a2 = dfs(i + 1, True)
        #         memo[(i, have)] = max(a1, a2)
        #         return max(a1, a2)
        #     else:
        #         a3 = -prices[i] + dfs(i + 1, True)
        #         a4 = dfs(i + 1, False)
        #         memo[(i, have)] = max(a3, a4)
        #         return max(a3, a4)
        # return dfs(0, False), memo