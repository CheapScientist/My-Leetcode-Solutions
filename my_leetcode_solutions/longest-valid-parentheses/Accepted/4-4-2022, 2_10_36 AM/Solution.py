// https://leetcode.com/problems/longest-valid-parentheses

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l, r, mx = 0, 0, 0
        for i in s:
            if i == '(':
                l += 1
            else:
                r += 1
            if l == r:
                mx = max(mx, 2*r)
            elif r > l:
                l, r = 0, 0
        l, r = 0, 0
        for i in s[::-1]:
            if i == ')':
                r += 1
            else:
                l += 1
            if l == r:
                mx = max(mx, 2*l)
            elif r < l:
                l, r = 0, 0
        return mx