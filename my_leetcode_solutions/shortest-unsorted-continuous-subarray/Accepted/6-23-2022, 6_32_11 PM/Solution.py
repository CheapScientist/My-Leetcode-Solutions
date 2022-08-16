// https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        temp = sorted(nums)
        l, r = 0, len(nums) - 1
        while l < len(nums): 
            if temp[l] != nums[l]:
                break
            l += 1
        while r >= 0 :
            if temp[r] != nums[r]:
                break
            if r <= l: return 0
            r -= 1
        return r - l + 1
        