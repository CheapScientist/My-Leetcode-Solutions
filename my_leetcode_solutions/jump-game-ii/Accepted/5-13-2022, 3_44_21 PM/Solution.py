// https://leetcode.com/problems/jump-game-ii

class Solution:
    def jump(self, nums: List[int]) -> int:

        @cache
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if nums[i] == 0:
                return float('inf')
            temp = float('inf')
            for j in range(i+1, i+1+nums[i]):
                a1 = dfs(j)
                temp = min(temp, 1 + a1)
            # self.res = min(self.res, temp)
            return temp
        
        return dfs(0)
        
        