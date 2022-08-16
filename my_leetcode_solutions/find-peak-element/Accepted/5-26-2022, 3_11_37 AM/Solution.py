// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i, j in enumerate(nums):
            prev = nums[i - 1] if i > 0 else float('-inf')
            nt = nums[i + 1] if i + 1 < len(nums) else float('-inf')
            if j > nt and j > prev:
                return i
        return -1
        