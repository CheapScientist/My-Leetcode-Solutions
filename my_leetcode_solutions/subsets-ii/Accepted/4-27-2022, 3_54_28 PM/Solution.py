// https://leetcode.com/problems/subsets-ii

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        
        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1)
            while (i + 1 in range(len(nums))) and nums[i] == nums[i + 1]:
                i += 1
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res