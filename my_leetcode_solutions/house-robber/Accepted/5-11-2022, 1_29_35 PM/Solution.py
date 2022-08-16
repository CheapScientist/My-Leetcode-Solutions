// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        # self.maxVal = float('-inf')
        dp = [0]*(len(nums))
        maxSoFar = float('-inf')
        for i in range(len(nums)):
            a1 = dp[i - 1] if i > 0 else 0
            a2 = dp[i - 2] if i > 1 else 0
            dp[i] = max(a1, nums[i] + a2)
            maxSoFar = max(maxSoFar, dp[i])
            
        return maxSoFar
        
        
        