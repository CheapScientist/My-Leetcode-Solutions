// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        # dp = [[0]*cols for _ in range(rows)]
        # initialize dp:
        # dp[0][0] = grid[0][0]
        for c in range(1, cols):
            grid[0][c] = grid[0][c] + grid[0][c - 1]
        for r in range(1, rows):
            grid[r][0] = grid[r][0] + grid[r - 1][0]
        
        # update dp
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] = grid[r][c] + min(grid[r][c - 1], grid[r - 1][c])
        return grid[-1][-1]