// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        stacka, stackb = list(a), list(b)
        carry = 0
        ansStr = ''
        lena, lenb = len(a), len(b)
        for i in range(min(lena, lenb)):
            ans = int(stacka.pop()) + int(stackb.pop()) + carry
            if ans >= 2:
                carry = 1
                ans = ans % 2
            else:
                carry = 0
            ansStr += str(ans)
        while stacka:
            ans = int(stacka.pop()) + carry
            if ans >= 2:
                carry = 1
                ans = ans % 2
            else:
                carry = 0
            ansStr += str(ans)
        while stackb:
            ans = int(stackb.pop()) + carry
            if ans >= 2:
                carry = 1
                ans = ans % 2
            else:
                carry = 0
            ansStr += str(ans)
        if carry == 1:
            ansStr += '1'
        return ansStr[::-1]