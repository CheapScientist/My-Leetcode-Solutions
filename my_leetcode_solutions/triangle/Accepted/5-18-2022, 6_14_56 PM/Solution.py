// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == len(triangle):
                return 0
            memo[(i, j)] = min(triangle[i][j] + dfs(i + 1, j), triangle[i][j] + dfs(i + 1, j + 1))
            return memo[(i, j)]
            
        return dfs(0, 0)

            
        
        