// https://leetcode.com/problems/check-if-matrix-is-x-matrix

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols): 
                if r == c or (r + c) == rows - 1: 
                    if grid[r][c] == 0: 
                        return False
                else:
                    if grid[r][c] != 0:
                        return False
        return True