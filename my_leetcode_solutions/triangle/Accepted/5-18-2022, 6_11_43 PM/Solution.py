// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        @cache
        def dfs(i, j):
            if i == len(triangle):
                return 0
            return min(triangle[i][j] + dfs(i + 1, j), triangle[i][j] + dfs(i + 1, j + 1))
            
        return dfs(0, 0)

            
        
        