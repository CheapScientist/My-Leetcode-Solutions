// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0
        
        def dfs(r, c): 
            if ((not rows > r >= 0) or 
               (not cols > c >= 0) or 
               grid[r][c] == "0"):
                return 
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1": 
                    dfs(r, c)
                    ans += 1
        return ans