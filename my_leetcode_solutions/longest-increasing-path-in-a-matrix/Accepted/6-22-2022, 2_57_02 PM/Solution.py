// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        # dp[i][j] is the LIP at (i, j)
        # to update dp, if it is larger than its adj grids, = 1 + adj
        # else it's one
        rows, cols = len(A), len(A[0])
        dp = [[0]*cols for _ in range(rows)]
        
        def dfs(i, j): 
            if not dp[i][j]:
                val = A[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > A[i - 1][j] else 0,
                    dfs(i + 1, j) if i < rows - 1 and val > A[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > A[i][j - 1] else 0,
                    dfs(i, j + 1) if j < cols - 1 and val > A[i][j + 1] else 0)
            return dp[i][j]
        return max(dfs(x, y) for x in range(rows) for y in range(cols))