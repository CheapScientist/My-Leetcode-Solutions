// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]
        mx = 1
        for i in range(1, len(nums)):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, 1 + dp[j])
            dp.append(temp)
            mx = max(mx, temp)

        return mx
            
        