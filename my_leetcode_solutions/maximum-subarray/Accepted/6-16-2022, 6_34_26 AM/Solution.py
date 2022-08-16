// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums) == 1: return nums[0]
        n = len(nums)
        dp = [0]*n
        dp[0] = nums[0]
        res = dp[0]
        for i in range(1, n): 
            dp[i] = max(nums[i] + dp[i-1], nums[i])
            res = max(res, dp[i])
        return res