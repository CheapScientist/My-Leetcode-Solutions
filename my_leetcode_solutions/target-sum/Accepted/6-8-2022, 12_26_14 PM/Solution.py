// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i, build):
            if i == len(nums):
                if build == target:
                    return 1 
                else:
                    return 0
            res = 0
            res += dfs(i + 1, build + nums[i])
            res += dfs(i + 1, build - nums[i])
            return res
        
        return dfs(0, 0)
        