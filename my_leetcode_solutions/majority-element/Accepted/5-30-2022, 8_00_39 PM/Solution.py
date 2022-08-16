// https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums):
        if len(nums) == 1:
            return nums[0]
        candidate = nums[0]
        vote = 1
        for num in nums[1:]:
            if candidate == num:
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    candidate = num
                    vote = 1
        return candidate