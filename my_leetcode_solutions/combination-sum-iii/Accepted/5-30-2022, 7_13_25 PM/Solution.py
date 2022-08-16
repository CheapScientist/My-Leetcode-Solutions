// https://leetcode.com/problems/combination-sum-iii

class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        
        def dfs(num, build, sum_so_far):
            if len(build) == k:
                if sum_so_far == n:
                    res.append(build)
                return 
            
            for i in range(num, 10):
                if sum_so_far + i > n:
                    break
                dfs(i + 1, build + [i], sum_so_far + i)
        
        dfs(1, [], 0)
        return res
        
        