// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        # self.maxVal = float('-inf')
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                return 0 
            # two decisions: 1. rob today but have to at least wait a day
            a1 = nums[i] + dfs(i + 2)
            # 2. do not rob today and wait till tomorrow
            a2 = dfs(i + 1)
            memo[i] = max(a1, a2)
            return max(a1, a2)
            
        return dfs(0)
        
        
        