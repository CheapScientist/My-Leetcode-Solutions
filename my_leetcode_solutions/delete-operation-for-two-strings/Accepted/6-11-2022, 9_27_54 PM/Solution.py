// https://leetcode.com/problems/delete-operation-for-two-strings

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        @cache
        def dfs(i, j): 
            if (i == n and j == m):
                return 0
            if (i < n and j == m): 
                return n - i 
            if (i == n and j < m): 
                return m - j
            if word1[i] == word2[j]: 
                ans = dfs(i + 1, j + 1)
            else: 
                ans = min(1 + dfs(i + 1, j), 1 + dfs(i, j + 1))
            return ans
        
        return dfs(0, 0)