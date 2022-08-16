// https://leetcode.com/problems/max-area-of-island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        
        def dfs(r, c):
            if (r not in range(rows) or
               c not in range(cols) or 
               (r, c) in visit or 
               grid[r][c] == 0):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    temp = dfs(r, c)
                    maxArea = max(maxArea, temp)
        return maxArea
        
        # we are only visiting each element once, and all the lookup/search take O(1), so the overall TC is O(n*m) 
        # where n, c are the number of rows, cols, respectively
        # SC is O(n*m) bc of the visit set is at most (nm) big, call stack is at most (nm) long