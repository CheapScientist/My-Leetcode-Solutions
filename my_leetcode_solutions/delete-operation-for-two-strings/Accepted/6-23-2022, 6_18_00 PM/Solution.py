// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        
        @cache
        def dfs(i, j): # i -> word1, j -> word2
            if i == n and j == m: 
                return 0
            if i == n and j < m: 
                return m - j
            if i < n and j == m: 
                return n - i
            if word1[i] == word2[j]: 
                return dfs(i + 1, j + 1)
            else:
                return 1 + min(dfs(i + 1, j), dfs(i, j + 1))
        
        return dfs(0, 0)