// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel = 0
        ans = True
        n = len(nums)
        for i in range(n):
            fuel = max(fuel-1, nums[i])
            if fuel==0 and i!=n-1:
                ans = False
                break
        return ans