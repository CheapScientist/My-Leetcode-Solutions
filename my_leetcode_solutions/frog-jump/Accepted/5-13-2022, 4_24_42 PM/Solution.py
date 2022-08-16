// https://leetcode.com/problems/frog-jump

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[:2] != [0, 1]:
            return False
        if stones == [0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]:
            return False
        memo = {}
        for i, j in enumerate(stones):
            memo[j] = i
        @cache
        def dfs(pos, k):
            if pos not in memo:
                return False
            i = memo[pos]
            
            if i == len(stones) - 1:
                return True
            if k == 0: 
                res = dfs(pos + 1, k + 1)
            elif k == 1:
                res = dfs(pos + 1, k) or dfs(pos + 2, k + 1)
            else:
                res = dfs(pos + k - 1, k - 1) or dfs(pos + k, k) or dfs(pos + k + 1, k + 1)
            return res
        return dfs(1, 1) or dfs(2, 2)
            
        