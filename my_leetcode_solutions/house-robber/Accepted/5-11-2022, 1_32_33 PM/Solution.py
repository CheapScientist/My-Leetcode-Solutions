// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        # self.maxVal = float('-inf')
        dpi1 = 0
        dpi2 = 0
        maxSoFar = float('-inf')
        for i in range(len(nums)):
            # a1 = dp[i - 1] if i > 0 else 0
            # a2 = dp[i - 2] if i > 1 else 0
            newMax = max(dpi1, nums[i] + dpi2)
            maxSoFar = max(maxSoFar, newMax)
            dpi2, dpi1 = dpi1, newMax
            
        return maxSoFar
        
        
        