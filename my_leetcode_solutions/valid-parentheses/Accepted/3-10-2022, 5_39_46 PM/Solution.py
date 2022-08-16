// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        pairDict = {')':'(', '}':'{', ']':'['}
        res = ''
        openS = '({['
        if len(s)%2 == 1:
            return False
        for i in s:
            if i in openS:
                res += i
            elif len(res) > 0 and res[-1] == pairDict[i]:
                res = res[:-1]
            else:
                return False
        if len(res) > 0:
            return False
        else:
            return True