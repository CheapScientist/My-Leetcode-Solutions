// https://leetcode.com/problems/number-of-islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # dfs/bfs solution, mark visited positions as set
        if not grid: return 0
        rows, cols = len(grid), len(grid[0])
        res = 0 
        visit = set()
        
        def bfs(r, c):
            dq = collections.deque()
            visit.add((r, c))
            dq.append((r, c))
            
            directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
            
            while dq:
                row, col = dq.pop()
                for dr, dc in directions:
                    rr, cc = row + dr, col + dc
                    if (rr in range(rows) and
                       cc in range(cols) and
                       (rr, cc) not in visit and 
                       grid[rr][cc] == '1'):
                        visit.add((rr, cc))
                        dq.append((rr, cc))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    visit.add((r, c))
                    bfs(r, c)
                    res += 1
        return res
        