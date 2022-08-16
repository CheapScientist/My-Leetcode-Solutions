// https://leetcode.com/problems/frog-jump

class Solution:
    def canCross(self, stones: List[int]) -> bool:

        memo = {}
        for i, j in enumerate(stones):
            memo[j] = i
        @cache
        def dfs(pos, k):
            if k <= 0:
                return False
            if pos not in memo:
                return False
            i = memo[pos]
            if i == len(stones) - 1:
                return True
            return dfs(pos + k, k - 1) or dfs(pos + k, k) or dfs(pos + k, k + 1)
        return dfs(0, 1)
            
        