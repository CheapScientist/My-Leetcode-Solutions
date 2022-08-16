// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            if i >= len(s):
                if p[j] == '*':
                    return dfs(i, j + 1)
                else:
                    return False
            
            if p[j] == '*':
                a1 = dfs(i + 1, j)
                return a1 or dfs(i, j + 1)
            elif p[j] == '?':
                return dfs(i + 1, j + 1)
            else:
                return (s[i] == p[j] and dfs(i + 1, j + 1))
        return dfs(0, 0)
    