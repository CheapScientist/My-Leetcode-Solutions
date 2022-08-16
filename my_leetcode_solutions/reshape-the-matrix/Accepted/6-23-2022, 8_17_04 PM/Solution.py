// https://leetcode.com/problems/reshape-the-matrix

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows*cols != r*c or (rows == r and cols == c): return mat
        ans = []
        for row in range(rows):
            ans.extend(mat[row])
        res = []
        l = 0
        for _ in range(r): 
            res.append(ans[l:l+c])
            l += c 
        return res