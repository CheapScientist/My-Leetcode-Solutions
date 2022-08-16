// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(remaining, path):
            if not remaining:
                res.append(path[:])
                return
            for i in range(len(remaining)):
                dfs(remaining[:i] + remaining[i+1:], path + [remaining[i]])
        dfs(nums, [])
        return res