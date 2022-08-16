// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        previous = nums[0]
        i = 1
        while i in range(len(nums)):
            if nums[i] == previous:
                nums.pop(i)
                # nums.append('_')
            else:
                previous = nums[i]
                i += 1
        return len(nums)
