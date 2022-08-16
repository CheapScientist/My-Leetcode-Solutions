// https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start,end = len(nums), 0
        
        stack = []
        for i in reversed(range(len(nums))):  #finding end index of unsorted subarray
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)
        
        stack = []
        for i in range(len(nums)):  #finding start index of unsorted subarray
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)
        
        res = end - start + 1
        return res if res > 0 else 0 