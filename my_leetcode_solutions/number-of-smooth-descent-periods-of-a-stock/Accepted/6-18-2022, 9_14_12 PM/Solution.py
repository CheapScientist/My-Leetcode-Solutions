// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [1]*n
        res = 1
        if n == 1: return 1
        for i in range(1, n):
            now, prev = prices[i], prices[i - 1]
            if prev - now == 1: 
                dp[i] = 1 + dp[i - 1]
            res += dp[i]

        return res
                