// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)  == 1:
            return 0
        if len(nums) == 2:
            return 1 
        dp = [0]*len(nums)
        # dp[1] = 1 if nums[-2] != 0 else float('inf')
        for i in range(len(nums) - 2, -1, -1):
            j = len(nums) -1 - i
            dp[j] = 1 + min(dp[max(j - nums[i], 0):j]) if nums[i] != 0 else float('inf')
        return dp[-1]
        
        