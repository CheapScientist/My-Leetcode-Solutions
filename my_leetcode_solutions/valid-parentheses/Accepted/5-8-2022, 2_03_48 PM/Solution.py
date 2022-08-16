// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']':'[', '}': '{'}
        stack = []
        
        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if not stack: 
                    return False
                if stack and stack[-1] == match[i]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False