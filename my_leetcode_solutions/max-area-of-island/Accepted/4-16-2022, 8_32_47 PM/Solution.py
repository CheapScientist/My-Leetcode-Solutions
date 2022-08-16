// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxArea = 0 
        
        def dfs(r, c):
            if ((r, c) in visit or 
               r < 0 or c < 0 or 
               r == rows or c == cols or
               grid[r][c] == 0):
                
                return 0 
            
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r, c + 1) + dfs(r - 1, c) + dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 1 and (r, c) not in visit):

                    area = dfs(r, c)
                    maxArea = max(maxArea, area)
        
        return maxArea