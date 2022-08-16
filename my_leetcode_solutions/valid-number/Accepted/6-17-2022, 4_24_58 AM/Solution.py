// https://leetcode.com/problems/valid-number

class Solution:
    def isNumber(self, s: str) -> bool:
        sign, digit, dot, e = False, False, False, False
        signStr = "+-"
        for i in s: 
            if i in signStr: 
                if sign or dot or digit: return False
                sign = True
            elif i == '.': 
                if e or dot: return False
                dot = True
                # digit = False
            elif i.isdigit(): 
                digit = True
            elif i in 'eE': 
                if not digit or e: return False
                e = True
                sign = False
                digit = False
                dot = False
            else: 
                return False
        return digit 