// https://leetcode.com/problems/minimum-path-sum

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [grid[0][0]]*cols 
        for c in range(1, cols): 
            dp[c] = grid[0][c] + dp[c - 1]
        for r in range(1, rows): 
            temp = [grid[r][0] + dp[0]]*cols
            for c in range(1, cols): 
                temp[c] = grid[r][c] + min(dp[c], temp[c - 1])
            dp = temp[:]
        return dp[-1]