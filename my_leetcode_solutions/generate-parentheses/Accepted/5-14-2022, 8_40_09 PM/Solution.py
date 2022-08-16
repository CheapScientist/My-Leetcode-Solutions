// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(op, cl, path):
            if op == cl == n:
                res.append(path)
                return            
            if op < n:
                dfs(op + 1, cl, path + '(')
            if op > cl:
                dfs(op, cl + 1, path + ')')

            
        dfs(0, 0, '')
        return res
        
        