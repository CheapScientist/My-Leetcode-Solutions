// https://leetcode.com/problems/combination-sum-iv

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        
        def dfs(build):
            if build in memo:
                return memo[build]
            if build == target:
                return 1
            if build > target:
                return 0
            temp = 0
            for i in range(n):
                temp += dfs(build + nums[i])
            memo[build] = temp
            return temp
        
        return dfs(0)