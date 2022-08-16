// https://leetcode.com/problems/coin-change

class Solution:
    def coinChange(self, coins: list[int], amount: int):
        lookup = {}
        def rec(amount):
            if amount in lookup:
                return lookup[amount]
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf") - 1
            minCoins = float("inf")
            for ac in coins:
                minCoins = min(minCoins, 1 + rec(amount - ac))
            lookup[amount] = minCoins
            return minCoins
        a = rec(amount)
        if a != float('inf'):
            return a
        else:
            return -1