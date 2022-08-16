// https://leetcode.com/problems/strong-password-checker-ii

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        length = True if len(password) >= 8 else False
        if not length: return False
        upper, lower = False, False
        digit, special = False, False
        prev = password[0]
        spec = "!@#$%^&*()-+"
        if prev in spec: 
            special = True
        elif prev.isdigit(): 
            digit = True
        elif  0 <= ord(prev) - ord('a') <= 25: 
            lower = True
        else:
            upper = True
        
        for i in range(1, len(password)):
            cur = password[i]
            if cur == prev: return False
            if cur in spec: 
                special = True
            elif cur.isdigit(): 
                digit = True
            elif  0 <= ord(cur) - ord('a') <= 25: 
                lower = True
            else:
                upper = True
            prev = cur
        return True if (lower and upper and special and digit) else False