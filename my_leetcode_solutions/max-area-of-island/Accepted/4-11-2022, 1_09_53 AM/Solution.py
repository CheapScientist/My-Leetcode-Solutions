// https://leetcode.com/problems/max-area-of-island

class Solution(object):
    def maxAreaOfIsland(self, grid):
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if (r < 0 or r == rows or
                    c < 0 or c == cols or
                    grid[r][c] == 0 or
                    (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + 
                    dfs(r - 1, c) +
                    dfs(r, c + 1) + 
                    dfs(r, c - 1))
        area = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    area = max(area, dfs(r, c))
        return area
                    