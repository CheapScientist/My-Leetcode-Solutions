// https://leetcode.com/problems/power-of-two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0:
            return False
        while n > 1:
            if n % 2 == 1:
                return False
            else:
                n = n // 2
        return True