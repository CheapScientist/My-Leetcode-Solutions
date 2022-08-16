// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        res = 1
        for i in range(1, len(nums)):
            temp = 0
            for j in range(0, i):
                if nums[j] < nums[i]:
                    temp = max(temp, dp[j])
            dp[i] = 1 + temp
            res = max(res, dp[i])
        return res