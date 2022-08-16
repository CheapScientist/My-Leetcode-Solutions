// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if str(x)[0] in '+-':
            x = int(str(x)[1:])
            sign = -1
        return sign * int(str(x)[::-1]) if -2**31 <= sign * int(str(x)[::-1]) <= 2**31 - 1 else 0