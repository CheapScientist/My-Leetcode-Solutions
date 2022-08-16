// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)  == 1:
            return 0
        dp = [0]*len(nums)
        for i in range(len(nums) - 2, -1, -1):
            j = len(nums) -1 - i
            dp[j] = 1 + min(dp[max(j - nums[i], 0):j]) if nums[i] != 0 else float('inf')
        return dp[-1] if dp[-1] != float('inf') else -1
        
        