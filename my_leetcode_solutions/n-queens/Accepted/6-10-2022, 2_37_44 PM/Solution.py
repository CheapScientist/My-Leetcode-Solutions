// https://leetcode.com/problems/n-queens

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."]*n for _ in range(n)]
        # dset1 (r - c), dset2 (r + c)
        res = []
        cset, diagset1, diagset2 = set(), set(), set()
        
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if (c not in cset and 
                    (r - c) not in diagset1 and 
                    (r + c) not in diagset2):
                    cset.add(c)
                    diagset1.add((r - c))
                    diagset2.add((r + c))
                    board[r][c] = 'Q'
                    dfs(r + 1)
                    
                    # backtrack
                    cset.remove(c)
                    diagset1.remove((r - c))
                    diagset2.remove((r + c))
                    board[r][c] = '.'
            return
        
        dfs(0)
        return res