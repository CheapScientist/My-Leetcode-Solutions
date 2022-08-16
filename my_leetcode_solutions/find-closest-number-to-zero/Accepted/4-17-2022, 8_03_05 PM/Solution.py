// https://leetcode.com/problems/find-closest-number-to-zero

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        distance = float('inf')
        ans = float('-inf')
        for i in nums:
            if abs(i) < distance: 
                distance = abs(i)
                ans = i
            elif abs(i) == distance: 
                ans = max(ans, i)
        return ans
            