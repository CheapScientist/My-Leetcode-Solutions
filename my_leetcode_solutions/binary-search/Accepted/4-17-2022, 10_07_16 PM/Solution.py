// https://leetcode.com/problems/binary-search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r)//2
            if nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                return m
            else:
                l = m + 1
        return -1