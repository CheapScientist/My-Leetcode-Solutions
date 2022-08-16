// https://leetcode.com/problems/unique-paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1
        for x in range(1,m):
            for y in range(1,n):
                dp[x][y]=dp[x-1][y]+dp[x][y-1]
        return dp[m-1][n-1]
        