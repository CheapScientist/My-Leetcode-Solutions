// https://leetcode.com/problems/valid-parenthesis-string

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        @cache
        def dfs(i, l, r): 
            if l < r: return False
            if i == n:
                if l == r: 
                    return True
                else:
                    return False
            if s[i] == "(":
                return dfs(i + 1, l + 1, r)
            if s[i] == ")":
                return dfs(i + 1, l, r + 1)
            if s[i] == "*":
                return dfs(i + 1, l + 1, r) or dfs(i + 1, l, r) or dfs(i + 1, l, r + 1)
        
        return dfs(0, 0, 0)