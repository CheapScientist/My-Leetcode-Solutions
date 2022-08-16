// https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        build = 1
        while build < n:
            build *= 4

        return build == n