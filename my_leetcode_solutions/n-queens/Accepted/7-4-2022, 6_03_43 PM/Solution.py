// https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        col = set()
        dia1, dia2 = set(), set()
        ans = []
        
        def dfs(row): 
            if row == n: 
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return 
            for c in range(n): 
                if (c not in col and 
                   (row + c) not in dia1 and 
                   (row - c) not in dia2):
                    board[row][c] = 'Q'
                    col.add(c)
                    dia1.add(row + c)
                    dia2.add(row - c)
                    dfs(row + 1)
                    board[row][c] = '.'
                    col.remove(c)
                    dia1.remove(row + c)
                    dia2.remove(row - c)
            return 
        
        dfs(0)
        return ans
                
        