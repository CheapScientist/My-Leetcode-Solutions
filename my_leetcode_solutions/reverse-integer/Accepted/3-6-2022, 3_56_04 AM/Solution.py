// https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        strX = str(abs(x))
        b = strX[::-1]
        reversedNum = int(b)
        if x < 0:
            reversedNum = -reversedNum

        if reversedNum <= -2**(31) or reversedNum >= 2**(31) -1:
            return 0
        else:
            return reversedNum