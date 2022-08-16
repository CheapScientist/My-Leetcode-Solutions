// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # first check the rows:
        for i in range(9):
            temp = []
            for j in board[i][:]:
                if j in temp:
                    return False
                elif j in '0123456789':
                    temp.append(j)
        # then check the columns:
        for i in range(9):
            temp = []
            for k in range(9):
                if board[k][i] in temp:
                    return False
                elif board[k][i] in '0123456789':
                    temp.append(board[k][i])
        # then check sub-boxes:
        for rows in [3,6,9]:
            for columns in [3, 6, 9]:
                temp = []
                for subrows in range(rows - 3, rows):
                    for subcolumns in range(columns - 3, columns):
                        if board[subrows][subcolumns] in temp:
                            return False
                        elif board[subrows][subcolumns] in '0123456789':
                            temp.append(board[subrows][subcolumns])
        return True