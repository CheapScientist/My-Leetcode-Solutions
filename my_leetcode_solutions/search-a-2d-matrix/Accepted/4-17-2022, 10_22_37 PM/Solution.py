// https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix: return False
        rows, cols = len(matrix[0]), len(matrix)
        # do a bs for cols first since we know that cols are sorted
        leftc, rightc = 0, cols - 1
        # get all col elements into a list
        colList = []
        for i in range(cols):
            colList.append(matrix[i][0])

        while leftc <= rightc:
            midc = (leftc + rightc) // 2
            if colList[midc] > target:
                rightc = midc - 1
            elif colList[midc] == target:
                return True
            else:
                leftc = midc + 1
        # here leftc is set to the row that's ready for a second bs
        leftr, rightr = 0, rows - 1
        rowList = matrix[leftc - 1]
        while leftr <= rightr:
            midr = (leftr + rightr) // 2
            if rowList[midr] > target:
                rightr = midr - 1
            elif rowList[midr] == target:
                return True
            else:
                leftr = midr + 1
        return False