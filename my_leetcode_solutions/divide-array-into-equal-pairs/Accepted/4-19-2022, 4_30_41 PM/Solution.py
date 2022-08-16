// https://leetcode.com/problems/divide-array-into-equal-pairs

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        prev, cur = 0, 1
        while cur < len(nums):
            if nums[cur] != nums[prev]:
                return False
            prev += 2
            cur += 2
        return True
        