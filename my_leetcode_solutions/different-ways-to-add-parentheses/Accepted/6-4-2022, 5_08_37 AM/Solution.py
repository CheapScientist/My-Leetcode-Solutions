// https://leetcode.com/problems/different-ways-to-add-parentheses

class Solution:
    def diffWaysToCompute(self, s):
        return [eval('a'+c+'b')
                for i, c in enumerate(s) if c in '+-*'
                for a in self.diffWaysToCompute(s[:i])
                for b in self.diffWaysToCompute(s[i+1:])] or [int(s)]