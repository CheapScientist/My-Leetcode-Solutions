// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits:list):
        carry, addOne, ans = 0, [1], []
        while digits:
            temp1 = digits.pop()
            temp2 = addOne.pop() if len(addOne) > 0 else 0
            ansNum = temp2 + temp1 + carry
            carry, ansNum = ansNum//10, ansNum%10
            ans.append(ansNum)
        if carry:
            ans.append(carry)
        return ans[::-1]