// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            dp, res = max(nums[i], nums[i] + dp), max(res, dp)
        return max(res, dp)
        