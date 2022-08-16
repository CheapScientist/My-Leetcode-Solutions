// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        build = []
        
        def dfs(A, B):
            if not B: 
                res.append(build[:])
                return 
            for i, j in enumerate(B): 
                build.append(j)
                dfs(A + [j], B[:i] + B[i + 1:])
                build.pop()
            return
        
        dfs([], nums)
        return res