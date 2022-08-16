// https://leetcode.com/problems/rotate-function

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        s = sum(nums)
        # initialize f(0):
        f0 = 0
        coefficients = [i for i in range(len(nums))]
        for i, j in zip(coefficients, nums):
            f0 += i * j
        # then compute maxf in O(n):
        maxSoFar = f0
        for i in range(len(nums) - 1, -1, -1):
            tempRes = f0 + s - (len(nums))*nums[i]
            maxSoFar = max(maxSoFar, tempRes)
            f0 = tempRes
        return maxSoFar