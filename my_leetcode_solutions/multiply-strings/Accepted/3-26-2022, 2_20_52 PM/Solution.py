// https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        pow1, pow2 = len(num1) - 1, len(num2) - 1
        int1, int2 = 0, 0
        ord0 = ord('0')
        for i in num1:
            int1 += 10**pow1*(ord(i) - ord0)
            pow1 -= 1
        for i in num2:
            int2 += 10**pow2*(ord(i) - ord0)
            pow2 -= 1
        return str(int1*int2)