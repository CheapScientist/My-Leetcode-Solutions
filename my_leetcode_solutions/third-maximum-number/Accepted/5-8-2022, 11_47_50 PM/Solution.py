// https://leetcode.com/problems/third-maximum-number

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        nums.sort()
        res = [nums[0]]
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                res.append(nums[i])
            prev = nums[i]
        return res[-3] if len(res) >= 3 else res[-1]