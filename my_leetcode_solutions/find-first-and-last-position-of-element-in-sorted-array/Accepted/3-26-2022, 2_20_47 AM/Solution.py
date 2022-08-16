// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums:list[int], target: int):
        l = self.helper(nums, target, True)
        r = self.helper(nums, target, False)
        return [l, r]
    def helper(self, nums, target, LeftBias):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            mi = (l + r) // 2
            pivot = nums[mi]
            if pivot > target:
                r = mi -1
            elif pivot < target:
                l = mi + 1
            else:
                idx = mi
                if LeftBias:
                    r = mi - 1
                else:
                    l = mi + 1
        return idx