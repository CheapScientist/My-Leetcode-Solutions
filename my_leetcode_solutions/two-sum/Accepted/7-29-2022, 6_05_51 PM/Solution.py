// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo = {} # num: idx
        for i, j in enumerate(nums):
            if target - j in memo:
                return [memo[target - j], i]
            memo[j] = i
            
        return -1