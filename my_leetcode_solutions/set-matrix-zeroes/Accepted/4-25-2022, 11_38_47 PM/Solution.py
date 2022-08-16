// https://leetcode.com/problems/set-matrix-zeroes

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        rows, cols = len(matrix), len(matrix[0])
        zerosR, zerosC = set(), set()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zerosR.add(r)
                    zerosC.add(c)
        for r in range(rows):
            for c in range(cols):
                if r in zerosR or c in zerosC:
                    matrix[r][c] = 0
        
        