// https://leetcode.com/problems/wildcard-matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i >= len(s) and j >= len(p):
                # memo[(i, j)] = True
                return True
            if j >= len(p):
                # memo[(i, j)] = False
                return False
            if i >= len(s):
                if p[j] == '*':
                    memo[(i, j)] = dfs(i, j + 1)
                    return memo[(i, j)] 
                else:
                    memo[(i, j)] = False
                    return False
            
            if p[j] == '*':
                memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 1)
                return memo[(i, j)] 
            elif p[j] == '?':
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = (s[i] == p[j] and dfs(i + 1, j + 1))
                return memo[(i, j)] 
        return dfs(0, 0)
    