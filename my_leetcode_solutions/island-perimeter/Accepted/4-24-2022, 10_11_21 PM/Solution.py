// https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r not in range(rows) or
                    c not in range(cols) or
                    (r, c) in visit or
                    grid[r][c] == 0):
                return 0
            visit.add((r, c))
            ans = howManyNei(r, c)
            ans += dfs(r + 1, c)
            ans += dfs(r - 1, c)
            ans += dfs(r, c + 1)
            ans += dfs(r, c - 1)
            return ans
        def howManyNei(r, c):
            start = 4
            if r + 1 in range(rows):
                if grid[r + 1][c] == 1:
                    start -= 1
            if r - 1 in range(rows):
                if grid[r - 1][c] == 1:
                    start -= 1
            if c + 1 in range(cols):
                if grid[r][c + 1] == 1:
                    start -= 1
            if c - 1 in range(cols):
                if grid[r][c - 1] == 1:
                    start -= 1
            return start

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)