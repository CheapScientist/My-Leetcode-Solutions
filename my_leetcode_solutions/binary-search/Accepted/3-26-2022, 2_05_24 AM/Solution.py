// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mi = (lo + hi)//2
            pivot = nums[mi]
            if pivot == target:
                return mi
            elif pivot > target:
                hi = mi - 1
            else:
                lo = mi + 1
        return -1
        