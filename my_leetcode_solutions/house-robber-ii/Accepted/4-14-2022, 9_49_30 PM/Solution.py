// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        def rob1(nums: list[int]):
            if len(nums) <= 2:
                return max(nums)
            nums[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            return nums[-1]
        
        a = rob1(nums[:-1])
        b = rob1(nums[1:])
        return max(a,b)