// https://leetcode.com/problems/replace-elements-in-an-array

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        memo = {}
        new = {}
        for i, j in enumerate(nums):
            memo[j] = i
        
        for fr, to in operations:
            new[memo[fr]] = to
            temp = memo[fr]
            del memo[fr]
            memo[to] = temp
        res = [0]*len(nums)
        for i, j in enumerate(nums):
            if i not in new:
                res[i] = nums[i]
            else:
                res[i] = new[i]
        return res