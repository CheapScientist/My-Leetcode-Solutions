// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()
        ans = 0
        
        def dfs(r, c):
            if (r not in range(rows) or 
               c not in range(cols) or 
               (r, c) in visit or 
               grid[r][c] == '0'):
                return False
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return True
        
        for r in range(rows): 
            for c in range(cols):
                if grid[r][c] == '1' and dfs(r, c):
                    ans += 1
        return ans 