// https://leetcode.com/problems/valid-perfect-square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mi = (l + r)//2
            if num == mi**2:
                return True
            elif num > mi**2:
                l = mi + 1
            else:
                r = mi - 1
        return False