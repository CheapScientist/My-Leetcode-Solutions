// https://leetcode.com/problems/longest-increasing-path-in-a-matrix

class Solution:
    def longestIncreasingPath(self, A: List[List[int]]) -> int:
        # dp[i][j] is the LIP at (i, j)
        # to update dp, if it is larger than its adj grids, = 1 + adj
        # else it's one
        rows, cols = len(A), len(A[0])
        dp = [[0]*cols for _ in range(rows)]
        
        def dfs(r, c): 
            if not dp[r][c]: 
                a3 = dfs(r + 1, c) if r + 1 < rows and A[r][c] < A[r + 1][c] else 0
                a1 = dfs(r - 1, c) if r and A[r][c] < A[r - 1][c] else 0
                a2 = dfs(r, c - 1) if c and A[r][c] < A[r][c - 1] else 0
                a4 = dfs(r, c + 1) if c + 1 < cols and A[r][c] < A[r][c + 1] else 0
                ans = 1 + max(a1, a2, a3, a4)
                dp[r][c] = ans
            return dp[r][c]
        return max(dfs(x, y) for x in range(rows) for y in range(cols))