// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums = [10,9,2,5,3,7,101,18]
        # dp = [1, 1, 1, 2, 2, 3, 4, 4]
        # a = [0,1,0,3,2,3]
        # dp = [1, 2, 0, 3, 3, 4]
        
        dp = [1]
        mx = 1
        for i in range(1, len(nums)):
            temp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    temp = max(temp, 1 + dp[j])
            dp.append(temp)
            mx = max(mx, temp)
        # print(dp)
        return mx
            
        