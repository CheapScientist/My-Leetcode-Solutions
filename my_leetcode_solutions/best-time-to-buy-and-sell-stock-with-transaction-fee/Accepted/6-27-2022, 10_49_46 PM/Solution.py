// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int):
        n = len(prices)
        # dp[0][i] represents the state of having a stock
        # dp[1][i] represents the state of not having a stock
        have = -prices[0]
        clear = 0
        for i in range(1, n): 
            # if we have a stock today, that means we have just bought one, or we have one yesterday and did not act 
            clear = max(clear, prices[i] - fee + have)
            have = max(have, -prices[i] + clear)
        return clear
        
#         @cache
#         def dfs(i, hold): # i is the index of prices we are currently at; hold indicate whether we have a stock at hand
#             if i == n: return 0
#             # if we have a stock:
#             if hold: 
#                 # action 1: sell it and pay the fee
#                 ans1 = prices[i] - fee + dfs(i + 1, False)
#                 # action 2: do not act and wait till tomorrow
#                 ans2 = dfs(i + 1, True)
#                 return max(ans1, ans2)
#             # if we do not have a stock
#             else:
#                 # action 3: buy a stock, now we have a stock
#                 ans3 = -prices[i] + dfs(i + 1, True)
#                 # action 4: do not act
#                 ans4 = dfs(i + 1, False)
#                 return max(ans3, ans4)
        
#         return dfs(0, False)
                
                