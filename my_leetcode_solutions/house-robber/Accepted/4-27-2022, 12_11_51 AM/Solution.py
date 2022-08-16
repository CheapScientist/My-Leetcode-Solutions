// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: list[int]) -> int:
        lookup = {}
        def rec(i):
            if i >= len(nums):
                return 0
            if i in lookup:
                return lookup[i]
            else:
                lookup[i] = max(nums[i] + rec(i + 2), rec(i + 1))
                return lookup[i]

        return rec(0)
        