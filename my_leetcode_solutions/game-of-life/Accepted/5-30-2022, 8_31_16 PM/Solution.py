// https://leetcode.com/problems/game-of-life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return None
        rows, cols = len(board), len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        memo = {}
        
        def helper(r, c):
            numofOnes = 0
            for direction in directions:
                dr, dc = direction
                newr, newc = r + dr, c + dc
                if rows > newr >= 0 and cols > newc >=0 and board[newr][newc] == 1:
                    numofOnes += 1
            return numofOnes
        
        for r in range(rows):
            for c in range(cols):
                numof1 = helper(r, c)
                memo[(r, c)] = numof1 + memo.get((r, c), 0)
        
        for r in range(rows):
            for c in range(cols):
                numof1 = memo[(r, c)]
                if board[r][c] == 1:
                    if 3 >= numof1 >= 2:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0
                else:
                    if numof1 == 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 0
            
        
        