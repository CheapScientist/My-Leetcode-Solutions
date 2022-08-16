// https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
