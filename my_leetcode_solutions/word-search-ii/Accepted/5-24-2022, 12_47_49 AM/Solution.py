// https://leetcode.com/problems/word-search-ii

class Trie(collections.defaultdict):
    def __init__(self):
        super().__init__(lambda: Trie())
        self._is_word = False
        self._count = 0
    
    def add(self, word):
        runner = self
        runner._count += 1
        for c in word:
            runner = runner[c]
            runner._count += 1
        runner._is_word = True
        
    def remove(self, word):
        runner = self
        runner._count -= 1
        for c in word:
            if runner[c]._count == 1:
                del runner[c]
                return
            runner = runner[c]
            runner._count -= 1
        runner._is_word = False
        
    def contains(self, word):
        runner = self
        for c in word:
            if runner._count == 0 or c not in runner:
                return False
            runner = runner[c]
        return runner._is_word
    


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        n, m = len(board), len(board[0])
        root = Trie()
        for word in words:
            root.add(word)
            
        def dfs(i, j, trie, s):
            s.append(board[i][j])
            trie = trie[board[i][j]]
            if trie._is_word:
                root.remove(s)
                trie._is_word = False
                res.append("".join(s))

            board[i][j] = '#'
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < n and 0 <= nj < m and board[ni][nj] in trie:
                    dfs(ni, nj, trie, s)
            board[i][j] = s.pop()
                
        res = []    
        for i in range(n):
            for j in range(m):
                if board[i][j] in root:
                    dfs(i, j, root, [])
                 
        return res  