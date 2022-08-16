// https://leetcode.com/problems/2-keys-keyboard

class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def dfs(i, j): # i is how many 'A''s we have, j is how many 'A''s we copied
            if i > n: 
                return float('inf')
            if i == n: 
                return 0
            # we have two decisions: 
            # 1. copy i -> (i, j) -> (i, i)
            # 2. paste i -> (i, j) -> (i+j, j)
            if j == 0: 
                return 1 + dfs(i, i)
            if i != j:
                return 1 + min(dfs(i, i), dfs(i+j, j))
            if i == j:
                return 1 + dfs(i+j, j)
        return dfs(1, 0)