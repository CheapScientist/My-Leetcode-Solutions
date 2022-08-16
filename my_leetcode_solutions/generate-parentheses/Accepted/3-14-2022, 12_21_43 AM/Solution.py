// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int):
        res = []

        def recursive(opened, closed, stringBuilder):
            if opened == closed == 0:
                res.append(stringBuilder)
            if opened < closed:
                recursive(opened,closed -1,stringBuilder + ')')
            if opened > 0:
                recursive(opened -1, closed, stringBuilder + '(')
            return res
        return recursive(n, n, "")
