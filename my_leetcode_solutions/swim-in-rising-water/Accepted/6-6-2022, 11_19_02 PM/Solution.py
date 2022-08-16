// https://leetcode.com/problems/swim-in-rising-water

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        if not grid: return -1
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        minH = [(grid[0][0], 0, 0)]
        
        while minH: 
            cost, r, c = heapq.heappop(minH)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r == rows - 1 and c == cols - 1:
                return cost
            for direction in directions:
                dr, dc = direction
                newr, newc = r + dr, c + dc
                if not(rows > newr >= 0) or not(cols > newc >= 0) or (newr, newc) in visit:
                    continue
                heapq.heappush(minH, [max(cost, grid[newr][newc]), newr, newc])
            
                