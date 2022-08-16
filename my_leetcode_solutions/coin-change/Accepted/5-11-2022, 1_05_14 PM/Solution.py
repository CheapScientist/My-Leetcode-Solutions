// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        memo = {}
        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount in coins:
                return 1
            if amount < 0:
                return float('inf')
            temp = float('inf')
            for coin in coins:
                temp = min(temp, dfs(amount - coin))
            memo[amount] = 1 + temp
            return 1 + temp
        res = dfs(amount)
        return res if res != float('inf') else -1
        