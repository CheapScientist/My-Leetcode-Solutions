// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition

class Solution:
    def maximumGroups(self, A: List[int]) -> int:
        A.sort()
        ans = 0
        n = len(A)
        while n >= ans + 1:
            ans += 1
            n -= ans
            
        return ans
            
        
        