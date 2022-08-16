// https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        hashT = {}
        for i in range(len(nums)):
            if nums[i] in hashT:
                return [hashT[nums[i]], i]
            else:
                hashT[target - nums[i]] = i