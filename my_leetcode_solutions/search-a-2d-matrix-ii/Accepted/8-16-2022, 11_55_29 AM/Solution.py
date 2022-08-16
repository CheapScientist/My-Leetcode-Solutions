// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        x, y = 0, cols - 1 
        
        while x < rows and y >= 0: 
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                x += 1
            elif matrix[x][y] > target:
                y -= 1
        return False