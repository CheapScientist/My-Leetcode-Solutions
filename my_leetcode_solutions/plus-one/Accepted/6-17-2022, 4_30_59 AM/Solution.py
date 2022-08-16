// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1)//10
        digits[-1] = (digits[-1] + 1)%10
        for i in range(len(digits) - 2, -1, -1): 
            ans = digits[i] + carry
            carry = ans//10
            digits[i] = ans%10
        if carry: 
            return [1] + digits
        else:
            return digits