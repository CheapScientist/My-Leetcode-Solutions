// https://leetcode.com/problems/permutations-ii

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        def dfs(nums, path):
            visit = set()
            if not nums:
                res.append(path[:])
                return
            for i in range(len(nums)):
                if nums[i] not in visit:
                    visit.add(nums[i])
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
        dfs(nums, [])
        return res