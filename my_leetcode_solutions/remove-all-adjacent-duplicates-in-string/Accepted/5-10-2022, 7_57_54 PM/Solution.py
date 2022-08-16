// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] == i:
                    stack.pop()
                else:
                    stack.append(i)
        return ''.join(stack)
        