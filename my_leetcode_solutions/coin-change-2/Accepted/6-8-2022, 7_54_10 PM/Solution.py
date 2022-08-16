// https://leetcode.com/problems/coin-change-2

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount: return 1
        @cache
        def dfs(i, build):
            if build > amount: 
                return False
            if build == amount:
                return True
            if i == len(coins):
                return False
            res1 = dfs(i, build + coins[i])
            res2 = dfs(i + 1, build)
            return res1 + res2
        return dfs(0, 0)