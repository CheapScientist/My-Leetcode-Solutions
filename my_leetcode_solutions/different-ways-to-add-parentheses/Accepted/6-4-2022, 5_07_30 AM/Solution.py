// https://leetcode.com/problems/different-ways-to-add-parentheses

class Solution:
    def diffWaysToCompute(self, s: str) -> List[int]:
        operators = '+-*'
        
        
        def dfs(s):
            if s.isdigit():
                return [int(s)]
            ans = []
            for i, j in enumerate(s):
                if j in operators:
                    for a in dfs(s[:i]):
                        for b in dfs(s[i + 1:]):
                            ans.append(eval('a' + j + 'b'))

            return ans
        
        
        return dfs(s)