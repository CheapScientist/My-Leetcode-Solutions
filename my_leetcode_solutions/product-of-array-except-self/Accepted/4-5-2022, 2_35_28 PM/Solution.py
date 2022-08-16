// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1]
        for i in range(len(nums) - 1):
            temp = nums[i]*output[-1]
            output.append(temp)
        rightProduct =  1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = rightProduct * output[i]
            rightProduct *= nums[i]
        return output