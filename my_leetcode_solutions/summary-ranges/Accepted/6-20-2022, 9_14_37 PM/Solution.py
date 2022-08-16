// https://leetcode.com/problems/summary-ranges

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        r = 0
        while r < len(nums):
            temp = r
            while r + 1 < len(nums) and nums[r + 1] == nums[r] + 1:
                r += 1
            if temp == r:
                res.append(str(nums[r]))
            else:
                res.append(str(nums[temp]) + '->' + str(nums[r]))
            r += 1
        return res