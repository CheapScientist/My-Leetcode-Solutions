// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        rows, cols = len(matrix), len(matrix[0])
        new = [[0]*rows for _ in range(cols)]
        for r in range(cols):
            for c in range(rows):
                new[r][c] = matrix[c][r]
        return new