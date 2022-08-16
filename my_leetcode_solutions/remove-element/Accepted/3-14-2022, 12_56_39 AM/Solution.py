// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        end = len(nums) - 1
        while i in range(len(nums)):
            if nums[i] == val:
                nums[i], nums[end], end = nums[end], nums[i], end - 1
                nums.pop()
            else:
                i += 1
        return len(nums)