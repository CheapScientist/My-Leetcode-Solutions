// https://leetcode.com/problems/sign-of-the-product-of-an-array

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg = 0
        for i in nums:
            if i < 0:
                neg += 1
            elif i == 0:
                return 0
        return (-1)**neg