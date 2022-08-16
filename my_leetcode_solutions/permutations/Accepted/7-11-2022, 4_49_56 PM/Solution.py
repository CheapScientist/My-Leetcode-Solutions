// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(remain, path):
            if not remain:
                res.append(path[:])
                return
            for i in range(len(remain)):
                dfs(remain[:i]+remain[i+1:], path+[remain[i]])

        dfs(nums, [])
        return res