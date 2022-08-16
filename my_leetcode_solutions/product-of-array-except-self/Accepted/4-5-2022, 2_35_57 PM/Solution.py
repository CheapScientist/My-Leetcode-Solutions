// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        val = 1
        for i in range(len(nums)-1):
            val *= nums[i]
            res.append(val)
        val = 1
        for j in range(len(nums)-1, 0, -1):
            val *= nums[j]
            res[j-1] *= val
        return res