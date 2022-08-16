// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return -1
        if len(nums) == 1: return nums[0]
        n = len(nums)
        prev = nums[0]
        res = prev
        for i in range(1, n): 
            prev = max(nums[i] + prev, nums[i])
            res = max(res, prev)
        return res