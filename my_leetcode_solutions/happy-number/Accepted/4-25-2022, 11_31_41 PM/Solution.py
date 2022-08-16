// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        lookup = set()
        lookup.add(n)
        def helper(n):
            x = str(n)
            ans = 0
            for i in x:
                ans += int(i)**2
            if ans in lookup:
                return False
            else:
                lookup.add(ans)
            if ans == 1:
                return True
            return helper(ans)
        while 1:
            return helper(n)
        
            
        