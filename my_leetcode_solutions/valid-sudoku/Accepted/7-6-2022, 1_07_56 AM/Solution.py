// https://leetcode.com/problems/valid-sudoku

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = cols = [[0, 2], [3, 5], [6, 8]]
        # first check rows:

        row = col = 9
        for r in range(row):
            cur_row = board[r]
            num = set()
            for x in cur_row:
                if x == '.': continue
                if x not in num:
                    num.add(x)
                else:
                    return False
        for c in range(col):
            num = set()
            for r in range(row):
                x = board[r][c]
                if x == '.': continue
                if x not in num:
                    num.add(x)
                else:
                    return False

        for r in rows:
            r_mn, r_mx = r
            for c in cols:
                c_mn, c_mx = c
                num = set()
                for rr in range(r_mn, r_mx + 1):
                    for cc in range(c_mn, c_mx + 1):
                        x = board[rr][cc]
                        if x == '.': continue
                        if x not in num:
                            num.add(x)
                        else:
                            return False
        return True