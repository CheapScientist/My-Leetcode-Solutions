// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        maxSoFar = 0
        memo = {}
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            val = matrix[r][c]
            ans = 1 + max(dfs(r + 1, c) if r + 1 < rows and matrix[r + 1][c] > val else 0, 
                         dfs(r - 1, c) if r - 1 >= 0 and matrix[r - 1][c] > val else 0, 
                         dfs(r, c + 1) if c + 1 < cols and matrix[r][c + 1] > val else 0, 
                         dfs(r, c - 1) if c - 1 >= 0 and matrix[r][c - 1] > val else 0)
            memo[(r, c)] = ans 
            return ans
        
        
        for r in range(rows):
            for c in range(cols):
                ans = dfs(r, c)
                maxSoFar = max(ans, maxSoFar)
        return maxSoFar