// https://leetcode.com/problems/target-sum

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        
        def dfs(i, build):
            if (i, build) in memo:
                return memo[(i, build)]
            if i == len(nums):
                if build == target:
                    return 1 
                else:
                    return 0
            res = 0
            res += dfs(i + 1, build + nums[i])
            res += dfs(i + 1, build - nums[i])
            memo[(i, build)] = res
            return res
        
        return dfs(0, 0)
        