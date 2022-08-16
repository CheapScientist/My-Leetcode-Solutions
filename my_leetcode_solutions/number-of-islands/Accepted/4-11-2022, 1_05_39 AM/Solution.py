// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        res = 0

        def dfs(r, c):
            if (r < 0 or r == rows or
                    c < 0 or c == cols or
                    grid[r][c] == '0' or
                    (r, c) in visit):
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res