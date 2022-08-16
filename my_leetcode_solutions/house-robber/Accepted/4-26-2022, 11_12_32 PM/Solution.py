// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[:2])]
        for i in range(2, len(nums)):
            dp.append(max(dp[-1], dp[i - 2] + nums[i]))
        return dp[-1]