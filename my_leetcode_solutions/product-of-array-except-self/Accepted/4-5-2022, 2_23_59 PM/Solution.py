// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        leftProduct, rightProduct = [1], [1]
        for i in range(len(nums)):
            leftProduct.append(nums[i]*leftProduct[i])
            rightProduct.append(nums[len(nums) - 1 - i]*rightProduct[i])
        rightProduct = rightProduct[::-1]
        ans = []
        for i in range(len(nums)):
            ans.append(leftProduct[i]*rightProduct[i+1])
        return ans
        