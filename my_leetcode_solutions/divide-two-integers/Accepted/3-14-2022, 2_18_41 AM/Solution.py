// https://leetcode.com/problems/divide-two-integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        count = 0
        if dividend == 0:
            return 0
        if (divisor > 0 and dividend > 0) or (dividend < 0 and divisor < 0):
            sign = True
        else:
            sign = False
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp = divisor
            mul = 1
            while dividend >= temp:
                dividend -= temp
                count += mul
                mul += mul
                temp += temp
        if not sign:
            res = -count
        else:
            res = count
        return min(max(-2147483648,res),2147483647)