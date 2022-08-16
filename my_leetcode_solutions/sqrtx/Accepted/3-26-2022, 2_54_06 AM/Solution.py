// https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x - 1
        if x <= 1:
            return x
        while l <= r:
            m = (l + r)//2
            if m**2 == x:
                return m
            elif m**2 > x:
                r = m - 1
            elif m**2 < x:
                l = m + 1
        return r