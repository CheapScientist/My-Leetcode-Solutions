// https://leetcode.com/problems/n-queens-ii

class Solution:
    
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        cset, d1set, d2set = set(), set(), set()
        
        def dfs(r):
            if r == n: 
                self.res += 1
                return 
            for c in range(n):
                if (c not in cset and 
                   (r + c) not in d1set and 
                   (r - c) not in d2set):
                    cset.add(c)
                    d1set.add((r + c))
                    d2set.add((r - c))
                    # self.board[r][c] = 'Q'
                    dfs(r + 1)
                    cset.remove(c)
                    d1set.remove((r + c))
                    d2set.remove((r - c))
            return
        dfs(0)
        return self.res