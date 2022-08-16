// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible

class Solution:
    def minOperations(self, nums: list[int], numsDivide: list[int]) -> int:
        def helper(a, b):
            if not b:
                return abs(a)
            return helper(b, a % b)

        nums.sort()
        if len(numsDivide) == 1:
            res = -1
            for j, i in enumerate(nums):
                if numsDivide[0]%i == 0:
                    res = j
                    return res
            return res
        ans = numsDivide[0]
        n = len(numsDivide)
        for i in range(1, n):
            ans = min(ans, helper(numsDivide[i], numsDivide[i - 1]))

        res = -1
        for j, i in enumerate(nums):
            if ans % i == 0:
                res = j
                return res
        return res