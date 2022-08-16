// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount + 1)
        for i in range(1, amount + 1):
            tempMin = float('inf')
            for coin in coins:
                if i - coin >=0: 
                    tempMin = min(tempMin, dp[i - coin])
            dp[i] = 1 + tempMin
        return dp[-1] if dp[-1] != float('inf') else -1
        