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
        
        # cache results
#         memo = {}
        
#         def dfs(i, canBuy):
#             if (i, canBuy) in memo:
#                 return memo[(i, canBuy)]
#             if i >= len(prices):
#                 return 0
#             # situation 1: I can buy stock today
#             if canBuy:
#                 # decision 1: buy stock
#                 res1 = -prices[i] + dfs(i + 1, False)
#                 # decision 2: not buy and just wait 
#                 res2 = dfs(i + 1, True)
#                 temp = max(res1, res2)
#             # situation 2: I have a stock at hand
#             else:
#                 # decision 1: sell it today, but I have to wait one more day to act
#                 res3 = prices[i] + dfs(i + 2, True)
#                 # decision 2: do not sell it today, just wait
#                 res4 = dfs(i + 1, False)
#                 temp = max(res3, res4)
#             memo[(i, canBuy)] = temp
#             return temp
#         ans = dfs(0, True) 
#         return ans