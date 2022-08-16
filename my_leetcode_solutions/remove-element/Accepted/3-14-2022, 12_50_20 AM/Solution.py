// https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i in range(len(nums)):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)