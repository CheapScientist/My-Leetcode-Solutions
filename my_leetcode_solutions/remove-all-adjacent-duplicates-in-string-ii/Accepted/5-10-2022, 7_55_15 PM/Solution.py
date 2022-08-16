// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # [['char', counts]]
        for i in s:
            if not stack:
                stack.append([i, 1])
            else:
                if stack[-1][0] == i:
                    if stack[-1][1] + 1 == k:
                        stack.pop()
                    else:
                        stack[-1] = [i, stack[-1][1] + 1]
                else:
                    stack.append([i, 1])
        res = ''
        for char, count in stack:
            res += char*count
        return res
            
        