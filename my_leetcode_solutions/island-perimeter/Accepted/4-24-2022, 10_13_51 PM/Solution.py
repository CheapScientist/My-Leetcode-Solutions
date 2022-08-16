// https://leetcode.com/problems/island-perimeter

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        ans = 0
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
                    ans += howManyNei(r, c)
        return ans