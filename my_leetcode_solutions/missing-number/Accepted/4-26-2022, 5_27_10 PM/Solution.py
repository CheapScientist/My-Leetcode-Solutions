// https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        prev = 0
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                return prev + 1
            prev = nums[i]
        return prev + 1