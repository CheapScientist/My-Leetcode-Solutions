// https://leetcode.com/problems/range-sum-of-sorted-subarray-sums

class Solution:
    def rangeSum(self, nums: list[int], n: int, left: int, right: int) -> int:
        new = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                new.append(s)
        new.sort()
        sum1 = 0 
        for k in range(left - 1, right):
            sum1 += new[k]
        return sum1%(10**9 + 7)