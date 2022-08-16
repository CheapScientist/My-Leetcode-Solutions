// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1, len(nums)):
            temp = []
            for j in range(0, i):
                if nums[j] < nums[i]:
                    temp.append(dp[j])
            print(temp)
            if temp:
                dp[i] = 1+ max(temp)
            else:
                dp[i] = 1
        print(dp)
        return max(dp)