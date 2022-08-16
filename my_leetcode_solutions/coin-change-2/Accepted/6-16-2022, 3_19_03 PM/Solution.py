// https://leetcode.com/problems/coin-change-2

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if not amount: return 1
        memo = {}
        def dfs(i, build):
            if (i, build) in memo:
                return memo[(i, build)]
            if build > amount: 
                # memo[(i, build)] = False
                return False
            if build == amount:
                # memo[(i, build)] = True
                return True
            if i == len(coins):
                return False
            res1 = dfs(i, build + coins[i])
            res2 = dfs(i + 1, build)
            memo[(i, build)] = res1 + res2
            return res1 + res2
        return dfs(0, 0)