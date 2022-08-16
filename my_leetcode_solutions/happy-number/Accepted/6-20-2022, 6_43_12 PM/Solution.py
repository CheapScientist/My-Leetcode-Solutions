// https://leetcode.com/problems/happy-number

class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        while n != 1: 
            if n in seen: return False
            seen.add(n)
            temp = 0
            for i in str(n):
                temp += int(i)**2
            n = temp
        return True