// https://leetcode.com/problems/rotting-oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        rotten = deque()
        healthyOranges = 0
        numberofMins = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    healthyOranges += 1
                elif grid[r][c] == 2:
                    rotten.append((r, c))
        
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        while rotten and healthyOranges > 0: 
            for i in range(len(rotten)):
                r, c = rotten.popleft()
                for rr, cc in directions:
                    rp = r + rr
                    cp = c + cc
                    if (rp in range(rows) and cp in range(cols) and 
                        grid[rp][cp] == 1):
                        healthyOranges -= 1
                        grid[rp][cp] = 2
                        rotten.append((rp, cp))
            numberofMins += 1
        return -1 if healthyOranges else numberofMins
        