// https://leetcode.com/problems/intersection-of-multiple-arrays

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1: return sorted(nums[0])
        beginSet = set(nums.pop())
        
        while nums:
            cur = nums.pop()
            temp = set()
            for i in cur:
                if i in beginSet:
                    temp.add(i)
            beginSet = temp
        res = list(beginSet)
        res.sort()
        return res
        