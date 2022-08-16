// https://leetcode.com/problems/combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        build = []
        
        def dfs(i): 
            if len(build) == k: 
                res.append(build[:])
                return 
            for j in range(i, n + 1): 
                build.append(j)
                dfs(j + 1)
                build.pop()
            return 
        
        dfs(1)
        return res