// https://leetcode.com/problems/word-search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        rows, cols = len(board), len(board[0])
        visit = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r not in range(rows) or 
               c not in range(cols) or 
               board[r][c] != word[i] or
               (r, c) in visit):
                return False
            visit.add((r, c))
            a1 = dfs(r + 1, c, i + 1)
            a2 = dfs(r - 1, c, i + 1)
            a3 = dfs(r, c + 1, i + 1)
            a4 = dfs(r, c - 1, i + 1)
            visit.remove((r, c))
            return (a1 or a2 or a3 or a4)
            
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False