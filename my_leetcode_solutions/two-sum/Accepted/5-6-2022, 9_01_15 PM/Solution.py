// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {}
        if not nums: return []
        for i, j in enumerate(nums):
            if target - j in memo:
                return i, memo[target - j]
            if j not in memo:
                memo[j] = i
