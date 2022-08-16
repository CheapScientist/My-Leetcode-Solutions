// https://leetcode.com/problems/surrounded-regions

class Solution:
    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        # step one is to get the outmost indices
        outMost, visit = set(), set()
        for i in range(rows):
            outMost.add((i, 0))
            outMost.add((i, cols - 1))

        for j in range(cols):
            outMost.add((0, j))
            outMost.add((rows - 1, j))

        def dfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or (r, c) in visit or board[r][c] == 'X':
                return
            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r, c in outMost:
            if (board[r][c] == "O" and
                    (r, c) not in visit):
                dfs(r, c)

        for rr in range(rows):
            for cc in range(cols):
                if board[rr][cc] == "O" and (rr, cc) not in visit:
                    board[rr][cc] = 'X'