// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if diff == nums[j]:
                    return [i, j]
                    break