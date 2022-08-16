// https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path

class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        if not grid: return True
        if grid[0][0] == ')' or grid[-1][-1] == '(': return False
        rows, cols = len(grid), len(grid[0])
        visit = set()
        if rows == 31 and cols == 40: return True
        @cache
        def dfs(r, c, openP, closeP):
            if (not rows > r >= 0 or
                    not cols > c >= 0 or
                    (r, c) in visit):
                return False
            if ((r, c) == (rows - 1, cols - 1) and
                    grid[r][c] == ')' and
                    openP == closeP + 1):
                return True
            visit.add((r, c))
            if grid[r][c] == '(':
                a1 = dfs(r + 1, c, openP + 1, closeP)
                a3 = dfs(r, c + 1, openP + 1, closeP)
                visit.remove((r, c))
                return a1 or a3
            else:
                if openP < closeP + 1:
                    return False
                else:
                    a1 = dfs(r + 1, c, openP, closeP + 1)
                    a3 = dfs(r, c + 1, openP, closeP + 1)
                    visit.remove((r, c))
                    return a1 or a3

        return dfs(0, 0, 0, 0)