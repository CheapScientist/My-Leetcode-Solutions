// https://leetcode.com/problems/selling-pieces-of-wood

class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:
        memo = {}
        for h, w, price in prices:
            memo[h, w] = price
        @cache
        def dfs(r, c):
            
            ans = memo.get((r, c), 0)
            
            if r > 1: 
                for x in range(1, r//2 + 1):
                    ans = max(ans, dfs(r - x, c) + dfs(x, c))
            if c > 1:
                for y in range(1, c//2 + 1):
                    ans = max(ans, dfs(r, c - y) + dfs(r, y))
            return ans
        
        return dfs(m, n)
        