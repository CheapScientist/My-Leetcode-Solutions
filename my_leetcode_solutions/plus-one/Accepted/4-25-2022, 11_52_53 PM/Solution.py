// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        plus1 = [1]
        res = []
        for i in range(len(digits) - 1, -1, -1):
            a1 = plus1.pop() if plus1 else 0
            ans = digits[i] + a1 + carry
            carry = ans//10
            ans = ans%10
            res.append(ans)
        if carry:
            res.append(1)
        return res[::-1]
            