// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0]*cols for _ in range(rows)]
        ans = 0
        mod = 10**9 + 7
        def dfs(i, j): 
            if not dp[i][j]:
                val = grid[i][j]
                a1 = dfs(i - 1, j) if i > 0 and val > grid[i - 1][j] else 0
                a2 = dfs(i + 1, j) if i + 1 < rows and val > grid[i + 1][j] else 0
                a3 = dfs(i, j - 1) if j > 0 and val > grid[i][j - 1] else 0
                a4 = dfs(i, j + 1) if j + 1 < cols and val > grid[i][j + 1] else 0
                dp[i][j] = 1 + a1 + a2 + a3 + a4
            return dp[i][j]
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c)
                ans += dp[r][c]
                ans %= mod
        return ans