// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums)==1:
            return True
        
        minn = 1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>=minn:
                reach = True
            else:
                reach = False
            if reach:
                minn=1
            else:
                minn+=1
                
        return reach