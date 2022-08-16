// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        
        def bs(arr: list[int], target: int) -> bool:
            l, r = 0, len(arr) - 1
            while l <= r:
                m = (l + r)//2
                if arr[m] == target:
                    return True
                if arr[m] < target: 
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        for r in range(rows):
            if bs(matrix[r], target):
                return True
        return False