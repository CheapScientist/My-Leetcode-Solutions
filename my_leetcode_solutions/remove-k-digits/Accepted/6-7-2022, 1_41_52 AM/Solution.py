// https://leetcode.com/problems/remove-k-digits

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = k
        for i in num: 
            while remain and stack and stack[-1] > i: 
                stack.pop()
                remain -= 1
            stack.append(i)
        stack = stack[:len(stack) - remain]
        return str(int(''.join(stack))) if stack else "0"
                        
        