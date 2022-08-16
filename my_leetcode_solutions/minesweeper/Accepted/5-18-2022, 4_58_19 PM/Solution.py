// https://leetcode.com/problems/minesweeper

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board: return []
        rows, cols = len(board), len(board[0])
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        visit = set()
        
        def dfs(r, c):
            if (not inRange(r, c) or 
               (r, c) in visit or 
               board[r][c] == 'M'):
                return 
            visit.add((r, c))
            nofMines = helper(r, c)
            if nofMines != 0:
                board[r][c] = str(nofMines)
            else:
                board[r][c] = 'B'
                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    dfs(nr, nc)

        def inRange(r, c):
            if rows > r >= 0 and cols > c >= 0:
                return True
            else:
                return False
        
        def helper(r, c):
            nofMines = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if inRange(nr, nc) and board[nr][nc] == 'M':
                    nofMines += 1
            return nofMines
        
        dfs(click[0], click[1])
        return board
            
        
        